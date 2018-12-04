from neuromllite import *
from neuromllite.NetworkGenerator import *
from neuromllite.utils import create_new_model
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)

def generate(cell_numbers, duration, dt=0.025, simulation_seed=1234, config='Net'):
    
    reference = "%s"%(config)
    
    net = Network(id=reference)
    net.notes = "A network model: %s"%reference
    net.temperature = 34 # degC
    
    r1 = RectangularRegion(id='ca1', x=0,y=0,z=0,width=1000,height=100,depth=1000)
    net.regions.append(r1)
    
    net.parameters = {}
    net.parameters['stim_amp'] = '350pA'
    
    for cell in cell_numbers.keys():
        reference += '_%s%s'%(cell,cell_numbers[cell])

        cell_id = '%scell'%cell
        cell_nmll = Cell(id=cell_id, neuroml2_source_file='../../cells/%s.cell.nml'%cell)
        
        net.cells.append(cell_nmll)
        
        pop = Population(id='pop_%s'%cell_id, 
                            size=cell_numbers[cell], 
                            component=cell_id, 
                            properties={'color':colors[cell]})

        pop.random_layout = RandomLayout(region=r1.id)

        net.populations.append(pop)
 
        ################################################################################
        ###   Add some inputs


        input_source = InputSource(id='iclamp_0', 
                                   neuroml2_input='PulseGenerator', 
                                   parameters={'amplitude':'stim_amp', 'delay':'100ms', 'duration':'500ms'})


        net.input_sources.append(input_source)


        net.inputs.append(Input(id='Stim_%s'%input_source.id,
                                input_source=input_source.id,
                                population=pop.id,
                                percentage=100))
      
        
                                               
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
        
        sim, net = generate({'olm':5}, 1000)
        
        check_to_generate_or_run(sys.argv, sim)
    