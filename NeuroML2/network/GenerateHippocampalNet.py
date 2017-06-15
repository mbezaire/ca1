# -*- coding: utf-8 -*-
""" 
    Creates a NeuroML2 version of the hippocampal network by Marianne Bezaire
    Authors: András Ecker, Padraig Gleeson
"""

import neuroml
import neuroml.writers as writers

from morphology_helper import helper_morphology, calc_seg_fracalong

from pyneuroml import pynml
from pyneuroml.lems.LEMSSimulation import LEMSSimulation

from random import seed


def helper_getnextcolor(randomSeed):
    
    import random as rnd
    
    rnd.seed(randomSeed)
    
    return "%g %g %g"%(rnd.random(), rnd.random(), rnd.random())
    

def create_populations(net, cell_types, nrn_runname, randomSeed):
    '''
    Reads original data files (mainly position.dat) and creates population of cells
    :param net: neuroml.Network() - to which the populations will be added 
    :param cell_types: list - (just to avoid multiple declaration of cell_types)
    :param nrn_runname: string - name of the directory where the saved data files are stored (celltype.dat, position.dat)
    :param randoSeed: int - seed for random color generation
    :return dCellIDs: dictionary - key: cellID, value: [cell_type, ID in pop_cell_type] (for creating synapses)
    :return dNumCells: dictonary with the number of cells in a given population (for creating output files -> just for "real cells")
    '''
    
    # read in cell gids:
    fCellIDs = "../../results/%s/celltype.dat"%nrn_runname
    dCellIDs = {}
    
    with open(fCellIDs) as file:
        next(file)  # skip header: "celltype, techtype, typeIndex, rangeStart, rangeEnd"
        for line in file:
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
    
    file.close()
     
    # read in cell positions
    fPositions = "../../results/%s/position.dat"%nrn_runname
    dCellPops = {}   
    
    with open(fPositions) as file:
        next(file)  # skip header: "cell, x, y, z, host"
        for line in file:
            cellID = int(line.split()[0])
            if cellID in dCellIDs:
                cell_type = dCellIDs[cellID][0]
                
            pos = [float(line.split()[1]), float(line.split()[2]), float(line.split()[3])]
            if cell_type not in dCellPops:
                dCellPops[cell_type] = []
                dCellPops[cell_type].append(pos)
            else:
                dCellPops[cell_type].append(pos)
                    
    file.close()
    
    
    ##### add populations to nml file #####  
    
    dNumCells = {}  # for creating displays and output files (see later in the code)
    
    j = 0  # for increasing random seed in random colour generation
    for cell_type, pop_list in dCellPops.iteritems():
        
        if cell_type in cell_types:
            dNumCells[cell_type] = 0
            component = "%scell"%cell_type
        else:
            component = "spikeGenPoisson"
        # TODO: implement other stimulations ...
    
        popID = "pop_%s"%cell_type
        pop = neuroml.Population(id=popID, component=component, type="populationList", size=len(pop_list))
        pop.properties.append(neuroml.Property("color", helper_getnextcolor(randomSeed+j)))
        net.populations.append(pop)      
        j += 1
        
        for i, sublist in enumerate(pop_list):    
            x_pos = sublist[0]; y_pos = sublist[1]; z_pos = sublist[2]            
            inst = neuroml.Instance(id=i)
            pop.instances.append(inst)
            inst.location = neuroml.Location(x=x_pos, y=y_pos, z=z_pos)
            
            if cell_type in cell_types:
                dNumCells[cell_type] += 1 
            
    return dCellIDs, dNumCells


def helper_pyramidalcell(cell, dNumCells):
    
    if cell != "pyramidalcell":
        return cell[:-4]
    elif cell == "pyramidalcell" and "poolosyn" in dNumCells:
        return "poolosyn"
    else:
        return "cutsuridis"


