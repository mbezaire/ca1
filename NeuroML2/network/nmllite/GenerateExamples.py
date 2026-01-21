from neuromllite import *
from neuromllite.NetworkGenerator import *
from neuromllite.utils import create_new_model
import sys

sys.path.append("..")

from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)

def generate(cell, duration, config='IClamp'):
    
    reference = "%s_%s"%(config, cell)

    cell_id = '%scell'%cell
    cell_nmll = Cell(id=cell_id, neuroml2_source_file='../../cells/%s.cell.nml'%cell)
    synapses = []
 
    ################################################################################
    ###   Add some inputs
    
    if 'IClamp' in config:
        parameters = {}
        parameters['stim_amp'] = '350pA'
        input_source = InputSource(id='iclamp_0', 
                                   neuroml2_input='PulseGenerator', 
                                   parameters={'amplitude':'stim_amp', 'delay':'100ms', 'duration':'500ms'})
      
        
    elif 'PoissonFiringSynapse' in config:
        
        syn_exc = Synapse(id='syn_poolosyn_to_%s'%cell, 
                      neuroml2_source_file='../../synapses/exp2Synapses.synapse.nml')
        syn_exc = Synapse(id='syn_poolosyn_to_pvbasket', 
                      neuroml2_source_file='../../synapses/exp2Synapses.synapse.nml')
    
        synapses.append(syn_exc)

        parameters = {}
        parameters['average_rate'] = '100 Hz'
        parameters['number_per_cell'] = '10'
        input_source = InputSource(id='pfs0', 
                                   neuroml2_input='PoissonFiringSynapse', 
                                   parameters={'average_rate':'average_rate', 
                                               'synapse':syn_exc.id, 
                                               'spike_target':"./%s"%syn_exc.id})
                                               
    network_filename = '%s.json'%reference         
    
    sim, net = create_new_model(reference,
                     duration, 
                     dt=0.01, # ms 
                     temperature=34, # degC
                     default_region='CA1',
                     parameters = parameters,
                     cell_for_default_population=cell_nmll,
                     color_for_default_population=colors[cell],
                     input_for_default_population=input_source,
                     synapses=synapses,
                     network_filename=network_filename)
                     
    if 'PoissonFiringSynapse' in config:
        
        net.inputs[0].number_per_cell = 'number_per_cell'
        print(net.inputs[0])
        
        # Resave...
        net.to_json_file(network_filename)
    
    return sim, net



if __name__ == "__main__":
    
    if '-all' in sys.argv:
        for cell in colors:
            if cell!='ec' and cell !='ca3':
                generate(cell, 700, config="IClamp")
                generate(cell, 1000, config="PoissonFiringSynapse")
            
        
    else:
        #generate('IFcurve_PV')
        #generate('olm')
        #sim, net = generate('olm', 700, config="IClamp")
        sim, net = generate('olm', 1000, config="PoissonFiringSynapse")
        #generate('bistratified')
        #generate('IClamp_Pyr')
        
        check_to_generate_or_run(sys.argv, sim)
    