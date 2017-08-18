#!/usr/bin/python
# -*- coding: utf8 -*-
"""
reproduces Figure 2 D-G from Bezaire et al. 2016
author: András Ecker, last update 08.2017
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set_context("paper")
sns.set_style("white")

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
figFolder = os.path.join(basePath, "figures")


def get_traces(cell_type):
    """gets the voltage traces to different current sweeps"""
    
    assert cell_type in ["pvbasket", "cck", "olm", "ngf"], "cell type: %s not supported here!"%cell_type
    
    fName = "iv_%scell.v.dat"%cell_type
    tmp = {"pvbasket":[500, 8], "cck":[600, 7], "olm":[1000, 5], "ngf":[500, 9]}  # [analysis_duration, nSweeps] helper dict to init containers for results
    
    # first check if the traces are already saved (eg. after running the notebooks)
    if not os.path.isfile(fName):

        # run the simulation if there aren't saved traces
        print("\n running simulations to get traces \n")
        from helper import input_currents
        
        cell_file = "../cells/%s.cell.nml"%cell_type        
        analysis_duration = tmp[cell_type][0]
        if cell_type == "pvbasket":
            custom_amps_nA = [-0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.5]           
        elif cell_type == "cck":
             custom_amps_nA = [-0.1, -0.08, -0.06, -0.04, -0.02, 0.0, 0.08]
        elif cell_type == "olm":
            custom_amps_nA = [-0.1, -0.07, -0.04, -0.01, 0.23]
        elif cell_type == "ngf":
            custom_amps_nA = [-0.13, -0.11, -0.09, -0.07, -0.05, -0.03, -0.01, 0, 0.19]
            
        input_currents(cell_file,
                       custom_amps_nA=custom_amps_nA,
                       analysis_duration=analysis_duration,
                       pre_zero_pulse=50,
                       post_zero_pulse=50)
    
    dt = 0.001; simduration = tmp[cell_type][0] + 100; nSweeps = tmp[cell_type][1]       
    datapoints = int(simduration/dt) + 1
    t = np.linspace(0, simduration, datapoints); traces = np.zeros((nSweeps, datapoints))
                    
    with open(fName) as f:
        for j, line in enumerate(f):
            for i in range(1, nSweeps+1):
                traces[i-1, j] = float(line.split()[i])*1000  # *1000 mV conversion
                
    return t, traces
            

def plot_traces(t, traces, cell_type):
    """plots the different current traces"""
    
    dCols = {"pvbasket":"#20B2AA", "cck":"#DAA520", "olm":"#663399", "ngf":"#DA70D6"} # dummy dict to reproduce the same figure layout ...
    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1)
    sns.despine(bottom=True, left=True)
       
    for i in range(0, traces.shape[0]):
        ax.plot(t, traces[i, :], color=dCols[cell_type])
    
    ax.set_xticks([]); ax.set_yticks([])
    xlim_ = t[-1]
    ax.set_xlim([0, xlim_])
    
    # draw scale bar
    if cell_type == "ngf":
        ax.plot([xlim_-102, xlim_-2], [-80, -80], "k-", lw=3)
        ax.plot([xlim_-2, xlim_-2], [-80, -60], "k-", lw=3)
       
    figName = os.path.join(figFolder, "%s_sweeps.png"%cell_type)
    fig.savefig(figName)
    

if __name__ == "__main__":

    try:
        cell_type = sys.argv[1]
    except:
        cell_type = "ngf"
        
    t, traces = get_traces(cell_type)
    plot_traces(t, traces, cell_type)
    
    plt.show()
    
    
