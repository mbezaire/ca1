#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Creates a NeuroML2 version of the hippocampal network by Marianne Bezaire using opencortex
(by reproducing the cell placement and the connectivity)
Authors: András Ecker, Padraig Gleeson, last update: 08.2017
"""

import os
import re
import sys
import warnings
import numpy as np
import random as rnd
# NeuroML specific libraries
import neuroml
from pyneuroml import pynml
import opencortex.core as oc
import opencortex.build as oc_build

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])


def get_popdata(numData):
    """reads in cell numbers from config file"""
    
    dCells = {}   
    fName = os.path.join(basePath, "datasets", "cellnumbers_%i.dat"%numData)
    with open(fName) as f_:
        next(f_)  # skip header: "11"
        for line in f_:
            dCells[helper_getcelltype(line.split()[0])] = {"ncells":int(float(line.split()[2])),
                                                           "layer":int(float(line.split()[3]))}
                
    print("Cell numbers read from config. file!")
    return dCells


def get_projdata(connData, synData):
    """reads in connection specific data from config files"""
    
    dSyns = {}
    fName = os.path.join(basePath, "datasets", "conndata_%i.dat"%connData)
    with open(fName) as f_:
        next(f_)  # skip header: "99"
        for line in f_:
            precell_type = helper_getcelltype(line.split()[0])
            postcell_type = helper_getcelltype(line.split()[1])
            weight = float(line.split()[2])*1000.  # *1000 uS->nS conversion
            ncons = int(float(line.split()[3]))
            nsyns = int(float(line.split()[4]))
            if weight and ncons and nsyns:  # check if weight, nconns and nsyns are not 0
                projID = "proj_%spop_to_%spop"%(precell_type, postcell_type)
                dSyns[projID] = {"precell_type":precell_type,
                                 "postcell_type":postcell_type,
                                 "weight":weight,
                                 "ncons":ncons,
                                 "nsyns":nsyns}  # dict will be further extended
                                 
    fName = os.path.join(basePath, "datasets", "syndata_%i.dat"%synData)
    with open(fName) as f_:
        next(f_)  # skip header: "97"
        for line in f_:
            postcell_type = helper_getcelltype(line.split()[0])
            precell_type = helper_getcelltype(line.split()[1])
            projID = "proj_%spop_to_%spop"%(precell_type, postcell_type)
            if projID in dSyns:  # check if weight isn't set to zero from conndata_*.dat               
                post_list = line.split()[3]  # post list (as specified in the NEURON cell templates)
                dist_crit_from = line.split()[4]; dist_crit_to = line.split()[5]
                dSyns[projID]["post_seg_group"] = helper_getpostseggroup(post_list, dist_crit_from, dist_crit_to)
                if line.split()[2] != "ExpGABAab":
                    dSyns[projID]["tau_rise"] = float(line.split()[6])  # scaling left blank - so it's [6] not [7]
                    dSyns[projID]["tau_decay"] = float(line.split()[7])
                    dSyns[projID]["e_rev"] = float(line.split()[8])
                else:  # ngf cells have different synapses...
                    dSyns[projID]["tau_rise_A"] = float(line.split()[6])  # scaling left blank - so it's [6] not [7]
                    dSyns[projID]["tau_decay_A"] = float(line.split()[7])
                    dSyns[projID]["e_rev_A"] = float(line.split()[8])
                    dSyns[projID]["tau_rise_B"] = float(line.split()[9])
                    dSyns[projID]["tau_decay_B"] = float(line.split()[10])
                    dSyns[projID]["e_rev_B"] = float(line.split()[11])
                    
                                  
    return dSyns


def helper_getnextcolor(randomSeed):
    """generates random color (used to visualize diff. pops on OSB)"""       
    rnd.seed(randomSeed)   
    return "%g %g %g"%(rnd.random(), rnd.random(), rnd.random())


def helper_getcelltype(cell_name):
    """helper function to process config files"""
    if cell_name == "pyramidalcell":
        return "poolosyn"
    else:
        return cell_name[:-4]


def helper_layer(layer):
    """sets boundaries in z direction, based on layer"""
    # slice size: 4000*1000*450 (see distr. of layers (450um) below)
    # Note: scaling alters only x and y size and keeps z inact! (as in the original model)
    if layer == 0:  # oriens
        z_min = 0; z_size = 100
    elif layer == 1:  # pyramidale
        z_min = 100; z_size = 50
    elif layer == 2:  # radiatum
        z_min = 150; z_size = 200
    elif layer == 3:  # lacunosum-moleculare
        z_min = 350; z_size = 100
    return z_min, z_size


def helper_getpostseggroup(post_list, dist_crit_from, dist_crit_to):
    """helper function to process distance criterion and get post. segment group"""
    
    dist_from = int(re.findall(r'\d+', dist_crit_from)[0])
    dist_to = int(re.findall(r'\d+', dist_crit_to)[0])
    
    if dist_from == 1:  # in some cases it's set to -1 (and re. finds 1) -> set to 0
        dist_from = 0
    
    # generate segment_group name (as specified in the NeuroML .cell files)
    if post_list == "soma_list":
        return "soma_group"
    elif post_list == "axon_list":  # for AA cells
        return "axon_group"
    elif post_list in ["dendrite_list", "apical_list"]:
        return "%s_%i_to_%i"%(post_list, dist_from, dist_to)
    elif post_list == "basal_list":  # hacky solution for OLM cell
        return "dendrite_list_%i_to_%i"%(dist_from, dist_to)
    else:
        print "something went wrong!", post_list, dist_crit_from, dist_crit_to
        

def helper_popsize(pop_size, scale):
    """calculates downscaled population size"""
    if scale != 1:
        if np.floor(pop_size/scale) >= 1.:
            return int(np.floor(pop_size/scale))
        else:
            return 1
    else:
        return pop_size


# helper functions (mostly to process config files)
# *************************************************************************************************************
# network specific methods, using opencortex functions       
       
       
def add_pop(network, scale, cell_type, pop_size, layer, color):
    """adds population using opencortex function and helper functions above"""

    pop_size = helper_popsize(pop_size, scale)
    z_min, z_size = helper_layer(layer)
    
    if cell_type not in ["ca3", "ec"]:  # "real" cells have template
        return oc.add_population_in_rectangular_region(network,
                                                       pop_id="pop_%s"%cell_type, cell_id="%scell"%cell_type,
                                                       size=pop_size,
                                                       x_min=0, y_min=0, z_min=z_min,
                                                       x_size=4000/np.sqrt(scale), y_size=1000/np.sqrt(scale), z_size=z_size,
                                                       color=color)
    else:
        return oc.add_population_in_rectangular_region(network,
                                                       pop_id="pop_%s"%cell_type, cell_id="spikeGenPoisson065",
                                                       size=pop_size,
                                                       x_min=0, y_min=0, z_min=z_min,
                                                       x_size=4000/np.sqrt(scale), y_size=1000/np.sqrt(scale), z_size=z_size,
                                                       color=color)


def add_proj(nml_doc, network, projID,
             prepop, postpop,
             tau_rise, tau_decay, e_rev,
             weight, ncons, nsyns, post_seg_group):
    """adds targeted projection using opencortex function"""
    
    precell_type = re.split(r'\_', prepop.id)[1]
    postcell_type = re.split(r'\_', postpop.id)[1]
    projID_loc = "proj_%spop_to_%spop"%(precell_type, postcell_type)     
    # sanity check for redundant names...
    assert projID == projID_loc 
    
    if len(tau_rise) == 1:  # ngf cells have custom GABA_A,B synapses (defined as 2 diff synapse per one connection) and are handeled differently
        
        syn = oc.add_exp_two_syn(nml_doc,
                                 id="syn_%s_to_%s"%(precell_type, postcell_type),
                                 gbase="%fnS"%weight,
                                 erev="%fmV"%e_rev[0],
                                 tau_rise="%fms"%tau_rise[0],
                                 tau_decay="%fms"%tau_decay[0])
        
        # Note: Opencortex extends the id of the given projection        
        proj = oc.add_targeted_projection(nml_doc, network,
                                          prefix=projID,
                                          presynaptic_population=prepop,
                                          postsynaptic_population=postpop,
                                          targeting_mode="convergent",
                                          synapse_list=[syn.id],
                                          number_conns_per_cell=ncons,
                                          pre_segment_group="soma_group",
                                          post_segment_group=post_seg_group,
                                          delays_dict={syn.id:3},
                                          weights_dict={syn.id:nsyns})  # multiple synapses per single connection are replaced by scaled up synaptic weight (for 1 connection)
                                          
    else:  # boundled GABA_A GABA_B synapse
    
        syn_A = oc.add_exp_two_syn(nml_doc,
                                   id="syn_%s_to_%s_A"%(precell_type, postcell_type),
                                   gbase="%fnS"%weight,
                                   erev="%fmV"%e_rev[0],
                                   tau_rise="%fms"%tau_rise[0],
                                   tau_decay="%fms"%tau_decay[0])
        syn_B = oc.add_exp_two_syn(nml_doc,
                                   id="syn_%s_to_%s_B"%(precell_type, postcell_type),
                                   gbase="%fnS"%(weight/3.37),  # GABA_B is weaker (see original .mod file)
                                   erev="%fmV"%e_rev[1],
                                   tau_rise="%fms"%tau_rise[1],
                                   tau_decay="%fms"%tau_decay[1])
        
        # Note: Opencortex extends the id of the given projection
        proj = oc.add_targeted_projection(nml_doc, network,
                                          prefix=projID,
                                          presynaptic_population=prepop,
                                          postsynaptic_population=postpop,
                                          targeting_mode="convergent",
                                          synapse_list=[syn_A.id, syn_B.id],
                                          number_conns_per_cell=ncons,
                                          pre_segment_group="soma_group",
                                          post_segment_group=post_seg_group,
                                          delays_dict={syn_A.id:3, syn_B.id:3},
                                          weights_dict={syn_A.id:nsyns, syn_B.id:nsyns})  # multiple synapses per single connection are replaced by scaled up synaptic weight (for 1 connection)
                                          
    return proj


def add_stim(nml_doc, network, projID,
             prepop_name, postpop,
             tau_rise, tau_decay, e_rev,
             weight, ncons, nsyns, post_seg_group):
    """adds input population with poisson firing rate using opencortex functions"""
    
    assert prepop_name in ["ca3", "ec"], "prepop name has to be 'ca3' or 'ec' for the synapse to work"
    postcell_type = re.split(r'\_', postpop.id)[1]
    projID_loc = "proj_%spop_to_%spop"%(prepop_name, postcell_type) 
    # sanity check for redundant names...
    assert projID == projID_loc

    syn = oc.add_exp_two_syn(nml_doc,
                             id="syn_%s_to_%s"%(prepop_name, postcell_type),
                             gbase="%fnS"%(weight*nsyns),  # multiplied by nsyns here, instead of scaling afterwards
                             erev="%fmV"%e_rev[0],
                             tau_rise="%fms"%tau_rise[0],
                             tau_decay="%fms"%tau_decay[0])
    
    pf_syn = oc.add_poisson_firing_synapse(nml_doc,          
                                           id="pop_%s_to_%spop"%(prepop_name, postcell_type),
                                           average_rate="0.65 Hz",
                                           synapse_id="syn_%s_to_%s"%(prepop_name, postcell_type))
    
    # Note: Opencortex extends the id of the given projection                                
    pf_proj = oc.add_targeted_inputs_to_population(network,
                                                   id=projID,
                                                   population=postpop,
                                                   input_comp_id=pf_syn.id,
                                                   segment_group=post_seg_group,
                                                   number_per_cell=ncons,  
                                                   all_cells=True)
                                                   
    return pf_proj
                                    
                                      
def generate_hippocampal_net(networkID, scale=1000, numData=101, connData=430, synData=120,
                             generate_LEMS=True, duration=100, dt=0.01):
    """generates hippocampal network, by reproducing the placement, connectivity and scaling of the Bezaire network""" 
  
    if scale >= 1000:
        warnings.warn("\n***** Scaling down more then 1000x alters population size, slice volume and the connectivity seriously! *****\n")
    
    cell_types = ["axoaxonic", "bistratified", "cck", "ivy", "ngf", "olm", "poolosyn", "pvbasket", "sca"]
    
    # init nml document
    nml_doc, network = oc.generate_network(networkID, network_seed=12345, temperature="34degC")
    
    # include necessary files
    for cell_type in cell_types:
        path_to_cell = "../cells/%s.cell.nml"%cell_type
        nml_doc.includes.append(neuroml.IncludeType(href=path_to_cell))
        # workaround to handle opencortex's way of including cell templates
        oc_build.cell_ids_vs_nml_docs["%scell"%cell_type] = pynml.read_neuroml2_file(path_to_cell, include_includes=False)   
    
    # create populations
    dCells = get_popdata(numData)
    dPops = {}  # dict for storing populations (used for creating projections)
    num_cells = 0
    for cell_type, props in dCells.iteritems():
        if cell_type in cell_types:
            pop = add_pop(network, scale, cell_type, pop_size=props["ncells"], layer=props["layer"],
                          color=helper_getnextcolor(num_cells))
            dPops[cell_type] = pop
            num_cells += pop.get_size()       
        
    print("Populations created; #cells:%i (without stimulating 'cells')"%num_cells)
    
    
    # connect populations
    dSyns = get_projdata(connData, synData)
    num_cons = 0
    for projID, props in dSyns.iteritems():
        precell_type = props["precell_type"]; postcell_type = props["postcell_type"]  # just to get populations from pop dictionary        
        if precell_type in cell_types:
            prepop = dPops[precell_type]; postpop = dPops[postcell_type]
            if "tau_rise_A" not in props:  # single synapse
                proj = add_proj(nml_doc, network,
                                projID, prepop, postpop,
                                tau_rise=[props["tau_rise"]], tau_decay=[props["tau_decay"]], e_rev=[props["e_rev"]],
                                weight=props["weight"], ncons=props["ncons"], nsyns=props["nsyns"],
                                post_seg_group=props["post_seg_group"])
            else:  # boundled synapse
                proj = add_proj(nml_doc, network,
                                projID, prepop, postpop,
                                tau_rise=[props["tau_rise_A"], props["tau_rise_B"]],
                                tau_decay=[props["tau_decay_A"], props["tau_decay_B"]],
                                e_rev=[props["e_rev_A"], props["e_rev_B"]],
                                weight=props["weight"], ncons=props["ncons"], nsyns=props["nsyns"],
                                post_seg_group=props["post_seg_group"])
            num_cons += len(proj[0].connection_wds)
        else:  # outer stimulation
            postpop = dPops[postcell_type]
            proj = add_stim(nml_doc, network,
                            projID, prepop_name=precell_type, postpop=postpop,
                            tau_rise=[props["tau_rise"]], tau_decay=[props["tau_decay"]], e_rev=[props["e_rev"]],
                            weight=props["weight"], ncons=props["ncons"], nsyns=props["nsyns"],
                            post_seg_group=props["post_seg_group"])
                                    
    print("Cells connected; #connections:%i (without stimulating connections)"%num_cons)
    
    
    # save to file
    nml_fName = "%s.net.nml"%network.id
    oc.save_network(nml_doc, nml_fName,
                    validate=True, format="xml", use_subfolder=False)


    if generate_LEMS:
    
        # dictionary to specify saving (voltage traces)
        max_traces = 5
        save_traces= {}        
        for pop_name, pop in dPops.iteritems():   
            f_ = "Sim_%s.%s.v.dat"%(nml_doc.id, pop.component)
            save_traces[f_] = []
            if pop.get_size() < max_traces:  # check if there are enough cells in pop to save
                max_traces = pop.get_size()
            for i in range(0, max_traces):
                quantity = "%s/%i/%s/v"%(pop.id, i, pop.component)
                save_traces[f_].append(quantity)
        
        lems_fName = oc.generate_lems_simulation(nml_doc, network, nml_fName,
                                                 duration=duration, dt=dt,
                                                 gen_plots_for_all_v=False,
                                                 gen_saves_for_quantities=save_traces,
                                                 gen_spike_saves_for_all_somas=True,
                                                 lems_file_name="LEMS_%s.xml"%network.id,
                                                 simulation_seed=12345)
                                                 
    else:
        lems_fName = None
        
    return lems_fName


if __name__ == "__main__":

    try:
        scale = float(sys.argv[1])
        run_simulation = sys.argv[2]
    except:
        scale = 100000  
        run_simulation = False
    
    lems_fName = generate_hippocampal_net("HippocampalNet_oc",
                                          scale=scale,
                                          generate_LEMS=True)
    print lems_fName, run_simulation
    if lems_fName and run_simulation:
        import multiprocessing as mp
        oc.simulate_network(lems_fName, simulator="jNeuroML_NetPyNE",
                            max_memory="5G", num_processors=mp.cpu_count())

