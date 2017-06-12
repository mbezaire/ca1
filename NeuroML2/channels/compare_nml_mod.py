import matplotlib.pyplot as pylab
import os.path
import sys


chans = ['KvCaB']
         
chans = ['Kdrfast', 'Kdrslow', 'Kdrp', 'Kdrfastngf',
         'KvA','KvAolm', 'KvAproxp', 'KvAdistp', 
         'KvAngf', 'KvGroup',
         'KvCaB',
         'HCN','HCNolm', 'HCNp',  
         'Nav','Navbis', 'Navcck','Navaxonp',
         'Navp','Navapicalp', 'Navngf',
         'CavL', 'CavN']
         
         
#chans = ['Nav','Navbis', 'Navcck', 'Navngf', 'Navp']
#chans = ['KvCaB']

gates = ['m', 'h', 'c', 'd', 'r', 'q', 'n', 'l', 'a', 'b', 'o', 's']

temperatures = [24]

comparison_readme = open('compare/README.md','w')

image_str = '<td><a href="%s"><img alt="???" src="%s" height="200"/></a></td>\n'

nogui = '-nogui' in sys.argv

for temperature in temperatures:

    for channel_id in chans:
        
        comparison_readme.write("\n#### %s\n"%channel_id)
        comparison_readme.write('<p><a href="../../../ch_%(cid)s.mod">ch_%(cid)s.mod</a>, <a href="../%(cid)s.channel.nml">%(cid)s.channel.nml</a></p>\n'%{'cid':channel_id})
        comparison_readme.write('<table><tr>\n')

        vramp_lems_file  = '%s.rampV.lems.dat'%channel_id

        ts = []
        volts = []
        for line in open(vramp_lems_file):
            ts.append(float(line.split()[0])*1000)
            volts.append(float(line.split()[1])*1000)

        fig = pylab.figure()
        fig.canvas.set_window_title("Time Course(s) of activation variables of %s at %sdegC"%(channel_id, temperature))

        pylab.xlabel('Membrane potential (mV)')
        pylab.ylabel('Time Course - tau (ms)')
        pylab.grid('on')

        for gate in gates:

            tau_lems_file  = '%s.%s.tau.lems.dat'%(channel_id, gate)

            if os.path.isfile(tau_lems_file):
                taus = []
                for line in open(tau_lems_file):
                    ts.append(float(line.split()[0])*1000)
                    taus.append(float(line.split()[1])*1000)

                pylab.plot(volts, taus, linestyle='-', linewidth=2, label="LEMS %s %s tau"%(channel_id, gate))

                tau_mod_file  = '../../ch_%s.%s.tau.dat'%(channel_id, gate)

                if os.path.isfile(tau_mod_file):
                    vs = []
                    taus = []
                    for line in open(tau_mod_file):
                        vs.append(float(line.split()[0]))
                        taus.append(float(line.split()[1]))

                    pylab.plot(vs, taus, '--x', label="Mod %s %s tau"%(channel_id, gate))
                    
                    pylab.legend()
                    fig_name = '%s_%s_tau.png'%(channel_id, gate)
                    pylab.savefig('compare/%s'%fig_name,bbox_inches='tight')
                    comparison_readme.write(image_str%(fig_name,fig_name))




        fig = pylab.figure()
        fig.canvas.set_window_title("Steady state(s) of activation variables of %s at %sdegC"%(channel_id, temperature))

        pylab.xlabel('Membrane potential (mV)')
        pylab.ylabel('Steady state (inf)')
        pylab.grid('on')
        
        # comparison_readme.write('</tr><tr>\n')

        for gate in gates:

            inf_lems_file  = '%s.%s.inf.lems.dat'%(channel_id, gate)

            if os.path.isfile(inf_lems_file):
                infs = []
                for line in open(inf_lems_file):
                    infs.append(float(line.split()[1]))

                pylab.plot(volts, infs, linestyle='-', linewidth=2, label="LEMS %s %s inf"%(channel_id, gate))

                inf_mod_file  = '../../ch_%s.%s.inf.dat'%(channel_id, gate)

                if os.path.isfile(inf_mod_file):
                    vs = []
                    infs = []
                    for line in open(inf_mod_file):
                        vs.append(float(line.split()[0]))
                        infs.append(float(line.split()[1]))

                    pylab.plot(vs, infs, '--x', label="Mod %s %s inf"%(channel_id, gate))
                    pylab.legend()
                    
                    fig_name = '%s_%s_inf.png'%(channel_id, gate)
                    pylab.savefig('compare/%s'%fig_name,bbox_inches='tight')
                    comparison_readme.write(image_str%(fig_name,fig_name))

        
        comparison_readme.write('</tr></table>\n')

comparison_readme.close()

if not nogui:
    pylab.show()
