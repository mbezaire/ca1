
import opencortex.core as oc


def generate(target_cell, 
             pre_cell, 
             duration, 
             num_inputs,
             firing_freq, 
             dt=0.025):
                 
    tgt_cell_file = '../../cells/%s.cell.nml'%target_cell
    
    target_cell_id = '%scell'%target_cell
    
    syn_id = "syn_%s_to_%s"%(pre_cell, target_cell)
    
    reference= "Stim_%s_%s_%s_%sHz"%(pre_cell,target_cell,num_inputs,firing_freq)
    
    nml_doc, network = oc.generate_network(reference, temperature='34degC')
    
    oc.include_neuroml2_cell(nml_doc,tgt_cell_file,target_cell_id, channels_also=False)
    
    oc.include_neuroml2_file(nml_doc,'../../synapses/exp2Synapses.synapse.nml')
    
    pop = oc.add_single_cell_population(network,
                                        'pop_%s'%target_cell,
                                        target_cell_id)
                                        
    poisson_stim = oc.add_poisson_firing_synapse(nml_doc,
                                       id="ps_%s"%syn_id,
                                       average_rate="%s Hz"%firing_freq,
                                       synapse_id=syn_id)
                                        
    oc.add_targeted_inputs_to_population(network, 
                                         "Stim_0",
                                         pop, 
                                         poisson_stim.id, 
                                         segment_group='dendrite_group',
                                         number_per_cell = num_inputs,
                                         all_cells=True)
                                         

    nml_file_name = '%s.net.nml'%network.id
    oc.save_network(nml_doc, nml_file_name, validate=False)

    interesting_seg_ids = [0] # [soma, .. some dends .. , axon]

    to_plot = {'Some_voltages':[]}
    to_save = {'%s_voltages.dat'%target_cell_id:[]}

    for seg_id in interesting_seg_ids:
        to_plot.values()[0].append('%s/0/%s/%s/v'%(pop.id, pop.component,seg_id))
        to_save.values()[0].append('%s/0/%s/%s/v'%(pop.id, pop.component,seg_id))

    oc.generate_lems_simulation(nml_doc, 
                                network, 
                                nml_file_name, 
                                duration, 
                                dt = dt,
                               gen_plots_for_all_v = False,
                               plot_all_segments = False,
                               gen_plots_for_quantities = to_plot,   #  Dict with displays vs lists of quantity paths
                               gen_saves_for_all_v = False,
                               save_all_segments = False,
                               gen_saves_for_quantities = to_save)   #  Dict with file names vs lists of quantity paths)
    
        
if __name__ == "__main__":
    
    olm_cell = 'olm'
    pyr_cell = "poolosyn"
    duration = 300
        
    generate(olm_cell, pyr_cell, duration, num_inputs=100, firing_freq=50)
    generate(pyr_cell, 'ec', duration, num_inputs=400, firing_freq=30)
