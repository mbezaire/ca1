# -*- coding: utf-8 -*-
""" 
    Helper method for dealing with NeuroML2 morphologies:
    1) in NEURON one can specify (eg.) a synaptic terminal along a segment group
    in NeuroML2 this is not possible, only along segments (with segmentID-not the name of the segment)
    -> this methods converts fractionAlong in a segmentGroup (NEURON way of doing it) into fractionAlong in a segment within a segment group (NeuroML2 way of doing it)
    2) the code deletes the numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
    Authors: András Ecker, Padraig Gleeson
"""

import neuroml

import neuroml.loaders as loaders
import neuroml.writers as writers

def helper_getlenght(prox, dist):
    
    import numpy as np
    return np.sqrt((dist[0]-prox[0])*(dist[0]-prox[0]) + (dist[1]-prox[1])*(dist[1]-prox[1]) + (dist[2]-prox[2])*(dist[2]-prox[2]))


def helper_morphology(morph_file):   

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
        else:
            print ("warning: This segmentGroup: %s hasn't got a NeuroLexID -> it's a branching cable!"%segGroup.id)
          
        # deletes numberInternalDivisions from annotation (will be valid -> it will be possible to visualize it on OSB)
        if segGroup.annotation:
            segGroup.annotation = None
    
    # iterates over segments in segment groups and calculates lenghts of segments
    dSegGroups = {}
    for groupID, segment_list in dSegGroupMembers.iteritems():
        segs = []
        lSegs = []
        for segID in segment_list:
            seg = doc.cells[0].morphology.segments[dSegIDs[segID]]
            if seg.proximal:
                prox = [seg.proximal.x, seg.proximal.y, seg.proximal.z]
                dist = [seg.distal.x, seg.distal.y, seg.distal.z]
            else:
                prox = dist  # TODO: check if segments within a segment group are always in order, otherwise prx should be parent.distal
                dist = [seg.distal.x, seg.distal.y, seg.distal.z]
            lSeg = helper_getlenght(prox, dist)
            segs.append(seg.id)
            lSegs.append(lSeg)
            
        dSegGroups[groupID] = [segs, lSegs]


    writers.NeuroMLWriter.write(doc, morph_file)
    print("Saved modified morphology file to: " + morph_file)

    return dSegGroups
  

def calc_seg_fracalong(dSegGroups, segGroupID, origFracAlong):
    
    segs = dSegGroups[segGroupID][0]; lengths = dSegGroups[segGroupID][1]
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

"""
# tested with the hippocampal network of Marianne Bezaire
if __name__ == "__main__":
    dSegGroups = helper_morphology("../cells/poolosyn.cell.nml")
    
    segGroup = "apical_116"
    segID, fracAlong = calc_seg_fracalong(dSegGroups, segGroup, 0.5)
    print segGroup, dSegGroups[segGroup], "segID: %g, fracAlong:%g"%(segID, fracAlong)
"""