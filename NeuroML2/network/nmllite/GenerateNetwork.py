from neuromllite import *
from neuromllite.NetworkGenerator import *
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)

def generate(cell_numbers, input_num_freqs, duration, dt=0.025, simulation_seed=1234, config='Net'):
    
    reference = "%s"%(config)
    
    net = Network(id=reference)
    net.notes = "A network model: %s"%reference
    net.temperature = 34 # degC
    
    ca1 = RectangularRegion(id='ca1', x=0,y=0,z=0,width=1000,height=100,depth=1000)
    net.regions.append(ca1)
    
    ext = RectangularRegion(id='ext', x=1500,y=0,z=0,width=1000,height=100,depth=1000)
    net.regions.append(ext)
    
    net.parameters = {}
    net.parameters['stim_amp'] = '350pA'
    
    for cell in cell_numbers.keys():
        reference += '_%s%s'%(cell,cell_numbers[cell])

        cell_id = '%scell'%cell
        cell_nmll = Cell(id=cell_id, neuroml2_source_file='../../cells/%s.cell.nml'%cell)
        
        net.cells.append(cell_nmll)
        
        pop = Population(id='pop_%s'%cell, 
                            size=cell_numbers[cell], 
                            component=cell_id, 
                            properties={'color':colors[cell]})

        pop.random_layout = RandomLayout(region=ca1.id)

        net.populations.append(pop)
 
    net.id = reference 

    ################################################################################
    ###   Add some inputs
    for input in input_num_freqs:

        num, freq = input_num_freqs[input]
        ssp = Cell(id='%scell'%input, pynn_cell='SpikeSourcePoisson')

        ssp.parameters = { 'rate':       '%s'%freq,
                         'start':      0,
                         'duration':   1e9}
        net.cells.append(ssp)

        pop = Population(id='pop_%s'%input, 
                            size=num, 
                            component=ssp.id, 
                            properties={'color':colors[input]})

        pop.random_layout = RandomLayout(region=ext.id)

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
        pass
        
    else:
        
        #sim, net = generate({'olm':5}, 1000)
        sim, net = generate({'ngf':5}, {'ec':(5,50)}, 1000)
        
        check_to_generate_or_run(sys.argv, sim)
    