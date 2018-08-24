import sys

import pprint; pp = pprint.PrettyPrinter(depth=6)

from neuromllite.sweep.ParameterSweep import ParameterSweep
from neuromllite.sweep.ParameterSweep import NeuroMLliteRunner
       
sys.path.append("..") 
from GenerateHippocampalNet_oc import helper_getcolor

colors = helper_getcolor(None)

if __name__ == '__main__':


    if '-all' in sys.argv:
        
        print('Generating all plots')
        save_fig_dir = './'
        html = '<table>\n'
        
        fixed = {'dt':0.001, 'duration':700}


        vary = {'stim_amp':['%spA'%(i) for i in xrange(-50,400,50)]}
        #vary = {'stim_amp':['%spA'%(i/10.0) for i in xrange(-10,20,5)]}
        #vary = {'stim_amp':['1.5pA','2pA']}

        for type in colors:
            if type!='ec' and type !='ca3':

                run = True
                #run = False
                
                if run:
                
                    nmllr = NeuroMLliteRunner('Sim_IClamp_%s.json'%type,
                                              simulator='jNeuroML_NEURON')
                    ps = ParameterSweep(nmllr, 
                                        vary, 
                                        fixed,
                                        num_parallel_runs=16,
                                      save_plot_all_to='firing_rates_%s.png'%type,
                                      heatmap_all=True,
                                      save_heatmap_to='heatmap_%s.png'%type,
                                        plot_all=True, 
                                        show_plot_already=False)

                    report = ps.run()

                    #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
                    ps.plotLines('stim_amp','mean_spike_frequency',save_figure_to='mean_spike_frequency_%s.png'%type)
                
                
                html+='<tr>\n'
                html+='  <td><b>'+type+'</b></td>\n'
                html+='  <td><a href="mean_spike_frequency_%s.png'%type+'">\n'
                html+='    <img alt="?" src="mean_spike_frequency_%s.png'%type+'" height="180"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="firing_rates_%s.png'%type+'">\n'
                html+='    <img alt="?" src="firing_rates_%s.png'%type+'" height="180"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="heatmap_%s.png'%type+'">\n'
                html+='    <img alt="?" src="heatmap_%s.png'%type+'" height="180"/></a>\n'
                html+='  </td>\n'
                html+='<tr>\n'

        import matplotlib.pyplot as plt
        if not '-nogui' in sys.argv:
            print("Showing plots")
            plt.show()
            
            
        with open(save_fig_dir+'info.html','w') as f:
            f.write('<html><body>\n%s\n</body></html>'%html)
        with open(save_fig_dir+'README.md','w') as f2:
            f2.write('### CA1 cell summary \n%s'%(html.replace('.html','.md')))
        
    else:
        
        fixed = {'dt':0.01, 'duration':700}

        quick = False
        #quick=True

        vary = {'stim_amp':['%spA'%(i/10.0) for i in xrange(-10,20,2)]}
        vary = {'dt':[0.1,0.05,0.025,0.01,0.005,0.0025,0.001,0.0005,0.00025,0.0001]}
        vary = {'dt':[0.1,0.05,0.025,0.01,0.005,0.0025,0.001]}
        vary = {'dt':[0.1,0.05,0.025,0.01,0.005]}
        
        #vary = {'number_per_cell':[i for i in xrange(0,250,10)]}
        #vary = {'stim_amp':['1pA','1.5pA','2pA']}
        vary = {'stim_amp':['%spA'%(i) for i in xrange(-100,500,50)]}

        type = 'bistratified'
        #type = 'ivy'
        type = 'ngf'
        type = 'olm'
        #type='poolosyn'
        config = 'IClamp'
        #config = 'PoissonFiringSynapse'

        nmllr = NeuroMLliteRunner('Sim_%s_%s.json'%(config,type),
                                  simulator='jNeuroML_NEURON')

        if quick:
            pass

        ps = ParameterSweep(nmllr, vary, fixed,
                            num_parallel_runs=16,
                                  plot_all=True, 
                                  save_plot_all_to='firing_rates_%s.png'%type,
                                  heatmap_all=True,
                                  save_heatmap_to='heatmap_%s.png'%type,
                                  show_plot_already=False)

        report = ps.run()
        ps.print_report()

        #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
        ps.plotLines('stim_amp','mean_spike_frequency',save_figure_to='mean_spike_frequency_%s.png'%type)
        #ps.plotLines('dt','mean_spike_frequency',save_figure_to='mean_spike_frequency_%s.png'%type, logx=True)
        #ps.plotLines('number_per_cell','mean_spike_frequency',save_figure_to='poisson_mean_spike_frequency_%s.png'%type)

        import matplotlib.pyplot as plt
        if not '-nogui' in sys.argv:
            print("Showing plots")
            plt.show()