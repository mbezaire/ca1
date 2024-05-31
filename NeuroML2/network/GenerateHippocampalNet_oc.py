#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Creates a NeuroML2 version of the hippocampal network by Marianne Bezaire using opencortex
(by reproducing the cell placement and the connectivity)
Authors: András Ecker, Padraig Gleeson, last update: 11.2017
"""

import os
import re
import sys
import warnings
import numpy as np
# NeuroML specific libraries
import neuroml
from pyneuroml import pynml
import opencortex.core as oc
import opencortex.build as oc_build

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])


def helper_getcolor(cell_type):  # just to be callable from other scripts... 
    """consistent coloring with Bezaire et al. 2016"""    
    dCols = {"axoaxonic":"1 0 0", "bistratified":"0.62745098 0.32156863 0.17647059",
             "cck":"0.85490196 0.64705882 0.1254902", "ivy":"0.6627451 0.6627451 0.6627451",
             "ngf":"0.85490196 0.43921569 0.83921569", "olm":"0.4 0.2 0.6",
             "poolosyn":"0.25490196 0.41176471 0.88235294", "pvbasket":"0.1254902 0.69803922 0.66666667",
             "sca":"1 0.62745098 0.47843137", "ca3":"0.9 0.9 0.9", "ec":"0.75 0.75 0.75"}    
    if cell_type==None:
        return dCols
    return dCols[cell_type]


def helper_getcelltype(cell_name):
    """helper function to process config files"""
    if cell_name == "pyramidalcell":
        return "poolosyn"
    else:
        return cell_name[:-4]


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


def helper_layer(layer):
    """sets boundaries in z direction, based on layer"""
    # slice size: 4000*1000*450 (see distr. of layers (450um) below)
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
        print("Something went wrong! %s, %s %s" %(post_list, dist_crit_from, dist_crit_to))
        

def helper_popsize(pop_size, scale):
    """calculates downscaled population size"""
    if scale != 1:
        if np.floor(pop_size/scale) >= 1.:
            return int(np.floor(pop_size/scale))
        else:
            return 1
    else:
        return pop_size
        
        
def write_popinfo(dPops, scale):
    """writes out size of the populations"""
    
    with open("popsize_scale%s.txt"%scale, "w") as f:
        f.write("popname, number of cells\n")
    
        for cell_type in dPops:
            pop = dPops[cell_type]
            popsize = pop.get_size()
            if cell_type not in ["ca3", "ec"]:
                line = "pop_%s: %s\n"%(cell_type, popsize)
            else:
                line = "(stim) pop_%s: %s\n"%(cell_type, popsize)
            f.write(line)


# helper functions (mostly to process config files)
# *************************************************************************************************************
# network specific methods, using opencortex functions       
       
       
def add_pop(nml_doc, network, scale, cell_type, pop_size, layer, duration=None):
    """adds population using opencortex function and helper functions above"""

    pop_size = helper_popsize(pop_size, scale)
    z_min, z_size = helper_layer(layer)
    
    if cell_type not in ["ca3", "ec"]:  # "real" cells have template
        return oc.add_population_in_rectangular_region(network,
                                                       pop_id="pop_%s"%cell_type, cell_id="%scell"%cell_type,
                                                       size=pop_size,
                                                       x_min=0, y_min=z_min, z_min=0,  # y-z changed on OSB...
                                                       #x_size=4000/np.sqrt(scale), y_size=1000/np.sqrt(scale), z_size=z_size,
                                                       x_size=4000, y_size=z_size, z_size=1000,  # don't scale volume to get better visualization; # y-z changed on OSB...
                                                       color=helper_getcolor(cell_type))
    else:
        spike_gen = oc.add_spike_source_poisson(nml_doc, id="stim_%s"%cell_type,
                                                start="0ms", duration="%fms"%duration, rate="0.65Hz")  # duration used only here
        
        # add outer stimulations outside of the slice... (to get better visualization on OSB)
        if cell_type == "ca3":
            x_min = 0
        elif cell_type == "ec":
            x_min = 3900
        return oc.add_population_in_rectangular_region(network,
                                                       pop_id="pop_%s"%cell_type, cell_id=spike_gen.id,
                                                       size=pop_size,
                                                       x_min=x_min, y_min=500, z_min=450,  # y-z changed on OSB...
                                                       x_size=100, y_size=100, z_size=100,
                                                       color=helper_getcolor(cell_type))


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
    
    if precell_type not in ["ca3", "ec"]:
        pre_seg_group = "soma_group"
    else:
        pre_seg_group = None  # will leave preSegmentId and preFractionAlong in the generated file (which is the way how 'artificial cells' connect to 'real cells')
    
    if len(tau_rise) == 1:  # ngf cells have custom GABA_A,B synapses (defined as 2 diff synapse per one connection) and are handeled differently
        
        syn = oc.add_exp_two_syn(nml_doc,
                                 id="syn_%s_to_%s"%(precell_type, postcell_type),
                                 gbase="%fnS"%weight,
                                 erev="%fmV"%e_rev[0],
                                 tau_rise="%fms"%tau_rise[0],
                                 tau_decay="%fms"%tau_decay[0])
                
        proj = oc.add_targeted_projection(network,
                                          prefix="proj",
                                          presynaptic_population=prepop,
                                          postsynaptic_population=postpop,
                                          targeting_mode="convergent",
                                          synapse_list=[syn.id],
                                          number_conns_per_cell=ncons,
                                          pre_segment_group=pre_seg_group,
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
        
        proj = oc.add_targeted_projection(network,
                                          prefix="proj",
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
                                    
                                      
def generate_hippocampal_net(networkID, scale=100000, duration=100, numData=101, 
                             connData=430, synData=120, addSyns=True, format_="xml",
                             include_external_stims=True):                                 
    """generates hippocampal network, by reproducing the placement, connectivity and scaling of the Bezaire network""" 
  
    if scale > 2000:
        warnings.warn("***** Scaling down more then 2000x alters both population size and the connectivity seriously! *****")
        
    
    cell_types = ["axoaxonic", "bistratified", "cck", "ivy", "ngf", "olm", "poolosyn", "pvbasket", "sca"]

    reference = networkID + ('' if include_external_stims else '_NoInput')
    # init nml document
    nml_doc, network = oc.generate_network(reference, network_seed=12345, temperature="34degC")
    
    # include necessary files
    for cell_type in cell_types:
        path_to_cell = "../cells/%s.cell.nml"%cell_type
        nml_doc.includes.append(neuroml.IncludeType(href=path_to_cell))
        # workaround to handle opencortex's way of including cell templates
        oc_build.cell_ids_vs_nml_docs["%scell"%cell_type] = pynml.read_neuroml2_file(path_to_cell, include_includes=False)   
    
    # create populations
    dCells = get_popdata(numData)
    
    if not include_external_stims:
        
        del dCells['ca3']
        del dCells['ec']
    
    dPops = {}  # dict for storing populations (used for creating projections)
    num_cells = 0
    for cell_type in dCells:
        props = dCells[cell_type]
        pop = add_pop(nml_doc, network, scale,
                      cell_type, pop_size=props["ncells"], layer=props["layer"], duration=duration)
        dPops[cell_type] = pop
        if cell_type in cell_types:
            num_cells += pop.get_size()       
        
    print("Populations created; #cells:%i (without stimulating 'cells')"%num_cells)
    write_popinfo(dPops, scale)
    
    
    # connect populations
    if addSyns:  # easier to visualize on OSB without synapses...
        dSyns = get_projdata(connData, synData)
        num_cons = 0
        for projID in dSyns:
            props = dSyns[projID]
            precell_type = props["precell_type"]; postcell_type = props["postcell_type"]  # just to get populations from pop dictionary 
            if precell_type in dPops and postcell_type in dPops:
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
                                        
        print("Cells connected; #connections:%i "%num_cons)
        
    
    # save to file
    nml_fName = "%s.net.nml%s"%(network.id, ".h5" if format_=="hdf5" else "")
    if format_ == "xml":  # save small networks to nml (and validate)
        oc.save_network(nml_doc, nml_fName,
                        validate=True, format="xml", use_subfolder=False)
        #pynml.run_jneuroml("-validate", nml_fName, "", max_memory="8G", verbose=True)  # increase heap size if necessary!
    else:  # save big networks to h5 file
        oc.save_network(nml_doc, nml_fName,
                        validate=False, format=format_, use_subfolder=False)
                                
    return nml_doc, network, nml_fName, dPops


def generate_lems(nml_doc, network, nml_fName, dPops, duration=100, dt=0.01):
    """generates lems simulation (and specifies savings - spikes + 5 random traces for pops)"""
    
    # dictionary to specify saving (voltage traces)
    mt_ = 5; ms_PC = 1500  # max traces to save, max PCs for spike saving (to spare memory on NSG)
    save_traces= {}; spike_save_pops = []; save_PCspikes = {}      
    for cell_type in dPops:
        pop = dPops[cell_type]
        if cell_type not in ["ca3", "ec"]:
            # save traces
            f_ = "Sim_%s.%s.v.dat"%(nml_doc.id, pop.component)
            save_traces[f_] = []            
            max_traces = mt_ if pop.get_size() >= mt_ else pop.get_size()
            for i in range(0, max_traces):
                quantity = "%s/%i/%s/v"%(pop.id, i, pop.component)
                save_traces[f_].append(quantity)
            
            # save spikes   
            if cell_type != "poolosyn":
                spike_save_pops.append(pop.id)
            else:
                s_ = "Sim_%s.%s.spikes"%(nml_doc.id, pop.component)
                save_PCspikes[s_] = []
                max_spikes = ms_PC if pop.get_size() >= ms_PC else pop.get_size()
                for i in range(0, max_spikes):
                    save_PCspikes[s_].append("%s/%i/%s"%(pop.id, i, pop.component))
                
               
    lems_fName = oc.generate_lems_simulation(nml_doc, network, nml_fName,
                                             duration=duration, dt=dt,
                                             include_extra_lems_files=["PyNN.xml"],  # to include SpikeSourcePoisson
                                             gen_plots_for_all_v=False,
                                             gen_saves_for_all_v=False,                            
                                             gen_saves_for_quantities=save_traces,  # save a few traces for every population
                                             gen_spike_saves_for_all_somas=False,  # don't save ca3, ec spikes (just because they take memory)
                                             gen_spike_saves_for_cells=save_PCspikes,  # save only "some" PC spikes
                                             gen_spike_saves_for_only_populations=spike_save_pops,  # save spikes for other populations                               
                                             lems_file_name="LEMS_%s%s.xml"%(network.id, "_h5" if ".h5" in nml_fName else ""),
                                             lems_file_generate_seed=12345,
                                             simulation_seed=12345)
                                             
    return lems_fName
  

def generate_instance(scale, duration, format_, run_simulation, simulator, generate_LEMS = True, include_external_stims=True):
    """helper function to make automated testing easier"""

    networkID = "HippocampalNet_scale%i_oc"%scale
    
    # generate network
    nml_doc, network, nml_fName, dPops = generate_hippocampal_net(networkID=networkID,
                                                                    scale=scale,
                                                                    duration=duration,
                                                                    format_=format_,
                                                                    include_external_stims=include_external_stims)
    # generate LEMS simulation                                                
    if generate_LEMS:
        lems_fName = generate_lems(nml_doc, network, nml_fName, dPops, duration=duration)
    else:
        lems_fName = None


    if lems_fName and run_simulation:
        if simulator == "NEURON":
            oc.simulate_network(lems_fName, simulator="jNeuroML_%s"%simulator,
                                max_memory="5G")
        elif simulator == "NetPyNE":
            import multiprocessing as mp
            oc.simulate_network(lems_fName, simulator="jNeuroML_%s"%simulator,
                                max_memory="5G", num_processors=mp.cpu_count())
        else:
            raise Exception("simulator:%s is not yet implemented"%simulator)


if __name__ == "__main__":

    if len(sys.argv)==2 and sys.argv[1] == "-test":
        
        generate_instance(100000, 500, "xml", False, None)
        generate_instance(100000, 500, "xml", False, None, include_external_stims=False)
        generate_instance(10000, 100, "hdf5", False, None)
        generate_instance(10000, 100, "hdf5", False, None, include_external_stims=False)
        generate_instance(1000, 100, "hdf5", False, None)
        generate_instance(1000, 100, "hdf5", False, None, include_external_stims=False)

    else:
        try:
            scale = int(sys.argv[1])       
        except:
            scale = 100000
        format_ = "hdf5" if scale < 2000 else "xml"   
        
        try:
            run_simulation = sys.argv[2]    
        except:
            run_simulation = False
        try:
            simulator = sys.argv[3]
        except:
            simulator = "NEURON"

        duration = 2000  # ms
        
        generate_instance(scale, duration, format_, run_simulation, simulator)



