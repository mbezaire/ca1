from neuromllite import *
from neuromllite.NetworkGenerator import *
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)
print colors

def generate(cell, config='IClamp'):
    
    ################################################################################
    ###   Build a new network

    ref = "%s_%s"%(config, cell)
    net = Network(id=ref)
    net.notes = "A simple network: %s."%ref
    net.temperature = 37 # degC
    net.parameters = {}
    

    ################################################################################
    ###   Add some regions
    
    r1 = RectangularRegion(id='region1', x=0,y=0,z=0,width=1000,height=100,depth=1000)
    net.regions.append(r1)


    ################################################################################
    ###   Add some cells

    net.cells.append(Cell(id=cell, neuroml2_source_file='../../cells/%s.cell.nml'%cell))
    


    ################################################################################
    ###   Add some synapses
    
    #ampa = 'wbsFake'
    #net.synapses.append(Synapse(id=ampa, 
    #                            lems_source_file='WangBuzsakiSynapse.xml'))



    ################################################################################
    ###   Add some populations

    comp = '%scell'%cell
    duration = 1000
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
        net.parameters['stim_amp'] = '55pA'
        input_source = InputSource(id='iclamp_0', 
                                   neuroml2_input='PulseGenerator', 
                                   parameters={'amplitude':'stim_amp', 'delay':'50ms', 'duration':'%sms'%duration})

        net.input_sources.append(input_source)

        net.inputs.append(Input(id='Stim0',
                                input_source=input_source.id,
                                population=pop.id,
                                percentage=100))
        
    else:

        input_source = InputSource(id='pfs0', 
                                   neuroml2_input='PoissonFiringSynapse', 
                                   parameters={'average_rate':'50 Hz', 'synapse':ampa, 'spike_target':"./%s"%ampa})

        net.input_sources.append(input_source)


        net.inputs.append(Input(id='Stim0',
                                input_source=input_source.id,
                                population=pop_pv.id,
                                percentage=100))


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
                     dt='0.025',
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
        generate('IClamp_PV')
        generate('IClamp_Pyr')
        
    else:
        #generate('IFcurve_PV')
        generate('olm')
        #generate('IClamp_Pyr')
    