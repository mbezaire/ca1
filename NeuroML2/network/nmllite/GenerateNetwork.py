from neuromllite import *
from neuromllite.NetworkGenerator import *
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

from neuromllite.sweep.ParameterSweep import ParameterSweep
from neuromllite.sweep.ParameterSweep import NeuroMLliteRunner

colors = helper_getcolor(None)

def generate(cell_numbers, 
             input_num_freqs, 
             duration, 
             dt=0.025, 
             simulation_seed=1234, 
             reference=None):
    
    reference0 = "Net"
    
    net = Network(id=reference0)
    net.temperature = 34 # degC
    
    ca1 = RectangularRegion(id='CA1', x=0,y=0,z=0,width=2000,height=500,depth=1000)
    net.regions.append(ca1)
    
    ext_ca3 = RectangularRegion(id='CA3', x=0,y=550,z=450,width=100,height=100,depth=100)
    net.regions.append(ext_ca3)
    ext_ec = RectangularRegion(id='EC', x=1900,y=550,z=450,width=100,height=100,depth=100)
    net.regions.append(ext_ec)
    
    net.parameters = {}
    
    for cell in cell_numbers.keys():
        reference0 += '_%s%s'%(cell,cell_numbers[cell])

        cell_id = '%scell'%cell
        cell_nmll = Cell(id=cell_id, neuroml2_source_file='../../cells/%s.cell.nml'%cell)
        
        net.cells.append(cell_nmll)
        
        net.parameters['num_%s'%cell] = cell_numbers[cell]
        
        pop = Population(id='pop_%s'%cell, 
                            size='num_%s'%cell, 
                            component=cell_id, 
                            properties={'color':colors[cell]})

        pop.random_layout = RandomLayout(region=ca1.id)

        net.populations.append(pop)
 

    ################################################################################
    ###   Add some inputs
    for input in input_num_freqs:

        num, freq = input_num_freqs[input]
        ssp = Cell(id='%scell'%input, pynn_cell='SpikeSourcePoisson')
        
        net.parameters['rate_%s'%input] = freq

        ssp.parameters = { 'rate':     'rate_%s'%input,
                         'start':      0,
                         'duration':   1e9}
        net.cells.append(ssp)

        pop = Population(id='pop_%s'%input, 
                            size=num, 
                            component=ssp.id, 
                            properties={'color':colors[input]})

        pop.random_layout = RandomLayout(region=ext_ca3.id if input=='ca3' else ext_ec.id)

        net.populations.append(pop)
            
            
                                

    for cell in cell_numbers.keys():
        for input in input_num_freqs:
            
            syn_id = 'syn_%s_to_%s'%(input, cell)
            net.synapses.append(Synapse(id=syn_id, neuroml2_source_file='../../synapses/exp2Synapses.synapse.nml'))
            
            net.projections.append(Projection(id='proj_%s_%s'%(input, cell),
                                      presynaptic='pop_%s'%input, 
                                      postsynaptic='pop_%s'%cell,
                                      synapse=syn_id,
                                      delay=0,
                                      weight=1,
                                      random_connectivity=RandomConnectivity(probability=.5)))
            
    if reference == None: 
        reference = reference0
    net.id = reference 
    net.notes = "A network model: %s"%reference
                                               
    network_filename = '%s.json'%reference         
    
    print(net.to_json())
    if network_filename==None:
        network_filename='%s.json'%net.id
    new_file = net.to_json_file(network_filename)
    

    ################################################################################
    ###   Build Simulation object & save as JSON

    sim = Simulation(id='Sim_%s'%reference,
                     network=new_file,
                     duration=duration,
                     dt=dt,
                     seed=simulation_seed,
                     recordTraces={'all':'*'})

    simulation_filename='%s.json'%sim.id
    sim.to_json_file(simulation_filename)
    
    return sim, net



if __name__ == "__main__":
    
    if '-all' in sys.argv:
        sim, net = generate({'ngf':3}, 
                            {'ec':(5,50)}, 
                            duration=1000, 
                            dt=0.01,
                            reference="TestNet")
                            
        check_to_generate_or_run(sys.argv, sim)
        
        
    elif '-pyr' in sys.argv:
        sim, net = generate({'poolosyn':6}, 
                            {'ec':(200,200)}, 
                            duration=300, 
                            reference="Pyr")
        
    elif '-ping' in sys.argv:
        sim, net = generate({'poolosyn':3, 'pvbasket':3}, 
                            {'ca3':(100,200.0)}, #, 'ec':(100,100)}, 
                            duration=300, 
                            reference="PING")
                            
        check_to_generate_or_run(sys.argv, sim)
    
    elif '-sweep' in sys.argv:
        
        fixed = {'num_ngf':'3', 'duration':500}

        vary = {'rate_ec':[10,20]}
        vary = {'rate_ec':[10,20,30,40,50,60,70]}
        
        simulator='jNeuroML_NetPyNE'
        simulator='jNeuroML_NEURON'
        
        nmllr = NeuroMLliteRunner('Sim_TestNet.json',
                                  simulator=simulator)        

        ps = ParameterSweep(nmllr, 
                            vary, 
                            fixed,
                            num_parallel_runs=16,
                            save_plot_all_to='traces.png',
                            heatmap_all=True,
                            save_heatmap_to='heatmap.png',
                            plot_all=True, 
                            show_plot_already=False)

        report = ps.run()
        ps.print_report()
        
        ps.plotLines('rate_ec','pop_ngf/0/ngfcell/v:mean_spike_frequency',save_figure_to='mean_spike_frequency_ngf.png')
        
        import matplotlib.pyplot as plt

        plt.show()
    else:
        
        #sim, net = generate({'olm':5}, 1000)
        sim, net = generate({'ngf':5, 'sca':5}, {'ec':(5,50)}, duration=1000, dt=0.01)
        
        check_to_generate_or_run(sys.argv, sim)
    