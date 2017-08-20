#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Creates a NeuroML2 version of the hippocampal network by Marianne Bezaire using libNeuroML and pyNeuroML
(by loading placement and connectivity saved by the NEURON version)
Authors: András Ecker, Padraig Gleeson, last update: 08.2017
"""

import os
import re
import sys
import random as rnd
# NeuroML specific libraries
import neuroml
import neuroml.writers as writers
from pyneuroml import pynml
from pyneuroml.lems.LEMSSimulation import LEMSSimulation
# helper functions from other scripts
from morphology_helper import helper_morphology, calc_seg_fracalong
from GenerateHippocampalNet_oc import helper_getcolor, helper_getcelltype, get_projdata

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])


def helper_getscale(runName):
    """get scale from saved parameters"""
   
    with open(os.path.join(basePath, runName, "runreceipt.txt")) as f:
        for line in f:
            if "Scale" in line:
                scale = int(re.findall(r'\d+', tmp)[0])
    return scale


def helper_writesynapse_txt(dSyns):
    """helper function to create NeuroML synapses (has to be copied to an nml file...) TODO: automate that"""
    
    exp2Synapses = ''; customGABASynapses = '';

    for projID, props in dSyns.iteritems():
        precell_type = props["precell_type"]; postcell_type = props["postcell_type"]
        synID = "syn_%s_to_%s"%(precell_type, postcell_type)
        
        if "tau_rise_A" not in props:  # single synapse
            syn = '\t<expTwoSynapse id="%s" gbase="%fnS" erev="%fmV" tauDecay="%fms" tauRise="%fms"/>\n\n'%(synID, props["weight"], props["e_rev"], props["tau_decay"], props["tau_rise"])
            exp2Synapses += syn
            
        else:  # boundled synapses
            syn_A = '\t<expTwoSynapse id="%s_A" gbase="%fnS" erev="%fmV" tauDecay="%fms" tauRise="%fms"/>\n'%(synID, props["weight"], props["e_rev_A"], props["tau_decay_A"], props["tau_rise_A"])
            syn_B = '\t<expTwoSynapse id="%s_B" gbase="%fnS" erev="%fmV" tauDecay="%fms" tauRise="%fms"/>\n\n'%(synID, props["weight"]/3.37, props["e_rev_B"], props["tau_decay_B"], props["tau_rise_B"])   # see /3.37 in the original .mod file
            customGABASynapses += (synA + synB)

    # write out files
    fExp2Synapses = open(os.path.join(basePath, "NeuroML2", "synapses", "exp2Synapses.txt"), "w")
    fExp2Synapses.write(exp2Synapses)
    fCustomGABASynapses = open(os.path.join(basePath, "NeuroML2", "synapses", "customGABASynapses.txt"), "w")
    fCustomGABASynapses.write(customGABASynapses)
    
    fExp2Synapses.close()
    fCustomGABASynapses.close()
    print("Synapses written to file!")
    
    
# helper functions (mostly to process config files)
# *************************************************************************************************************
# network specific methods, using libNeuroML and pyNeuroML           


def create_populations(net, cell_types, nrn_runname, randomSeed):
    """
    Reads original data files (mainly position.dat) and creates population of cells
    :param net: neuroml.Network() - to which the populations will be added 
    :param cell_types: list - (just to avoid multiple declaration of cell_types)
    :param nrn_runname: string - name of the directory where the saved data files are stored (celltype.dat, position.dat)
    :param randomSeed: int - seed for random color generation
    :return dCellIDs: dictionary - key: cellID, value: [cell_type, ID in pop_cell_type] (for creating synapses)
    :return dNumCells: dictonary with the number of cells in a given population (for creating output files -> just for "real cells")
    """
    
    # read in cell gids:
    dCellIDs = {}
    fCellIDs = os.path.join(basePath, nrn_runname, "celltype.dat")
    
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
    dCellPops = {} 
    fPositions = os.path.join(basePath, nrn_runname, "position.dat")  
    
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
    
    dNumCells = {}  # for creating displays and output files (see later in the code)
    
    for cell_type, pop_list in dCellPops.iteritems():
        
        if cell_type in cell_types:
            dNumCells[cell_type] = 0
            component = "%scell"%cell_type
        else:
            component = "spikeGenPoisson065"
        # TODO: implement other stimulations ...
    
        popID = "pop_%s"%cell_type
        pop = neuroml.Population(id=popID, component=component, type="populationList", size=len(pop_list))
        pop.properties.append(neuroml.Property("color", helper_getcolor(cell_type)))
        net.populations.append(pop)      
        
        for i, sublist in enumerate(pop_list):    
            x_pos = sublist[0]; y_pos = sublist[1]; z_pos = sublist[2]            
            inst = neuroml.Instance(id=i)
            pop.instances.append(inst)
            inst.location = neuroml.Location(x=x_pos, y=y_pos, z=z_pos)
            
            if cell_type in cell_types:
                dNumCells[cell_type] += 1 
            
    return dCellIDs, dNumCells


def add_synapses(net, cell_types, nrn_runname, dCellIDs, write_synapse_file=False):
    """
    Reads data files: conndata_x.dat (used to setup), connections.dat (saved after run) and synlist.dat (created by launch_synapse_printer.hoc)
    creates synapse files (only .txt files TODO: automate to make .nml-files)
    calculates the place of synapses and connects the cells
    :param net: neuroml.Network() - to which the projections will be added
    :param cell_types: list - (just to avoid multiple declaration of cell_types)
    :param nrn_runname: string - name of the directory where the saved data files are stored (synlist.dat, connections.dat)
    :param dCellIDs: dictionary created by create_populations, which stroes the gIDs
    """
    
    # automatically get some run specific info...
    with open(os.path.join(basePath, nrn_runname, "runreceipt.txt")) as f:
        for line in f:
            if "NumProcessors" in line:
                numCores = int(re.findall(r'\d+', line)[0])
            elif "ConnData" in line:
                connData = int(re.findall(r'\d+', line)[0])
            elif "SynData" in line:
                synData = int(re.findall(r'\d+', line)[0])     
    
    dSyns = get_projdata(connData, synData)  # read parameters from config files
    
    if write_synapse_file:
        helper_writesynapse_txt(dSyns)
    
    # read in synapse IDs by destinations (on postsyn morphology)
    dSynapseIDs = {}
    fSynapses = os.path.join(basePath, nrn_runname, "synlist.dat")  # created by launch_synapse_printer.hoc!    
    
    with open(fSynapses, "r") as f:
        for line in f:            
            precell_type = helper_getcelltype(line.split()[1])
            postcell_type = helper_getcelltype(line.split()[0])
            id_ = "proj_%spop_to_%spop"%(precell_type, postcell_type)  # keys in dSyns    
            if id_ in dSyns:  # only handle synapse if it's used (based on spec. conndata and syndata)
                synID = "syn_%s_to_%s_%i"%(precell_type, postcell_type, int(line.split()[2]))
            
                tmp = line.split()[3]  # is like: cell_type[0].foo[x]
                postSegID = tmp[tmp.rfind('.')+1:tmp.rfind('[')] + '_' + tmp[tmp.rfind('[')+1:tmp.rfind(']')]  # converts it to: foo_x (used by .cell.nml files)
                dSynapseIDs[synID] = postSegID         
   
    # read in connections
    dProjections = {}    
    for core in range(0, numCores):  
        # since subconns files are separated in the results accross cores (SimTracker could merge those files)
        fConnections = os.path.join(basePath, nrn_runname, "subconns_%i.dat"%core)
             
        with open(fConnections, "r") as f:
            # next(file)  # skip header: "source, target, synapse" <- only if useing connections.dat, created by SimTracker
            for line in f:            
                precellID = int(line.split()[0]); precell_type = dCellIDs[precellID][0]; precellIDPop = dCellIDs[precellID][1]
                postcellID = int(line.split()[1]); postcell_type = dCellIDs[postcellID][0]; postcellIDPop = dCellIDs[postcellID][1]
                synapseID = int(line.split()[2]);
                postSegID = dSynapseIDs["syn_%s_to_%s_%i"%(precell_type, postcell_type, synapseID)]
                
                connection = [precellIDPop, postcellIDPop, postSegID]
                projID = "proj_%spop_to_%spop"%(precell_type, postcell_type)
                
                if projID not in dProjections:
                    dProjections[projID] = []
                    dProjections[projID].append(connection)
                else:
                    dProjections[projID].append(connection)
    
    # load cell morphologies (for fractionAlong calculation for neuroml.Connections) - see morphology_helper.py
    dMorphs = {}
    for cell_type in cell_types:
        dMorphs[cell_type] = helper_morphology("../cells/%s.cell.nml"%cell_type) # will be a dictionary of dictionaries dMorphs[cell_type][segGroupID] = with "segments", "lengths", "distances"
               
                
    #####  add projections and connections to .nml file ##### 
    
    for projID, connection_list in dProjections.iteritems():
    
        precell_type = projID.split('_')[1][:-3]
        postcell_type = projID.split('_')[-1][:-3]
        
        if precell_type != "ngf":  # ngf cells are useing the boundled GABA_A, GABA_B syapse (ExpGABAab.mod)...
            proj = neuroml.Projection(id=projID,
                                      presynaptic_population="pop_%s"%precell_type,
                                      postsynaptic_population="pop_%s"%postcell_type,
                                      synapse="syn_%s_to_%s"%(precell_type, postcell_type))
    
            for i, sublist in enumerate(connection_list):
            
                precellID = sublist[0]; postcellID = sublist[1]; postSegmentGroupID = sublist[2]
                if precell_type not in ["ca3", "ec"]:
                    presynapticComp = "%scell"%precell_type
                    preSegID, preFracAlong = calc_seg_fracalong(dMorphs[precell_type], "soma_0", 0.5)  # see morphology_helper.py           
                else:
                    presynapticComp = "spikeGenPoisson065"  # TODO: implement other stimulations ...
                    preSegID = 0; preFracAlong = 0.5
                    
                postSegID, postFracAlong = calc_seg_fracalong(dMorphs[postcell_type], postSegmentGroupID, 0.5)  # see morphology_helper.py
            
                conn = neuroml.ConnectionWD(id=i,
                                            pre_cell_id="../pop_%s/%g/%s"%(precell_type, precellID, presynapticComp),
                                            pre_segment_id=preSegID,
                                            pre_fraction_along=preFracAlong,
                                            post_cell_id="../pop_%s/%g/%scell"%(postcell_type, postcellID, postcell_type),
                                            post_segment_id=postSegID,
                                            post_fraction_along=postFracAlong,
                                            weight=1,  # synaptic weights are specified at the synapse component level and are not scaled in the network
                                            delay="3ms")
                proj.connection_wds.append(conn)
                
            net.projections.append(proj)
            
        else:
            for sType in ['A', 'B']:
                proj = neuroml.Projection(id="%s_%s"%(projID, sType), 
                                          presynaptic_population="pop_%s"%precell_type,
                                          postsynaptic_population="pop_%s"%postcell_type,
                                          synapse="syn_%s_to_%s_%s"%(precell_type, postcell_type, sType))
                                          
                for i, sublist in enumerate(connection_list):
            
                    precellID = sublist[0]; postcellID = sublist[1]; postSegmentGroupID = sublist[2]
                    presynapticComp = "ngfcell"
                    preSegID, preFracAlong = calc_seg_fracalong(dMorphs["ngf"], "soma_0", 0.5)  # see morphology_helper.               
                    postSegID, postFracAlong = calc_seg_fracalong(dMorphs[postcell_type], postSegmentGroupID, 0.5)  # see morphology_helper.py
            
                    conn = neuroml.ConnectionWD(id=i,
                                                pre_cell_id="../pop_ngf/%g/%s"%(precellID, presynapticComp),
                                                pre_segment_id=preSegID,
                                                pre_fraction_along=preFracAlong,
                                                post_cell_id="../pop_%s/%g/%scell"%(postcell_type, postcellID, postcell_type),
                                                post_segment_id=postSegID,
                                                post_fraction_along=postFracAlong,
                                                weight=1,  # synaptic weights are specified at the synapse component level and are not scaled in the network
                                                delay="3ms")
                    proj.connection_wds.append(conn)
                                          
                net.projections.append(proj)

# ***************************************************************************************************************************************************

                
def generate_hippocampal_net(networkID,
                             nrn_runname,
                             validate=True,
                             randomSeed=12345,
                             generate_LEMS_simulation=False,
                             duration=100,
                             dt=0.01,
                             temperature="34.0 degC"):
    """creates NeuroML2 network file (.net.nml) based on data saved from NEURON, using the methods above"""
    
    cell_types = ["axoaxonic", "bistratified", "cck", "ivy", "ngf", "olm", "poolosyn", "pvbasket", "sca"]
    synapse_types = ["exp2Synapses", "customGABASynapses"]

  
    ###### Create network doc #####
    
    nml_doc = neuroml.NeuroMLDocument(id=networkID)
    rnd.seed(randomSeed)  
    nml_doc.properties.append(neuroml.Property("Network seed", randomSeed))
    
    for cell in cell_types:
        nml_doc.includes.append(neuroml.IncludeType(href="../cells/%s.cell.nml"%cell))
    for synapse in synapse_types:
        nml_doc.includes.append(neuroml.IncludeType(href="../synapses/%s.synapse.nml"%synapse))
    nml_doc.includes.append(neuroml.IncludeType(href="stimulations.nml"))
        
    # Create network
    net = neuroml.Network(id=networkID, type="networkWithTemperature", temperature=temperature)
    net.notes = "Network generated using libNeuroML v%s"%neuroml.__version__
    nml_doc.networks.append(net)
   
    # Create populations 
    print("Creating populations...")
    dCellIDs, dNumCells = create_populations(net, cell_types, nrn_runname, randomSeed)    
    
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
        
    if generate_LEMS_simulation:
        
        # Create a LEMSSimulation to manage creation of LEMS file
        ls = LEMSSimulation('Sim_'+networkID, duration, dt)
        
        # Point to network as target of simulation
        ls.assign_simulation_target(net.id)
        
        # Incude generated/existing NeuroML2 files
        channel_types = ['CavL', 'CavN', 'HCN', 'HCNolm', 'HCNp', 'KCaS', 'Kdrfast', 'Kdrfastngf', 'Kdrp', 'Kdrslow', 'KvA', 'KvAdistp', 'KvAngf', 'KvAolm', 'KvAproxp', 'KvCaB', 'KvGroup', 'Nav', 'Navaxonp', 'Navbis', 'Navcck', 'Navngf', 'Navp', 'leak_chan']
        
        for channel in channel_types:
            ls.include_neuroml2_file("../channels/%s.channel.nml"%channel, include_included=False)
        ls.include_neuroml2_file("../channels/Capool.nml", include_included=False)
        for cell in cell_types:
            ls.include_neuroml2_file("../cells/%s.cell.nml"%cell, include_included=False)
        for synapse in synapse_types:
            ls.include_neuroml2_file("../synapses/%s.synapse.nml"%synapse, include_included=False)
        ls.include_neuroml2_file("stimulations.nml", include_included=False)
        ls.include_neuroml2_file(nml_file, include_included=False)
        
        ###### Specify Display and output files #####
        
        max_traces = 9  # the 10th color in NEURON is white ...
        
        for cell_type, numCells in dNumCells.iteritems():
            PC = False
            if numCells > 0:
                of = "of_%s"%cell_type
                ls.create_output_file(of, "%s.v.dat"%cell_type)
                if cell_type == 'poolosyn' or cell_type == 'cutsuridis':  # TODO: ensure that only one of them is used for modelling pyramidal cells (in a given simulation)
                    PC = True
                    ls.create_event_output_file("spikes_PC", "PC.spikes.dat")
                    ls.create_display("disp_PC", "Voltages Pyramidal cells", "-80", "50")
                
                cell_id = "%scell"%cell_type
                pop_id = "pop_%s"%cell_type
                for i in range(numCells):
                    quantity = "%s/%i/%s/v"%(pop_id, i, cell_id)
                    ls.add_column_to_output_file(of, "v_%i"%i, quantity)
                    if PC:
                        ls.add_selection_to_event_output_file("spikes_PC", i, select='%s/%i/%s'%(pop_id, i, cell_id), event_port='spike')
                        if i < max_traces:
                            ls.add_line_to_display("disp_PC", "PC %i: V[mV]"%i, quantity, "1mV", pynml.get_next_hex_color()) 
            
        # Save to LEMS file
        print("Writing LEMS file...")
        lems_file_name = ls.save_to_file()
        
    else:
        
        ls = None
        lems_file_name = ''
        print("-----------------------------------")
           
                
    return ls, lems_file_name
    

# ***************************************************************************************************************************************************


if __name__ == "__main__":
    
    try:
        runName = sys.argv[1]        
    except:
        runName = "MiniScale_TestRun"        
    try:
        run_simulation = sys.argv[2]
    except:
        run_simulation = False
    
    scale = helper_getscale(runName)
    networkID = "HippocampalNet_scale%i"%scale
    ls, lems_file_name = generate_hippocampal_net(networkID=networkID,
                                                  nrn_runname=os.path.join("results", runName),  # could be changed to NSG folder too
                                                  generate_LEMS_simulation=True)
                                                  
    if ls and run_simulation:
        # run with jNeuroML_NEURON
        print("*** Loading LEMS file: %s and running with jNeuroML_NEURON ***"%(lems_file_name))
        sim = pynml.run_lems_with_jneuroml_neuron(lems_file_name, nogui=True)
        
        
    
