#!/usr/bin/python
# -*- coding: utf8 -*-
"""
reproduces Figure 3 C,D from Bezaire et al. 2016
author: András Ecker, last update 08.2017
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from analyse_results import helper_getcores, helper_simduration
from plots import plot_rasters

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])


def helper_getcelltype(cell_name):  # same as in ../NeuroML2/network/GenerateHippocampalNet_oc.py
    """helper function to process config files"""
    if cell_name == "pyramidalcell":
        return "poolosyn"
    else:
        return cell_name[:-4]


def get_spikes(runName, numCores):
    """reads in spikes from the saved files"""
    
    dIDx = {}
    dSpikeTimes = {}
    dSpikingNeurons = {}
    
    # reads celltype.dat to get PC indicies
    with open(os.path.join(basePath, runName, "celltype.dat")) as f:
        next(f)  # skip header
        lastID = 0
        for line in f:
            cell_type = helper_getcelltype(line.split()[0])           
            if cell_type not in ["ca3", "ec"]:  # no stimulating cells
                startID = int(line.split()[3])
                endID = int(line.split()[4])
                dIDx[cell_type] = np.r_[startID:endID+1]
                # init containers for the next part
                dSpikeTimes[cell_type] = []
                dSpikingNeurons[cell_type] = []
                if endID > lastID:  # just to store the last, not stimulating cell ID
                    lastID = endID
    
    # read in spike times
    for core in range(0, numCores):  # iterates over diff. files by diff. cores
        with open(os.path.join(basePath, runName, "spikeraster_%i.dat"%core)) as f:
        #with open(os.path.join(basePath, runName, "spikeraster.dat")) as f:  # for concatenated spikerasters...
            for line in f:
                spikingNeuron = int(line.split()[1])
                if spikingNeuron < lastID:  # not stim. cell
                    spikeTime = float(line.split()[0])
                    for cell_type, idx in dIDx.iteritems():
                        if spikingNeuron in idx:
                            dSpikeTimes[cell_type].append(spikeTime)
                            dSpikingNeurons[cell_type].append(spikingNeuron)
                   
    if len(dSpikingNeurons["poolosyn"]):
        print("spikes read from run: %s"%runName)
    else:
        print("NO PC spikes in run: %s"%runName)
            
    return dSpikeTimes, dSpikingNeurons
     
    
if __name__ == "__main__":

    #runName = "4s_10Hz"
    runName = "best_mixed_fastconn_scale10"
       
    numCores = helper_getcores(runName)
    simduration = helper_simduration(runName)
    dSpikeTimes, dSpikingNeurons = get_spikes(runName, numCores)
    
    plot_rasters(dSpikeTimes, dSpikingNeurons, simduration, runName)
    plt.show()
    
