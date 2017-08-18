#!/usr/bin/python
# -*- coding: utf8 -*-
"""
helper file (plotting PSD analysis, raster)
author: András Ecker, last update 08.2017
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

#sns.set_context("paper")
sns.set_style("white")

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
figFolder = os.path.join(basePath, "figures")


def plot_LFP(t, LFP, filteredLFP, f, Pxx, simduration, runName):
    """plots LFP, theta filtered LFP and PSD of LFP"""
    
    # cut out the initial transients from LFP (until 50ms)
    t = np.asarray(t)
    tmp = np.where(50 < t)[0][0]
    plotT = t[tmp:]
    plotLFP = LFP[tmp:]
    # cut out the initial transients of the filtered LFP (until 50ms)
    plotFilteredLFP = filteredLFP[tmp:]
    
    # cut PSD at 100Hz (and plot only below)
    PxxdB = 10*np.log10(Pxx/max(Pxx))
    f = np.asarray(f)
    tmp = np.where(f < 100)[0][-1]
    plotF = f[0:tmp]
    plotPxx = PxxdB[0:tmp]
    # separate theta band (and plot in diff color)
    thetaS = np.where(5 < f)[0][0]
    thetaE = np.where(f < 10)[0][-1]
    fTheta = f[thetaS:thetaE]
    PxxTheta = PxxdB[thetaS:thetaE]
    
    
    fig = plt.figure(figsize=(10, 8))
    
    ax = fig.add_subplot(3,1,1)
    #ax.plot(t, LFP, "b-")
    ax.plot(plotT, plotLFP, "b-")
    #ax.set_xlim([0, simduration])
    ax.set_xlim([50, simduration])
    ax.set_title("Local Field Potential of PCs")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("LFP (mV)")
    
    ax2 = fig.add_subplot(3,1,2)
    #ax2.plot(t, filteredLFP, "b-")
    ax2.plot(plotT, plotFilteredLFP, "r-")
    #ax2.set_xlim([0, simduration])
    ax2.set_xlim([50, simduration])
    ax2.set_title("Theta filtered LFP")
    ax2.set_xlabel("Time (ms)")
    ax2.set_ylabel("LFP (mV)")
    
    ax3 = fig.add_subplot(3,1,3)
    #ax3.plot(f, PxxdB, "b-", marker="o")
    ax3.plot(plotF, plotPxx, "b-", marker="o")
    ax3.plot(fTheta, PxxTheta, "r-", marker="o", lw=2, label="theta (5-10Hz)")
    #ax3.set_xlim([0, nyq])
    ax3.set_xlim([0, 100])
    ax3.set_title("Power Spectrum Density of LFP")
    ax3.set_xlabel("Frequency (Hz)")
    ax3.set_ylabel("PSD (dB)")
    ax3.legend()
    
    fig.tight_layout()
    
    figName = os.path.join(figFolder, "LFP_%s.png"%runName)
    fig.savefig(figName)
    
    
def plot_SDF(SDF, f, Pxx, runName):
    """plots SDF (smoothed rate) and PSD of SDF"""
    
    simduration = SDF.shape[0]
    t = np.linspace(1, simduration, simduration)
    # cut out the initial transients from SDF (until 50ms)
    tmp = np.where(50 < t)[0][0]
    plotT = t[tmp:]
    plotSDF = SDF[tmp:]
    
    # cut PSD at 100Hz (and plot only below)
    PxxdB = 10*np.log10(Pxx/max(Pxx))
    f = np.asarray(f)
    tmp = np.where(f < 100)[0][-1]
    plotF = f[0:tmp]
    plotPxx = PxxdB[0:tmp]
    # separate theta band (and plot in diff color)
    thetaS = np.where(5 < f)[0][0]
    thetaE = np.where(f < 10)[0][-1]
    fTheta = f[thetaS:thetaE]
    PxxTheta = PxxdB[thetaS:thetaE]
    
    
    fig = plt.figure(figsize=(10, 8))
    
    ax = fig.add_subplot(2,1,1)
    #ax.plot(t, SDF, "b-")
    ax.plot(plotT, plotSDF, "b-")
    #ax.set_xlim([0, simduration])
    ax.set_xlim([50, simduration])
    ax.set_title("Spike Density Function (rate) of PCs")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("SDF (Hz)")
    
    ax2 = fig.add_subplot(2,1,2)
    #ax2.plot(f, PxxdB, "b-", marker="o")
    ax2.plot(plotF, plotPxx, "b-", marker="o")
    ax2.plot(fTheta, PxxTheta, "r-", marker="o", lw=2, label="theta (5-10Hz)")
    #ax2.set_xlim([0, nyq])
    ax2.set_xlim([0, 100])
    ax2.set_title("Power Spectrum Density of SDF")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("PSD (dB)")
    ax2.legend()
    
    fig.tight_layout()
    
    figName = os.path.join(figFolder, "SDF_%s.png"%runName)
    fig.savefig(figName)


def plot_raster(spikingNeurons, spikeTimes, simduration, startID, endID, runName):
    """raster plot (used to visualize PC spikes)"""
    
    fig = plt.figure(figsize=(10, 8))
        
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(spikeTimes, spikingNeurons, c="blue", marker='.')
    ax.set_title("PC raster")
    if simduration > 1000:
        ax.set_xlim([simduration/2-500, simduration/2+500,])
    else:
        ax.set_xlim([0, simduration])
    ax.set_xlabel("Time (ms)")
    ax.set_ylim([startID, endID])
    ax.set_ylabel("Neuron number")
    
    figName = os.path.join(figFolder, "raster_%s.png"%runName)
    fig.savefig(figName)
    
    
def plot_rasters(dSpikeTimes, dSpikingNeurons, dIDx, simduration, runName):
    """raster plots (used to reproduce Fig3 C,)"""
    
    fig = plt.figure(figsize=(10, 7))
    
    gs = gridspec.GridSpec(9, 1, height_ratios=[4, 1, 1, 1, 1, 1, 1, 1, 1], hspace=0.1)
    ax0 = fig.add_subplot(gs[0]); ax1 = fig.add_subplot(gs[1]); ax2 = fig.add_subplot(gs[2])
    ax3 = fig.add_subplot(gs[3]); ax4 = fig.add_subplot(gs[4]); ax5 = fig.add_subplot(gs[5])
    ax6 = fig.add_subplot(gs[6]); ax7 = fig.add_subplot(gs[7]); ax8 = fig.add_subplot(gs[8])    
    dSubplots = {"poolosyn":[ax0, "#4169E1", "Pyr."], "pvbasket":[ax1, "#20B2AA", "PV+B."],
                 "cck":[ax2, "#DAA520", "CCK+B."], "sca":[ax3, "#FFA07A", "S.C.-A."], 
                 "axoaxonic":[ax4, "#FF0000", "Axo"], "bistratified":[ax5, "#A0522D", "Bis."],
                 "olm":[ax6, "#663399", "O-LM"], "ivy":[ax7, "#A9A9A9", "Ivy"],
                 "ngf":[ax8, "#DA70D6", "NGF."]}  # dummy dict to reproduce the same figure layout ...   
    
    for cell_type, spikeTimes in dSpikeTimes.iteritems():
        spikingNeurons = dSpikingNeurons[cell_type]; ax, col, ylab = dSubplots[cell_type]; idx = dIDx[cell_type]        
        ax.scatter(spikeTimes, spikingNeurons, color=col, marker='.', s=0.8)
        ax.set_ylabel(ylab, rotation=0, labelpad=25, color=col); ax.set_ylim([idx[0], idx[-1]])
        if simduration > 1000:
            ax.set_xlim([simduration/2-500, simduration/2+500])
        else:
            ax.set_xlim([0, simduration])
        ax.set_xticks([]); ax.set_yticks([])
    
    figName = os.path.join(figFolder, "rasters_%s.png"%runName)
    fig.savefig(figName)
    

def plot_traces(dTraces, t, runName):
    """plot (randomly selected) traces from each cell type"""

    fig = plt.figure(figsize=(10, 7))
    
    gs = gridspec.GridSpec(9, 1, hspace=0.1)
    ax0 = fig.add_subplot(gs[0]); ax1 = fig.add_subplot(gs[1]); ax2 = fig.add_subplot(gs[2])
    ax3 = fig.add_subplot(gs[3]); ax4 = fig.add_subplot(gs[4]); ax5 = fig.add_subplot(gs[5])
    ax6 = fig.add_subplot(gs[6]); ax7 = fig.add_subplot(gs[7]); ax8 = fig.add_subplot(gs[8])
    sns.despine(bottom=True, left=True)
    dSubplots = {"poolosyn":[ax0, "#4169E1", "Pyr."], "pvbasket":[ax1, "#20B2AA", "PV+B."],
                 "cck":[ax2, "#DAA520", "CCK+B."], "sca":[ax3, "#FFA07A", "S.C.-A."], 
                 "axoaxonic":[ax4, "#FF0000", "Axo"], "bistratified":[ax5, "#A0522D", "Bis."],
                 "olm":[ax6, "#663399", "O-LM"], "ivy":[ax7, "#A9A9A9", "Ivy"],
                 "ngf":[ax8, "#DA70D6", "NGF."]}  # dummy dict to reproduce the same figure layout ...
                 
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
    ax8.plot([xlim_-102, xlim_-2], [-70, -70], "k-", lw=3)
    ax8.plot([xlim_-2, xlim_-2], [-70, -20], "k-", lw=3)
        
    figName = os.path.join(figFolder, "traces_%s.png"%runName)
    fig.savefig(figName)


        
        
        
