#!/usr/bin/python
# -*- coding: utf8 -*-
"""
helper file (plotting PSD analysis, raster)
author: András Ecker, last update 06.2017
"""

import os
import numpy as np
import matplotlib.pyplot as plt

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])
figFolder = os.path.join(basePath, "figures")


def plot_LFP(t, LFP, filteredLFP, f, Pxx, runTime, runName):
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
    #ax.set_xlim([0, runTime])
    ax.set_xlim([50, runTime])
    ax.set_title("Local Field Potential of PCs")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("LFP (mV)")
    
    ax2 = fig.add_subplot(3,1,2)
    #ax2.plot(t, filteredLFP, "b-")
    ax2.plot(plotT, plotFilteredLFP, "r-")
    #ax2.set_xlim([0, runTime])
    ax2.set_xlim([50, runTime])
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
    
    runTime = SDF.shape[0]
    t = np.linspace(1, runTime, runTime)
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
    #ax.set_xlim([0, runTime])
    ax.set_xlim([50, runTime])
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


def plot_raster(spikingNeurons, spikeTimes, runTime, startID, endID, runName):
    """raster plot"""
    
    fig = plt.figure(figsize=(10, 8))
        
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(spikeTimes, spikingNeurons, c="blue", marker='.')
    ax.set_title("PC raster")
    if runTime > 1000:
        ax.set_xlim([runTime/2-500, runTime/2+500,])
    else:
        ax.set_xlim([0, runTime])
    ax.set_xlabel("Time (ms)")
    ax.set_ylim([startID, endID])
    ax.set_ylabel("Neuron number")
    
    figName = os.path.join(figFolder, "raster_%s.png"%runName)
    fig.savefig(figName)
        
        
        