def add_synapses(net, conndata, nrn_runname, dCellIDs, dNumCells, write_synapse_file=False):
    '''
    Reads original data files: conndata_x.dat, connections.dat and synlist.dat (created by launch_synapse_printer.hoc)
    create synapse files (only .txt files TODO: automate to make .nml-files)
    calculates the place of synapses and connects the cells
    :param net: neuroml.Network() - to which the projections will be added
    :param conndata: string(int) - original connection data file (only for setting the weights of the synapses, other parameters are loaded from other files)
    :param nrn_runname: string - name of the directory where the saved data files are stored (synlist.dat, connections.dat) ! nrn_runname depends on conndata !
    :param dCellIDs - dictionary created by create_populations, which stroes the gid's
    :param dNumCells - dictionary created by create_populations, quick and dirty way to handle pyramidalcell -> [poolosyncell, cutsuridiscell] in conndata_x.dat and synlist.dat
    '''
    
    # read in synaptic weight (if weight is 0 don't create synapses)
    fConndata = "../../datasets/conndata_%s.dat"%conndata
    dSWeights = {}
    
    with open(fConndata) as file:
        next(file)  # skip header/first row: "99"
        for line in file:
            
            # handle pyramidalcell
            preCell = helper_pyramidalcell(line.split()[0], dNumCells)
            postCell = helper_pyramidalcell(line.split()[1], dNumCells)
            weight = float(line.split()[2])*1000  # nS
            
            if weight != 0.:
                id = "%s_to_%s"%(preCell, postCell)
                dSWeights[id] = weight
                
    file.close()
    
    
    # read in synapse types and IDs
    fSynapses = "../../results/%s/synlist.dat"%nrn_runname
    dSynapseIDs = {}
    
    # for automated synapse file generation ...
    # there will be a unique synapse for every poosible connection where the weight is not 0 (not all of them will be used in the network)
    exp2Synapses = ''; customGABASynapses = ''; synapse_types = []
    
    with open(fSynapses) as file:
        for line in file:
            
            # handle pyramidalcell
            preCell = helper_pyramidalcell(line.split()[1], dNumCells)
            postCell = helper_pyramidalcell(line.split()[0], dNumCells)
            tmp = "%s_to_%s"%(preCell, postCell)
            
            if tmp in dSWeights:  # only handle synapse if weight is != 0
                id = "syn_%s_to_%s"%(preCell, postCell)
                synapseID = "%s_%s"%(id, int(line.split()[2]))
                weight = dSWeights[tmp]
            
                tmp = line.split()[3]  # is like: cell_type[0].foo[x]
                postSegID = tmp[tmp.rfind('.')+1:tmp.rfind('[')] + '_' + tmp[tmp.rfind('[')+1:tmp.rfind(']')]  # converts it to: foo_x            
            
                if synapseID not in dSynapseIDs:
                    dSynapseIDs[synapseID] = postSegID
        
                # write out synapses         
                    tauRise = float(line.split()[5]); tauDecay = float(line.split()[6]); erev = float(line.split()[7]);
                    syn = '\t<expTwoSynapse id="%s" gbase="%gnS" erev="%gmV" tauDecay="%gms" tauRise="%gms"/>\n\n'%(id, weight, erev, tauDecay, tauRise)
                    if id not in synapse_types and line.split()[4] != "ExpGABAab":
                        exp2Synapses += syn
                        synapse_types.append(id)
                else:
                    tauRiseB = float(line.split()[5]); tauDecayB = float(line.split()[6]); erevB = float(line.split()[7]);
                    synA = '\t<expTwoSynapse id="%s_A" gbase="%gnS" erev="%gmV" tauDecay="%gms" tauRise="%gms"/>\n'%(id, weight, erev, tauDecay, tauRise)
                    synB = '\t<expTwoSynapse id="%s_B" gbase="%gnS" erev="%gmV" tauDecay="%gms" tauRise="%gms"/>\n\n'%(id, weight/3.37, erevB, tauDecayB, tauRiseB)
                    if id not in synapse_types:
                        customGABASynapses += (synA + synB)
                        synapse_types.append(id)
                
        if write_synapse_file:
            fExp2Synapses = open("../synapses/exp2Synapses.txt", 'w')
            fExp2Synapses.write(exp2Synapses)
            fExp2Synapses.close()
            fCustomGABASynapses = open("../synapses/customGABASynapses.txt", 'w')
            fCustomGABASynapses.write(customGABASynapses)
            fCustomGABASynapses.close()
            
    file.close()
    
    
    # read in connections
    """
    Note: if you run the model (the NEURON one) on multiple processors with CatFlag==0,
    then the connections will be dispersed in one file per processor, named subconns_[processorID].dat.
    SimTracker can then merge the files together, but if you don't use SimTracker and are using multiple processors,
    try setting CatFlag==1 to have NEURON concatenate all the data into one connections.dat file)
    This code was based on test runs wth a single processor, so we are using subconns_0.dat
    """
    fConnections = "../../results/%s/subconns_0.dat"%nrn_runname  # TODO: fix this...(see above in docstring)
    dProjections = {}
    
    with open(fConnections) as file:
        # next(file)  # skip header: "source, target, synapse" <- only if useing connections.dat, created by SimTracker
        for line in file:
            
            preCellID = int(line.split()[0]); preCell_type = dCellIDs[preCellID][0]; preCellIDPop = dCellIDs[preCellID][1]
            postCellID = int(line.split()[1]); postCell_type = dCellIDs[postCellID][0]; postCellIDPop = dCellIDs[postCellID][1]
            synapseID = int(line.split()[2]); postSegID = dSynapseIDs["syn_%s_to_%s_%g"%(preCell_type, postCell_type, synapseID)]
            
            connection = [preCellIDPop, postCellIDPop, postSegID]
            projID = "proj_%spop_to_%spop"%(preCell_type, postCell_type)
            
            if projID not in dProjections:
                dProjections[projID] = []
                dProjections[projID].append(connection)
            else:
                dProjections[projID].append(connection)
    
    file.close()
    
    
    # load cell morphologies (for segment and fractionAlong calculation for neuroml.Connections) - see morphology_helper.py
    cell_types = dNumCells.keys()
    dMorphs = {}
    for cell in cell_types:
        dMorphs[cell] = helper_morphology("../cells/%s.cell.nml"%cell) # will be a dictionary of dictionaries d[cell][segGroupID] = [[segIDs], [lSegs]]
               
                
    #####  add projections and connections to nml file ##### 
    
    for projID, connection_list in dProjections.iteritems():
    
        presynaptic = projID.split('_')[1][:-3]
        postsynaptic = projID.split('_')[-1][:-3]
        
        if presynaptic != "ngf":  # ngf cells are useing the boundled GABA_A, GABA_B syapse (ExpGABAab.mod)...
            proj = neuroml.Projection(id=projID,
                                      presynaptic_population="pop_%s"%presynaptic,
                                      postsynaptic_population="pop_%s"%postsynaptic,
                                      synapse="syn_%s_to_%s"%(presynaptic, postsynaptic))
    
            for i, sublist in enumerate(connection_list):
            
                preCellID = sublist[0]; postCellID = sublist[1]; postSegmentGroupID = sublist[2]
                if presynaptic not in ["ca3", "ec"]:
                    presynapticComp = "%scell"%presynaptic
                    preSegID, preFracAlong = calc_seg_fracalong(dMorphs[presynaptic], "soma_0", 0.5)  # see morphology_helper.               
                else:
                    presynapticComp = "spikeGenPoisson"  # TODO: implement other stimulations ...
                    preSegID = 0; preFracAlong = 0.5
                postSegID, postFracAlong = calc_seg_fracalong(dMorphs[postsynaptic], postSegmentGroupID, 0.5)  # see morphology_helper.py
            
                conn = neuroml.ConnectionWD(id=i,
                                          pre_cell_id="../pop_%s/%g/%s"%(presynaptic, preCellID, presynapticComp),
                                          pre_segment_id=preSegID,
                                          pre_fraction_along=preFracAlong,
                                          post_cell_id="../pop_%s/%g/%scell"%(postsynaptic, postCellID, postsynaptic),
                                          post_segment_id=postSegID,
                                          post_fraction_along=postFracAlong,
                                          weight=1,  # synaptic weights are specified at the synapse component level and are not scaled in the network
                                          delay="3ms")
                proj.connection_wds.append(conn)
                
            net.projections.append(proj)
            
        else:  # TODO: check if only ngf is using ExpGABAab (with other ConnDat, SynData spec.)
            for sType in ['A', 'B']:
                proj = neuroml.Projection(id="%s_%s"%(projID, sType), 
                                          presynaptic_population="pop_%s"%presynaptic,
                                          postsynaptic_population="pop_%s"%postsynaptic,
                                          synapse="syn_%s_to_%s_%s"%(presynaptic, postsynaptic, sType))
                                          
                for i, sublist in enumerate(connection_list):
            
                    preCellID = sublist[0]; postCellID = sublist[1]; postSegmentGroupID = sublist[2]
                    presynapticComp = "ngfcell"
                    preSegID, preFracAlong = calc_seg_fracalong(dMorphs["ngf"], "soma_0", 0.5)  # see morphology_helper.               
                    postSegID, postFracAlong = calc_seg_fracalong(dMorphs[postsynaptic], postSegmentGroupID, 0.5)  # see morphology_helper.py
            
                    conn = neuroml.ConnectionWD(id=i,
                                              pre_cell_id="../pop_ngf/%g/%s"%(preCellID, presynapticComp),
                                              pre_segment_id=preSegID,
                                              pre_fraction_along=preFracAlong,
                                              post_cell_id="../pop_%s/%g/%scell"%(postsynaptic, postCellID, postsynaptic),
                                              post_segment_id=postSegID,
                                              post_fraction_along=postFracAlong,
                                              weight=1,  # synaptic weights are specified at the synapse component level and are not scaled in the network
                                              delay="3ms")
                    proj.connection_wds.append(conn)
                                          
                net.projections.append(proj)


