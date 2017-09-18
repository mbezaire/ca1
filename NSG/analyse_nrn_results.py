#!/usr/bin/python
# -*- coding: utf8 -*-
"""
analyses output of NSG simulation  (based on the NEURON version)
author: András Ecker, last update 06.2017
"""

import os
import shutil
import tarfile
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from plots import plot_LFP, plot_SDF, plot_raster

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])


def extract_tar(tarName, zipName, runName):
    """extract run specific results from NSG output file"""

    fName = os.path.join(basePath, tarName)
    with tarfile.open(fName, "r:gz") as tf:
        subdir_and_files = [tarinfo for tarinfo in tf.getmembers()
                            if tarinfo.name.startswith(os.path.join(".", zipName, "results", runName))]
        tf.extractall(members=subdir_and_files)
    
    # move zipName/results/runName to single directory (if exist it will delete and recreate)
    resultDir = os.path.join(basePath, runName)
    if os.path.isdir(resultDir):
        shutil.rmtree(resultDir)  
    shutil.move(os.path.join(basePath, zipName, "results", runName), resultDir)
    # delete empty zipName/results dir
    shutil.rmtree(os.path.join(basePath, zipName))


def helper_getcores(runName):
    """get number of processors used (for concatenating rasters)"""
    
    import re
    with open(os.path.join(basePath, runName, "runreceipt.txt")) as f:
        tmp = f.readlines()[0]  # get only the first line
        ncores = int(re.findall(r'\d+', tmp)[0])
    return ncores


def helper_simduration(runName):  
    """get specified duration of the simulation (only for figure xlims)"""
    
    import re
    with open(os.path.join(basePath, runName, "runreceipt.txt")) as f:
        for line in f:
            if "SimDuration" in line:
                simduration = int(re.findall(r'\d+', line)[0])
    return simduration
  
    
def analyse_lfp(runName):
    """PSD analysis of the saved LFP data"""
    
    # load in LFP from file
    t = []
    LFP = []
    with open(os.path.join(basePath, runName, "lfp.dat")) as f:
        for line in f:
            t.append(float(line.split()[0]))
            LFP.append(float(line.split()[1]))
    runTime = t[-1]  # from saved LFP
    simduration = helper_simduration(runName)  # from runreceipt (run specific metadata)
    assert runTime == float(simduration)
    
    # bandpass (5-10Hz) filter LFP
    fs = 1000./t[-1]*(len(t)-1)  # sampling frequency
    nyq = fs * 0.5
    # see more: https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.signal.butter.html
    b, a = signal.butter(3, [5/nyq, 10/nyq], btype="bandpass")
    #w, h = signal.freqz(b, a, worN=2000)
    #plt.plot((nyq/np.pi)*w, abs(h))
    filteredLFP = signal.filtfilt(b, a, LFP)   
    
    # PSD analysis
    # see more: http://docs.scipy.org/doc/scipy-dev/reference/generated/scipy.signal.welch.html
    f, Pxx = signal.welch(LFP, fs, window="hamming", nperseg=len(t)/2., scaling="spectrum")
    
    # plot results
    plot_LFP(t, LFP, filteredLFP, f, Pxx, runTime, runName)
    
    return runTime


def get_spikes(runName, numCores, runTime, plot_=True):
    """reads in PC spikes from the saved files"""
    
    # reads celltype.dat to get PC indicies
    with open(os.path.join(basePath, runName, "celltype.dat")) as f:
        for line in f:
            if line.split()[0] == "pyramidalcell":
                startID = int(line.split()[3])
                endID = int(line.split()[4])
    idx = np.r_[startID:endID+1]
    
    # reads spike times of PCs
    spikeTimes = []
    spikingNeurons = []
    rate = np.zeros((int(runTime)))  # hard coded for 1*ms binning
    for core in range(0, numCores):  # iterates over diff. files by diff. cores
        with open(os.path.join(basePath, runName, "spikeraster_%i.dat"%core)) as f:
        #with open(os.path.join(basePath, runName, "spikeraster.dat")) as f:  # for concatenated spikerasters...
            for line in f:
                if int(line.split()[1]) in idx:
                    spikeTime = float(line.split()[0])
                    spikeTimes.append(spikeTime)
                    spikingNeurons.append(int(line.split()[1]))
                    rate[int(spikeTime)] += 1
    rate = rate / (idx.shape[0] * 0.001)  # normalize rate
                   
    if len(spikingNeurons):
        print("PC spikes read from run: %s"%runName)
        if plot_:
            plot_raster(spikingNeurons, spikeTimes, runTime, startID, endID, runName)
    else:
        print("NO PC spikes in run: %s"%runName)
            
    return spikeTimes, spikingNeurons, rate


def analyse_rate(rate, runName):
    """same 'SDF'(smoothed rate) analysis as in Bezaire 2016"""
    
    # smooth rate: (this is not SDF as proposed in Szucs 1998, but just a Gaussian smoothing... - Andras)
    wGauss = signal.gaussian(11, std=3)  # std=3 from Bezaire paper
    # see more: https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.signal.convolve.html
    SDF = signal.convolve(rate, wGauss, mode="same") / sum(wGauss)
    
    # PSD analysis of "SDF"
    fs = 1000.  # hard coded for 1*ms binning
    # see more: http://docs.scipy.org/doc/scipy-dev/reference/generated/scipy.signal.welch.html
    f, Pxx = signal.welch(SDF, fs, window="hamming", nperseg=rate.shape[0]/2., scaling="spectrum")
    
    plot_SDF(SDF, f, Pxx, runName)


if __name__ == "__main__":

    tarName = "output.tar.gz"
    zipName = "CA1"
    runName = "best_mixed_fastconn_scale10"
       
    #extract_tar(tarName, zipName, runName)
    numCores = helper_getcores(runName)
    runTime = analyse_lfp(runName)
    _, _, rate = get_spikes(runName, numCores, runTime)
    if rate.any():
        analyse_rate(rate, runName)
    
    plt.show()
    
    
    
    
