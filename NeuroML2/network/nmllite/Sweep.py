import sys
import json

import pprint; pp = pprint.PrettyPrinter(depth=6)
from pyneuroml import pynml

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


        #vary = {'stim_amp':['%spA'%(i) for i in xrange(-100,500,2)]}
        vary = {'stim_amp':['%spA'%(i*10.0) for i in xrange(-10,50,5)]}
        #vary = {'stim_amp':['-100pA','0pA','100pA','200pA','300pA','400pA']}
        
        cells = colors.keys()
        #cells = ['olm','ivy']
        #cells = ['olm']
        #cells.remove('olm')
        #cells.remove('sca')
        #cells.remove('ivy')
        #cells.remove('bistratified')
        #cells.remove('ngf')
        #cells.remove('pvbasket')
        #cells = ['poolosyn']
        #fixed['dt']=0.025

        for type in cells:
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
                                        save_plot_all_to='images/firing_rates_%s.png'%type,
                                        heatmap_all=True,
                                        save_heatmap_to='images/heatmap_%s.png'%type,
                                        heatmap_lims=[-100,20],
                                        plot_all=True, 
                                        show_plot_already=False)

                    report = ps.run()

                    #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
                    ps.plotLines('stim_amp','mean_spike_frequency',save_figure_to='images/mean_spike_frequency_%s.png'%type)
                
                height = '160'
                html+='<tr>\n'
                html+='  <td width=30><b>'+type+'</b></td>\n'
                html+='  <td><a href="images/mean_spike_frequency_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/mean_spike_frequency_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/firing_rates_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/firing_rates_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/heatmap_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/heatmap_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/dt_traces_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/dt_traces_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/heatmap_dt_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/heatmap_dt_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/mean_spike_frequency_dt_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/mean_spike_frequency_dt_%s.png'%type+'" height="'+height+'"/></a>\n'
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
        
    elif '-dt' in sys.argv:
        
        optimal_stim = {'olm':100,'sca':100,'pvbasket':350,'ivy':220,'ngf':220,'bistratified':350,'cck':180,'axoaxonic':220,'poolosyn':280}
        #optimal_stim = {'olm':100,'sca':100}
        #optimal_stim = {'olm':100}
        #optimal_stim = {'pvbasket':350}
        

        vary = {'dt':[0.1,0.05,0.025,0.01,0.005,0.0025,0.001,0.0005,0.00025,0.0001]}
        vary = {'dt':[0.025,0.02,0.015,0.01,0.005,0.0025,0.001,0.0005]}
        vary = {'dt':[0.025,0.02,0.015,0.01,0.005,0.0025]}
        #vary = {'dt':[0.025,0.01,0.005,0.0025,0.001]}
        #vary = {'dt':[0.1,0.05,0.025,0.01,0.005]}
        #vary = {'dt':[0.05,0.025,0.01]}
        vary = {'dt':[0.025,0.01,0.005,0.0025,0.001]}
        vary = {'dt':[0.025,0.01,0.005,0.0025,0.001,0.0005,0.00025]}

        for type in optimal_stim:
            if type!='ec' and type !='ca3':

                run = True
                
                if run:
                
                    fixed = {'duration':700, 'stim_amp':'%spA'%optimal_stim[type]}
                    
                    nmllr = NeuroMLliteRunner('Sim_IClamp_%s.json'%type,
                                              simulator='jNeuroML_NEURON')
                    ps = ParameterSweep(nmllr, 
                                        vary, 
                                        fixed,
                                        num_parallel_runs=16,
                                        save_plot_all_to='images/dt_traces_%s.png'%type,
                                        heatmap_all=True,
                                        save_heatmap_to='images/heatmap_dt_%s.png'%type,
                                        plot_all=True, 
                                        show_plot_already=False)

                    report = ps.run()

                    #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
                    ps.plotLines('dt','mean_spike_frequency',save_figure_to='images/mean_spike_frequency_dt_%s.png'%type, logx=True)
                
                

        import matplotlib.pyplot as plt
        if not '-nogui' in sys.argv:
            print("Showing plots")
            plt.show()
            
    elif '-pois' in sys.argv:
        
        cells = colors.keys()
        #cells = ['olm','ivy']
        #cells = ['olm']
        #cells = ['axoaxonic','ivy']
        save_fig_dir = './'
        html = '<table>\n'
 
        vary = {'average_rate':['%sHz'%f for f in xrange(1,500,10)]}
        fixed = {'duration':1000, 'number_per_cell':30}
        
        vary = {'average_rate':['%sHz'%f for f in xrange(1,500,10)],
                'number_per_cell':[1,10,30,50,100,300,500]}
                
        vary = {'average_rate':['%sHz'%f for f in xrange(1,500,50)],
                'number_per_cell':[5,20,50,100,200],
                'seed':[i for i in range(1)]}
                
        #vary = {'average_rate':['%sHz'%f for f in xrange(1,2000,200)],
        #        'seed':[i for i in range(5)]}
                
        from GenerateNetwork import largest_allowable_dt
        fixed = {'duration':1000, 'number_per_cell':20}
        fixed = {'duration':1000}

        for type in cells:
            if type!='ec' and type !='ca3':

                run = True
                
                if run:
                    nmllr = NeuroMLliteRunner('Sim_PoissonFiringSynapse_%s.json'%type,
                                              simulator='jNeuroML_NEURON')
                    fixed['dt'] = largest_allowable_dt[type]
                    ps = ParameterSweep(nmllr, 
                                        vary, 
                                        fixed,
                                        num_parallel_runs=17,
                                        save_plot_all_to='images/pois_traces_%s.png'%type,
                                        heatmap_all=False,
                                        plot_all=True, 
                                        show_plot_already=False)

                    report = ps.run()

                    #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
                    ps.plotLines('average_rate',
                                 'mean_spike_frequency',
                                 #second_param='seed',
                                 second_param='number_per_cell',
                                 save_figure_to='images/pois_traces_average_rate_%s.png'%type)
                                 
                    #print report
                    with open('report_%s_pois.json'%type, 'w') as outfile:
                        json.dump(report, outfile, ensure_ascii=False, indent=4)
                                
                height = '160'
                html+='<tr>\n'
                html+='  <td width="30%"><b>'+type+'</b>\n'
                for f in fixed:
                    html+='<p><sup>%s = %s</sup></p>\n'%(f,fixed[f])
                for v in vary:
                    vs = vary[v]
                    html+='<p><sup>%s = %s-&gt;%s</sup></p>\n'%(v,vs[0],vs[-1])
                html+='</td>\n'
                html+='  <td><a href="images/pois_traces_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/pois_traces_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
                html+='  <td><a href="images/pois_traces_average_rate_%s.png'%type+'">\n'
                html+='    <img alt="?" src="images/pois_traces_average_rate_%s.png'%type+'" height="'+height+'"/></a>\n'
                html+='  </td>\n'
             
                html+='<tr>\n'
                
                

        import matplotlib.pyplot as plt
        if not '-nogui' in sys.argv:
            print("Showing plots")
            plt.show()
            
        with open(save_fig_dir+'poisson_inputs.html','w') as f:
            f.write('<html><body>\n%s\n</body></html>'%html)
        with open(save_fig_dir+'poisson_inputs.md','w') as f2:
            f2.write('### CA1 cells response to poisson inputs \n%s'%(html.replace('.html','.md')))
            
        
    elif '-curves' in sys.argv:
        
        cells = colors.keys()
        #cells = ['olm','ivy']
        #cells = ['olm']
        
        xs = []
        ys = []
        p_colors = []
        labels = []
        markers = []
        linewidths=[]
        
        rates = {}
        
        for type in cells:
            if type!='ec' and type !='ca3':
                rates[type] = {}
                
                f = 'report_%s_pois.json'%type
                print('Opening: %s'%f)
                with open(f, 'r') as rep:
                    report = json.load(rep)
                    
                for s in report["Simulations"]:
                    params = report["Simulations"][s]["parameters"]
                    n = params["number_per_cell"]
                    if not n in rates[type]:
                        rates[type][n] = {}
                    rate = float(params["average_rate"][:-2])
                    freq = report["Simulations"][s]["analysis"].values()[0]["mean_spike_frequency"]
                    print('Rate for %i inputs at %s Hz: %s Hz'%(n, rate, freq))
                    
                    rates[type][n][n*rate] = freq
                    
                for n in rates[type]:
                    
                    xx = []
                    yy = []
                    for in_r in sorted(rates[type][n].keys()):
                        xx.append(in_r)
                        yy.append(rates[type][n][in_r])
                    xs.append(xx)
                    ys.append(yy)

                    labels.append('%s_%i'%(type,n))
                    rgb = colors[type].split()
                    c_hex = '#'
                    for a in rgb:
                        c_hex = c_hex+'%02x'%int(float(a)*255)
                    p_colors.append(c_hex)
                    markers.append('o')
                    linewidths.append(0.2)
                    

                    
        ax = pynml.generate_plot(xs,                    
                         ys,               
                         "Rates",  
                         labels = labels,
                         markers = markers,
                         colors=p_colors,
                         linewidths = linewidths,
                         xaxis = 'Total input rate (Hz)',      
                         yaxis = 'Output rate (Hz)',  
                         title_above_plot = True,
                         show_plot_already=True)     # Save figure
        
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
                                  save_plot_all_to='images/firing_rates_%s.png'%type,
                                  heatmap_all=True,
                                  save_heatmap_to='images/heatmap_%s.png'%type,
                                  show_plot_already=False)

        report = ps.run()
        ps.print_report()

        #ps.plotLines('stim_amp','average_last_1percent',save_figure_to='average_last_1percent_%s.png'%type)
        ps.plotLines('stim_amp','mean_spike_frequency',save_figure_to='images/mean_spike_frequency_%s.png'%type)
        #ps.plotLines('dt','mean_spike_frequency',save_figure_to='mean_spike_frequency_%s.png'%type, logx=True)
        #ps.plotLines('number_per_cell','mean_spike_frequency',save_figure_to='poisson_mean_spike_frequency_%s.png'%type)

        import matplotlib.pyplot as plt
        if not '-nogui' in sys.argv:
            print("Showing plots")
            plt.show()