def init_voltage(nml_doc, net, dClamps, dNumCells):
    """
    Initialise the voltage of cells with voltageClamps (-> no need to create new cell_type.cell.nml files...)
    :param nml_doc: neuroml.NeuroMLDocument() - to which the voltage clamps will be added
    :param net: neuroml.Network() - to which the inputs will be added
    :param dClamps: dictionary which contains the initial voltages (this in hard coded...)
    :param dNumCells: - dictionary created by create_populations, which specifies how many inputs will be added
    """
    
    vcDur = 1  # ms
    for cell_type, numCells in dNumCells.iteritems(): 
        
        clamp = dClamps[cell_type]
        vc = neuroml.VoltageClamp(id="vc_%s"%cell_type, delay="0ms", duration="%gms"%vcDur, simple_series_resistance="5e4ohm", target_voltage="%gmV"%clamp)
        nml_doc.voltage_clamps.append(vc)
        
        input_list = neuroml.InputList(id="input_vc_%s"%cell_type, populations="pop_%s"%cell_type, component="vc_%s"%cell_type)
        
        for i in range(0, numCells):
                         
            inp = neuroml.Input(id=i, target="../pop_%s/%g/%scell"%(cell_type, i, cell_type), destination="synapses")
            input_list.input.append(inp)
        
        net.input_lists.append(input_list)
        
  
