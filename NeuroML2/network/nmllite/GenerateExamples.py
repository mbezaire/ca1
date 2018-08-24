from neuromllite import *
from neuromllite.NetworkGenerator import *
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)

def generate(cell, config='IClamp'):
    
    ################################################################################
    ###   Build a new network

    ref = "%s_%s"%(config, cell)
    net = Network(id=ref)
    net.notes = "A simple network: %s."%ref
    net.temperature = 34 # degC
    #net.parameters = {}
    

    ################################################################################
    ###   Add some regions
    
    r1 = RectangularRegion(id='region1', x=0,y=0,z=0,width=1000,height=100,depth=1000)
    net.regions.append(r1)


    ################################################################################
    ###   Add some cells

    net.cells.append(Cell(id=cell, neuroml2_source_file='../../cells/%s.cell.nml'%cell))
    


    ################################################################################
    ###   Add some synapses
    
    syn_exc = Synapse(id='syn_poolosyn_to_%s'%cell, 
                      neuroml2_source_file='../../synapses/exp2Synapses.synapse.nml')
    net.synapses.append(syn_exc)



    ################################################################################
    ###   Add some populations

    comp = '%scell'%cell
    duration = 300
    size = 1 

    pop = Population(id='pop_%s'%cell, 
                        size=size, 
                        component=comp, 
                        properties={'color':colors[cell]},
                        random_layout = RandomLayout(region=r1.id))


    net.populations.append(pop)



    ################################################################################
    ###   Add a projection

    '''
    net.projections.append(Projection(id='proj0',
                                      presynaptic=p0.id, 
                                      postsynaptic=p1.id,
                                      synapse='ampa'))

    net.projections[0].random_connectivity=RandomConnectivity(probability=0.5)'''
    
 
    ################################################################################
    ###   Add some inputs
    
    if 'IClamp' in config:
        net.parameters = {}
        net.parameters['stim_amp'] = '450pA'
        input_source = InputSource(id='iclamp_0', 
                                   neuroml2_input='PulseGenerator', 
                                   parameters={'amplitude':'stim_amp', 'delay':'100ms', 'duration':'500ms'})
        duration = 700

        net.input_sources.append(input_source)

        net.inputs.append(Input(id='Stim0',
                                input_source=input_source.id,
                                population=pop.id,
                                percentage=100))
        
    else:
        
        duration = 3000

        net.parameters = {}
        net.parameters['average_rate'] = '100 Hz'
        net.parameters['number_per_cell'] = '10'
        input_source = InputSource(id='pfs0', 
                                   neuroml2_input='PoissonFiringSynapse', 
                                   parameters={'average_rate':'average_rate', 
                                               'synapse':syn_exc.id, 
                                               'spike_target':"./%s"%syn_exc.id})

        net.input_sources.append(input_source)


        net.inputs.append(Input(id='Stim0',
                                input_source=input_source.id,
                                population=pop.id,
                                percentage=100,
                                number_per_cell='number_per_cell'))


    ################################################################################
    ###   Save to JSON format

    net.id = ref

    print(net.to_json())
    new_file = net.to_json_file('%s.json'%(ref))
    

    ################################################################################
    ###   Build Simulation object & save as JSON

    sim = Simulation(id='Sim_%s'%ref,
                     network=new_file,
                     duration=duration,
                     dt='0.01',
                     recordTraces={'all':'*'})

    sim.to_json_file()


    ################################################################################
    ###   Export to some formats
    ###   Try:
    ###        python Example1.py -graph2

    import sys
    check_to_generate_or_run(sys.argv, sim)



if __name__ == "__main__":
    
    if '-all' in sys.argv:
        for cell in colors:
            if cell!='ec' and cell !='ca3':
                generate(cell)
            
        
    else:
        #generate('IFcurve_PV')
        #generate('olm')
        generate('olm',config="PoissonFiringSynapse")
        #generate('bistratified')
        #generate('IClamp_Pyr')
    