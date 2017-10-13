#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Helper methods to analyse the traces of the PING network, saved by NetPyNE
Authors: András Ecker, Padraig Gleeson, last update: 08.2017
"""

import os
import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

#sns.set_context("paper")
sns.set_style("white")

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
figFolder = os.path.join(basePath, "figures")


def get_traces(fName, simduration, dt, popsize=1):
    """reads in single cell traces from file"""
    
    datapoints = int(simduration/dt)
    t = np.linspace(0, simduration-dt, datapoints); traces = np.zeros((popsize, datapoints))
    
    warn = False
    with open(fName) as f_:
        for j, line in enumerate(f_):
            for i in range(1, popsize+1):
                if not np.isnan(float(line.split()[i])):  # added because some wrong NetPyNE saves on NSG have nans inside...
                    traces[i-1, j] = float(line.split()[i])*1000  # *1000 mV conversion
                else:
                    warn = True  # throw warning at the end...
    if warn:
        warnings.warn("*** nan's encountered while loadning NetPyNE saved traces... ***")
                
    return t, traces


def get_spikes_rate(fName, t, popsize):
    """reads in spikes from saved file"""
    
    spikeTimes = []
    spikingNeurons = []
    rate = np.zeros(int(np.ceil(t[-1])))  # np.zeros_like(t) would not be consistent with nrn analysis scripts...
    
    with open(fName) as f_:
        for j, line in enumerate(f_):
            spikingNeurons.append(int(line.split()[0]))
            spiketime = float(line.split()[1])*1000  # *1000 ms conversion
            spikeTimes.append(spiketime); rate[int(spiketime)] += 1
            
    if rate.any():
        rate = rate / (popsize * 0.001)  # normalize rate 
        
    return spikeTimes, spikingNeurons, rate   


def plot_traces(t, dTraces, saveName):
    """plot (randomly selected) traces from each cell type"""

    fig = plt.figure(figsize=(10, 5))
    
    gs = gridspec.GridSpec(2, 1, hspace=0.1)
    ax0 = fig.add_subplot(gs[0]); ax1 = fig.add_subplot(gs[1])
    sns.despine(bottom=True, left=True)
    dSubplots = {"poolosyn":[ax0, "#4169E1", "Pyr."], "pvbasket":[ax1, "#20B2AA", "PV+B."]}  # dummy dict to reproduce the same figure layout ...
                 
    for cell_type, trace in dTraces.iteritems():
        ax, col, ylab = dSubplots[cell_type]
        ax.plot(t, trace, color=col)
        ax.set_ylabel(ylab, rotation=0, labelpad=25, color=col)
        simduration = t[-1]  # could be a sanity check against the one loaded from file...
        if simduration > 1000:
            xlim_ = simduration/2+500
            ax.set_xlim([simduration/2-500, xlim_])
        else:
            xlim_ = simduration
            ax.set_xlim([0, xlim_])
        ax.set_xticks([]); ax.set_yticks([])
    # draw scale bar
    ax1.plot([xlim_-102, xlim_-2], [-70, -70], "k-", lw=3)
    ax1.plot([xlim_-2, xlim_-2], [-70, -20], "k-", lw=3)
        
    figName = os.path.join(figFolder, "%s_traces.png"%saveName)
    fig.savefig(figName)


def plot_rasters(dSpikeTimes, dSpikingNeurons, simduration, saveName):
    """raster plots"""
    
    fig = plt.figure(figsize=(10, 5))
    
    gs = gridspec.GridSpec(2, 1, height_ratios=[1.5, 1], hspace=0.1)
    ax0 = fig.add_subplot(gs[0]); ax1 = fig.add_subplot(gs[1])
    dSubplots = {"poolosyn":[ax0, "#4169E1", "Pyr."], "pvbasket":[ax1, "#20B2AA", "PV+B."]}  # dummy dict to reproduce the same figure layout ...   
    
    for cell_type, spikeTimes in dSpikeTimes.iteritems():
        spikingNeurons = dSpikingNeurons[cell_type]; ax, col, ylab = dSubplots[cell_type]      
        ax.scatter(spikeTimes, spikingNeurons, color=col, marker='.')
        ax.set_ylabel(ylab, rotation=0, labelpad=25, color=col)
        if simduration > 1000:
            ax.set_xlim([simduration/2-500, simduration/2+500])
        else:
            ax.set_xlim([0, simduration])
        ax.set_xticks([]); ax.set_yticks([])
    
    figName = os.path.join(figFolder, "%s_rasters.png"%saveName)
    fig.savefig(figName)

          
if __name__ == "__main__":

    ref = "Sim_PINGNet_0_1"
    dPopsize = {"poolosyn":5, "pvbasket":3}
    
    dTraces = {}; dSpikeTimes = {}; dSpikingNeurons = {}
    for cell_type in ["poolosyn", "pvbasket"]:
        t, traces = get_traces("%s.%scell.v.dat"%(ref, cell_type), 100, 0.01)
        dTraces[cell_type] = traces[0, :]
        spikeTimes, spikingNeurons, _ = get_spikes_rate("%s.pop_%s.spikes"%(ref, cell_type), t, dPopsize[cell_type])
        dSpikeTimes[cell_type] = spikeTimes; dSpikingNeurons[cell_type] = spikingNeurons
    
    plot_rasters(dSpikeTimes, dSpikingNeurons, simduration=t[-1], saveName="test")
    plot_traces(t, dTraces, saveName="test")
    
    plt.show()
    
        
