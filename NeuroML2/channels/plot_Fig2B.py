#!/usr/bin/python
# -*- coding: utf8 -*-
"""
reproduces Figure 2 B (and some simular channel sum. figures) from Bezaire et al. 2016
author: András Ecker, last update 08.2017
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context("talk")
sns.set_style("white")

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
figFolder = os.path.join(basePath, "figures")


def get_inf(channel_name, gating_variables):  # Note: to get the data files run pynml-channelanalysis first
    """loads in inf variables from .dat files"""

    d_inf = {}
    for gate_var in gating_variables:
        tmp = []
        with open("%s.%s.inf.lems.dat"%(channel_name, gate_var)) as f:
            for line in f:
                tmp.append(float(line.split()[1]))
        d_inf[gate_var] = tmp
        
    v = np.linspace(-100, 100, len(d_inf[gate_var]))
    
    return v, d_inf
    
  
def get_tau(channel_name, gating_variables):  # Note: to get the data files run pynml-channelanalysis first
    """loads in tau variables from .dat files"""

    d_tau = {}
    for gate_var in gating_variables:
        tmp = []
        with open("%s.%s.tau.lems.dat"%(channel_name, gate_var)) as f:
            for line in f:
                tmp.append(float(line.split()[1]))
        d_tau[gate_var] = tmp
        
    v = np.linspace(-100, 100, len(d_inf[gate_var]))
    
    return v, d_tau
    

def plot_inf(v, d_inf, channel_name, dCols):
    """plot inf variables"""
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    sns.despine()
    
    for gate_var, inf in d_inf.iteritems():
        ax.plot(v, inf, label="%s %s inf"%(channel_name, gate_var), color=dCols[gate_var])
        
    ax.set_xlabel("Membrane potential (mV)")
    ax.set_xlim([-100, 100])
    ax.set_ylabel("Steady state / inf")
    ax.legend()
    
    figName = os.path.join(figFolder, "%s_inf.png"%channel_name)
    fig.savefig(figName)
    
    
def plot_tau(v, d_tau, channel_name, dCols):
    """plot tau variables"""
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    sns.despine()
    
    for gate_var, tau in d_tau.iteritems():
        ax.plot(v, tau, label="%s %s tau"%(channel_name, gate_var), color=dCols[gate_var])
        
    ax.set_xlabel("Membrane potential (mV)")
    ax.set_xlim([-100, 100])
    ax.set_ylabel("Time course / tau (ms)")
    ax.legend()
    
    figName = os.path.join(figFolder, "%s_tau.png"%channel_name)
    fig.savefig(figName)
    
    
    
if __name__ == "__main__":

    try:
        channel_name = sys.argv[1]
    except:
        channel_name = "Nav"
    
    # hard coded for Nav, KvA   
    gating_variables = {"Nav":["m", "h"], "KvA":["n", "l"]}  
    dCols = {"m":"#4682B4", "h":"#2E8B57", "n":"#A52A2A", "l":"#8A2BE2"}
    
    v, d_inf = get_inf(channel_name, gating_variables[channel_name])
    _, d_tau = get_tau(channel_name, gating_variables[channel_name])
    
    plot_inf(v, d_inf, channel_name, dCols)
    plot_tau(v, d_tau, channel_name, dCols)
    
    plt.show()
                
                