# ***************************************************************************************************************************************************
  
                
def generate_hippocampal_net(network_id,
                            conndata = "430",
                            nrn_runname = "TestRun",
                            validate = True,
                            randomSeed = 12345,
                            generate_LEMS_simulation = False,
                            duration = 100,
                            dt = 0.01,
                            temperature = "34.0 degC"):
    
    seed(randomSeed)
    
    cell_types = ['axoaxonic', 'bistratified', 'cck', 'cutsuridis', 'ivy', 'ngf', 'olm', 'poolosyn', 'pvbasket', 'sca']
    synapse_types = ['exp2Synapses', 'customGABASynapses']
    
    
    ###### Create network doc #####
    
    nml_doc = neuroml.NeuroMLDocument(id=network_id)
    
    for cell in cell_types:
        nml_doc.includes.append(neuroml.IncludeType(href="../cells/%s.cell.nml"%cell))
    for synapse in synapse_types:
        nml_doc.includes.append(neuroml.IncludeType(href="../synapses/%s.synapse.nml"%synapse))
    nml_doc.includes.append(neuroml.IncludeType(href="stimulations.nml"))
    
    
    # Create network
    net = neuroml.Network(id=network_id, type="networkWithTemperature", temperature=temperature)
    
    from neuroml import __version__
    net.notes = "Network generated using libNeuroML v%s"%__version__
    nml_doc.networks.append(net)
    
    
    # Create populations 
    print("Creating populations...")
    dCellIDs, dNumCells = create_populations(net, cell_types, nrn_runname, randomSeed)
    
    
    # Create synapses
    print("Connecting cells...")
    add_synapses(net, conndata, nrn_runname, dCellIDs, dNumCells, write_synapse_file=False)
    
    
    # initialise voltage
    print("Initialising cell voltage..")
    # TODO: this shouldn't be hard coded ... 
    dClamps = {}; dClamps["axoaxonic"] = -65.0127; dClamps["bistratified"] = -67.0184; dClamps["cck"] = -70.6306; dClamps["ivy"] = -59.9512
    dClamps["ngf"] = -59.9512; dClamps["olm"] = -71.1411; dClamps["poolosyn"] = -62.9601; dClamps["pvbasket"] = -65.0246; dClamps["sca"] = -70.5652
    init_voltage(nml_doc, net, dClamps, dNumCells)
    
        
    #######   Write to file  ######    

    print("Saving to file...")
    nml_file = network_id+'.net.nml'
    writers.NeuroMLWriter.write(nml_doc, nml_file)
    print("Written network file to: "+nml_file)
    
    
    if validate:

        ###### Validate the NeuroML ######    

        from neuroml.utils import validate_neuroml2
        validate_neuroml2(nml_file)
        
        
    if generate_LEMS_simulation:
        
        # Create a LEMSSimulation to manage creation of LEMS file
        ls = LEMSSimulation('Sim_'+network_id, duration, dt)
        
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


def main():
        
    ls, lems_file_name = generate_hippocampal_net(network_id="HippocampalNet",
                                                  nrn_runname = "TestRun",
                                                  validate=True,
                                                  generate_LEMS_simulation=True)
    import sys
    try:
        run_LEMS_simulation = sys.argv[1]
    except:
        run_LEMS_simulation = False
        
    if ls and run_LEMS_simulation:
        # run with jNeuroML_NEURON
        print("*** Loading LEMS file: %s and running with jNeuroML_NEURON ***"%(lems_file_name))
        sim = pynml.run_lems_with_jneuroml_neuron(lems_file_name, nogui=True)



if __name__ == "__main__":
    main()