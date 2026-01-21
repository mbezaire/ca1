#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Creates a simplified NeuroML2 version of the hippocampal network by Marianne Bezaire (point neurons are easier to visulaize on OSB)
Note: almost copy-paste from GenerateHippocamplaNet.py
Authors: András Ecker, Padraig Gleeson, last update: 08.2017
"""

import os
import sys
import random as rnd
# NeuroML specific libraries
import neuroml
import neuroml.writers as writers
from pyneuroml import pynml
# helper functions from other scripts
from GenerateHippocampalNet_oc import helper_getcolor, helper_getcelltype
from GenerateHippocampalNet import helper_getscale, add_synapses

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])


def create_populations_simplified(net, cell_types, nrn_runname, randomSeed):
    """
    Reads original data files (mainly position.dat) and creates population of cells
    Note: only component type is different from GenerateHippocampalNet.py code !
    """

    # read in cell gids:
    fCellIDs = os.path.join(basePath, nrn_runname, "celltype.dat")
    dCellIDs = {}
    
    with open(fCellIDs, "r") as f:
        next(f)  # skip header: "celltype, techtype, typeIndex, rangeStart, rangeEnd"
        for line in f:
            if line.split()[0] not in ["ca3cell", "eccell"]:
                cell_type = line.split()[1][:-4]
            else:
                cell_type = line.split()[0][:-4]
            rangeStart = int(line.split()[3])
            rangeEnd = int(line.split()[4])
            
            if rangeStart == rangeEnd:
                dCellIDs[rangeStart] = [cell_type, 0]
            elif rangeStart < rangeEnd:
                for ind, i in enumerate(range(rangeStart, rangeEnd+1)):
                    dCellIDs[i] = [cell_type, ind]
            else:
                raise AssertionError("rangeEnd:%g is lower than rangeStart:%g!"%(rangeEnd, rangeStart))
     
    # read in cell positions
    fPositions = os.path.join(basePath, nrn_runname, "position.dat")
    dCellPops = {}   
    
    with open(fPositions, "r") as f:
        next(f)  # skip header: "cell, x, y, z, host"
        for line in f:
            cellID = int(line.split()[0])
            if cellID in dCellIDs:
                cell_type = dCellIDs[cellID][0]
                
            pos = [float(line.split()[1]), float(line.split()[2]), float(line.split()[3])]
            if cell_type not in dCellPops:
                dCellPops[cell_type] = []
                dCellPops[cell_type].append(pos)
            else:
                dCellPops[cell_type].append(pos)
    
    ##### add populations to nml file #####  
    
    for cell_type, pop_list in dCellPops.iteritems():
        
        if cell_type in cell_types:
            component = "dummycell"
        else:
            component = "spikeGenPoisson065"
    
        popID = "pop_%s"%cell_type
        pop = neuroml.Population(id=popID, component=component, type="populationList", size=len(pop_list))
        pop.properties.append(neuroml.Property("color", helper_getcolor(cell_type)))
        net.populations.append(pop)      
        
        for i, sublist in enumerate(pop_list):    
            x_pos = sublist[0]; y_pos = sublist[1]; z_pos = sublist[2]            
            inst = neuroml.Instance(id=i)
            pop.instances.append(inst)
            inst.location = neuroml.Location(x=x_pos, y=y_pos, z=z_pos)
            
    return dCellIDs


def generate_hippocampal_net(networkID,
                             nrn_runname,
                             conndata="430",
                             numCores=1,
                             validate=True,
                             randomSeed=12345,
                             temperature="34.0 degC"):
    """creates simplified NeuroML2 network file (.net.nml) based on data saved from NEURON, using the methods above"""
    
    cell_types = ["axoaxonic", "bistratified", "cck", "ivy", "ngf", "olm", "poolosyn", "pvbasket", "sca"]
    synapse_types = ["exp2Synapses", "customGABASynapses"]
  
    ###### Create network doc #####
    
    nml_doc = neuroml.NeuroMLDocument(id=networkID)
    rnd.seed(randomSeed)  
    nml_doc.properties.append(neuroml.Property("Network seed", randomSeed))
    
    nml_doc.includes.append(neuroml.IncludeType(href="dummycell.cell.nml"))
    for synapse in synapse_types:
        nml_doc.includes.append(neuroml.IncludeType(href="../synapses/%s.synapse.nml"%synapse))
    nml_doc.includes.append(neuroml.IncludeType(href="stimulations.nml"))
        
    # Create network
    net = neuroml.Network(id=networkID, type="networkWithTemperature", temperature=temperature)
    net.notes = "Network generated using libNeuroML v%s"%neuroml.__version__
    nml_doc.networks.append(net)    
    
    # Create populations 
    print("Creating populations...")
    dCellIDs = create_populations_simplified(net, cell_types, nrn_runname, randomSeed)    
    
    # Create synapses
    print("Connecting cells...")
    add_synapses(net, cell_types, nrn_runname, dCellIDs)  
        
    #######   Write to file  ######    

    print("Saving to file...")
    nml_file = networkID+'.net.nml'
    writers.NeuroMLWriter.write(nml_doc, nml_file)
    print("Network saved to: %s"%nml_file)
        
    if validate:
        # Validate the NeuroML file   
        neuroml.utils.validate_neuroml2(nml_file)       


if __name__ == "__main__":

    try:
        runName = sys.argv[1]
    except:
        runName = "MiniScale_TestRun"

    scale = helper_getscale(runName)
    networkID = "HippocampalNet_scale%i_simplified"%scale
    generate_hippocampal_net(networkID=networkID,
                             nrn_runname=os.path.join("results", runName),
                             numCores=24*5)
                             
    # don't try to run this! (it's only for OSB visualization)

        


