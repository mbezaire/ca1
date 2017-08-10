#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Helper method to deal with NeuroML2 morphologies:
1) in NEURON one can specify (eg.) a synaptic terminal along a segment group
in NeuroML2 this is not possible, only along segments (with segmentID - not the name of the segment)
-> a method converts fractionAlong in a segmentGroup (NEURON way of doing it) into fractionAlong in a segment within a segment group (NeuroML2 way of doing it)
2) creates segmentGroups - based on distance from soma, used by opencortex to create connection between specified segmentGroups (to recreate the connectivity algo.)
+1) delete the numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
Authors: András Ecker, Padraig Gleeson
"""

import re
import numpy as np
    
import neuroml
import neuroml.loaders as loaders
import neuroml.writers as writers


def helper_getlength(prox, dist):
    """calculates the length of a segment"""    

    return np.sqrt((dist[0]-prox[0])*(dist[0]-prox[0]) + (dist[1]-prox[1])*(dist[1]-prox[1]) + (dist[2]-prox[2])*(dist[2]-prox[2]))
   

def helper_getdist(dist):
    """calculates distance (of distal end) of segment from 0,0,0 (Seg0_soma_0.proximal)"""

    return helper_getlength([0, 0, 0], dist)
  
  
def helper_morphology(morph_file):
    """loads in morphology and returns dictonary with segment groups""" 

    doc = loaders.NeuroMLLoader.load(morph_file)
    print("Loaded morphology file from: %s"%morph_file)

    # iterates over segments and get the index in the segment list corresponding to the segment id
    dSegIDs = {}
    for i, seg in enumerate(doc.cells[0].morphology.segments):
        dSegIDs[seg.id] = i

    # iterates over segment groups and get the ids of the segments within a group
    dSegGroupMembers = {}
    for segGroup in doc.cells[0].morphology.segment_groups:
        if segGroup.neuro_lex_id:
            dSegGroupMembers[segGroup.id] = []
            for member in segGroup.members:
                dSegGroupMembers[segGroup.id].append(member.segments)
        #else:
            #print ("warning: This segmentGroup: %s hasn't got a NeuroLexID -> it's a branching cable!"%segGroup.id)  # will print for segment group all, soma_group ... - comment out after 1st sanity check!
          
        # deletes numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
        if segGroup.annotation:
            segGroup.annotation = None
    
    # iterates over segments in segment groups and calculates lenghts of segments
    dSegGroups = {}
    for groupID, segment_list in dSegGroupMembers.iteritems():
        segs = []
        lSegs = []
        dSegs = []
        for segID in segment_list:
            seg = doc.cells[0].morphology.segments[dSegIDs[segID]]
            if seg.proximal:
                prox = [seg.proximal.x, seg.proximal.y, seg.proximal.z]
                dist = [seg.distal.x, seg.distal.y, seg.distal.z]
            else:
                prox = dist  # TODO: check if segments within a segment group are always in order, otherwise prox should be parent.distal
                dist = [seg.distal.x, seg.distal.y, seg.distal.z]
                
            lSeg = helper_getlength(prox, dist)
            dSeg = helper_getdist(dist)
            
            segs.append(seg.id)
            lSegs.append(lSeg)
            dSegs.append(dSeg)
            
        dSegGroups[groupID] = {"segments":segs, "lengths":lSegs, "distances":dSegs}

    writers.NeuroMLWriter.write(doc, morph_file)
    #print("Saved modified morphology file to: %s"%morph_file)

    return dSegGroups
  

def calc_seg_fracalong(dSegGroups, segGroupID, origFracAlong):
    """calculates correct NeuroML fractionAlong (for copying synapse placement extracted by NEURON)"""
    
    segs = dSegGroups[segGroupID]["segments"]; lengths = dSegGroups[segGroupID]["lengths"]
    totLen = sum(lengths)
    point = totLen * origFracAlong
    
    i = len(segs)-1; x = totLen
    while x > point:
        x -= lengths[i]
        i -= 1                
  
    segID = segs[i+1]
    remained = point - x 
    fracAlong = remained / lengths[i+1]

    return segID, fracAlong


def create_dendrite_list(morph_file, listName, dist_from, dist_to):
    """creates dendrite lists based on distance constraint (see syndata_* files) to replicate the original connectivity algorithm - using methods from opencortex"""
    
    # get basid properties of the morphology (see above)
    dSegGroups = helper_morphology(morph_file)
    
    # get segIDs, that meet the distance criterion
    dend_list = []
    for segGroup, props in dSegGroups.iteritems():
        if "soma" not in segGroup and "axon" not in segGroup:
            if listName == "dendrite_list":
                for i, dist in enumerate(props["distances"]):
                    if dist_from <= dist and dist <= dist_to:
                        dend_list.append(props["segments"][i])
                        
            elif listName == "apical_list" and "poolosyn" not in morph_file:
                if int(re.findall(r'\d', segGroup)[0]) in np.arange(0, 10):  # dend_0 ... dend_9 for all (but OLM) INs 
                    for i, dist in enumerate(props["distances"]):
                        if dist_from <= dist and dist <= dist_to:
                            dend_list.append(props["segments"][i])
            elif listName == "apical_list" and "poolosyn" in morph_file:
                if "apical" in segGroup:
                    for i, dist in enumerate(props["distances"]):
                        if dist_from <= dist and dist <= dist_to:
                            dend_list.append(props["segments"][i])
                                        
    # modify .cell.nml
    if dend_list:
        # create new segment group
        members = []
        for segment in dend_list:
            members.append(neuroml.Member(segments=segment))
            
        newSegGroup = neuroml.SegmentGroup(id="%s_%i_to_%i"%(listName, dist_from, dist_to),
                                           notes='segmentGroup added by A.Ecker to specify connection targets for opencortex (not added to segGroup id="all")',
                                           members=members)
                                           
        # add new group to cell file (bware it won't check if it already exists, just add!)
        doc = loaders.NeuroMLLoader.load(morph_file)
        morph = doc.cells[0].morphology
        morph.segment_groups.append(newSegGroup)
        
        writers.NeuroMLWriter.write(doc, morph_file)
    
    
# tested with the hippocampal network of Marianne Bezaire
if __name__ == "__main__":

    cell_types = ["axoaxonic", "bistratified", "cck", "ivy", "ngf", "poolosyn", "pvbasket", "sca"]
    for cell_type in cell_types:
        morph_file = "../cells/%s.cell.nml"%cell_type
        # will load in and save the morph file 5 times for every cell...
        create_dendrite_list(morph_file, "dendrite_list", 0, 50)
        create_dendrite_list(morph_file, "dendrite_list", 50, 200)
        create_dendrite_list(morph_file, "dendrite_list", 200, 1000)
        create_dendrite_list(morph_file, "apical_list", 100, 1000)
        create_dendrite_list(morph_file, "apical_list", 200, 1000)
        print("Saved modified morphology file to: %s"%morph_file)

    # some additional unique segment groups
    create_dendrite_list("../cells/ngf.cell.nml", "dendrite_list", 0, 1000)
    # OLM cell hasn't got apical_list so it's handeled differently
    morph_file = "../cells/olm.cell.nml"
    create_dendrite_list(morph_file, "dendrite_list", 0, 50)
    create_dendrite_list(morph_file, "dendrite_list", 50, 200)
    create_dendrite_list(morph_file, "dendrite_list", 200, 1000)
    create_dendrite_list(morph_file, "dendrite_list", 10, 1000)
    create_dendrite_list(morph_file, "dendrite_list", 100, 1000)
    print("Saved modified morphology file to: %s"%morph_file)

    # test fractionAlong calculation
    morph_file = "../cells/poolosyn.cell.nml"
    dSegGroups = helper_morphology(morph_file)
    segGroup = "apical_116"
    segID, fracAlong = calc_seg_fracalong(dSegGroups, segGroup, 0.5)
    print segGroup, dSegGroups[segGroup], "segID: %g, fracAlong:%g"%(segID, fracAlong)


