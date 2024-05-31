#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Compares channel dynamics in .mod files and in .nml files (run cd ../.. & ./analyse_modchans.sh and ./analyse_chans.sh first to create the .dat files!)
Authors: András Ecker, Padraig Gleeson, last update: 11.2017
"""

import sys
import os.path
import matplotlib.pyplot as plt
         
chans = ['Kdrfast', 'Kdrslow', 'Kdrp', 'Kdrfastngf',
         'KvA', 'KvAolm', 'KvAproxp', 'KvAdistp', 
         'KvAngf', 'KvGroup',
         'KvCaB',
         'KvMnew',
         'HCN','HCNolm', 'HCNp',  
         'Nav','Navbis', 'Navcck', 'Navccknew',
         'Navaxonp', 'Navp', 'Navngf',
         'CavN']
         
gates = ['m', 'h', 'c', 'd', 'r', 'q', 'n', 'l', 'a', 'b', 'o', 's']

temperatures = [34]  # [24, 34]

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

        for gate in gates:
        
            fig = plt.figure()
            fig.canvas.set_window_title("Time Course(s) of activation variables of %s at %sdegC"%(channel_id, temperature))
            plt.xlabel('Membrane potential (mV)')
            plt.ylabel('Time Course - tau (ms)')
            plt.grid('on')

            tau_lems_file  = '%s.%s.tau.lems.dat'%(channel_id, gate)

            if os.path.isfile(tau_lems_file):
                taus = []
                for line in open(tau_lems_file):
                    ts.append(float(line.split()[0])*1000)
                    taus.append(float(line.split()[1])*1000)

                plt.plot(volts, taus, linestyle='-', linewidth=2, label="LEMS %s %s tau"%(channel_id, gate))

                tau_mod_file  = '../../ch_%s.%s.tau.dat'%(channel_id, gate)

                if os.path.isfile(tau_mod_file):
                    vs = []
                    taus = []
                    for line in open(tau_mod_file):
                        vs.append(float(line.split()[0]))
                        taus.append(float(line.split()[1]))

                    plt.plot(vs, taus, '--x', label="Mod %s %s tau"%(channel_id, gate))
                    
                    plt.legend()
                    fig_name = '%s_%s_tau.png'%(channel_id, gate)
                    plt.savefig('compare/%s'%fig_name, bbox_inches='tight')
                    comparison_readme.write(image_str%(fig_name,fig_name))
                    plt.close("all")


        for gate in gates:
        
            fig = plt.figure()
            fig.canvas.set_window_title("Steady state(s) of activation variables of %s at %sdegC"%(channel_id, temperature))
            plt.xlabel('Membrane potential (mV)')
            plt.ylabel('Steady state (inf)')
            plt.grid('on')

            inf_lems_file  = '%s.%s.inf.lems.dat'%(channel_id, gate)

            if os.path.isfile(inf_lems_file):
                infs = []
                for line in open(inf_lems_file):
                    infs.append(float(line.split()[1]))

                plt.plot(volts, infs, linestyle='-', linewidth=2, label="LEMS %s %s inf"%(channel_id, gate))

                inf_mod_file  = '../../ch_%s.%s.inf.dat'%(channel_id, gate)

                if os.path.isfile(inf_mod_file):
                    vs = []
                    infs = []
                    for line in open(inf_mod_file):
                        vs.append(float(line.split()[0]))
                        infs.append(float(line.split()[1]))

                    plt.plot(vs, infs, '--x', label="Mod %s %s inf"%(channel_id, gate))
                    plt.legend()
                    
                    fig_name = '%s_%s_inf.png'%(channel_id, gate)
                    plt.savefig('compare/%s'%fig_name, bbox_inches='tight')
                    comparison_readme.write(image_str%(fig_name,fig_name))
                    plt.close("all")
       
        comparison_readme.write('</tr></table>\n')

comparison_readme.close()


if not nogui:
    plt.show()
