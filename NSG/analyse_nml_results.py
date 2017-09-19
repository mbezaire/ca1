#!/usr/bin/python
# -*- coding: utf8 -*-
"""
analyses output of NSG simulation (based on the NeuroML version)
author: András Ecker, last update 09.2017
"""

import os
import re
import sys
import shutil
import tarfile
#import numpy as np
#import matplotlib.pyplot as plt
basePath = os.path.sep.join(os.path.abspath('__file__').split(os.path.sep)[:-2])
# add the 'network' directory to the path (import the modules)
sys.path.insert(0, os.path.sep.join([basePath, "NeuroML2", "network"]))
from analyse_PING import get_traces, get_spikes
from plots import plot_SDF, plot_raster

NSGbasePath = os.path.join(basePath, "NSG")


def extract_tar(tarName):
    """extract run specific results from NSG output file"""

    fName = os.path.join(NSGbasePath, tarName)
    tf = tarfile.open(fName, "r:gz")
    scale = int(re.findall(r'\d+', tf.getmembers()[0].name)[1])  # get scale from dirname ([0] would be '1' -> because of 'CA1_*')
    zipName = "CA1_nml_scale%s"%scale
    
    subdir_and_files = [tarinfo for tarinfo in tf.getmembers()
                        if tarinfo.name.startswith(os.path.join(".", zipName, "network"))
                        or tarinfo.name == os.path.join(".", "stderr.txt") or tarinfo.name == os.path.join(".", "stdout.txt")]
    tf.extractall(members=subdir_and_files)
    tf.close()
    
    # move zipName/network to a new result directory (if exist it will delete and recreate)
    resultDir = os.path.join(NSGbasePath, "results_nml_scale%s"%scale)
    if os.path.isdir(resultDir):
        shutil.rmtree(resultDir)
    os.mkdir(resultDir)
    
    # move .dat files into separate directory (+ popsize, err and out files)
    for file_ in os.listdir(os.path.join(NSGbasePath, zipName, "network")):
        if file_.endswith(".dat"):  # you might extend this to keep net.nml or .xml files too !!!
            shutil.move(os.path.join(NSGbasePath, zipName, "network", file_), os.path.join(resultDir, file_))
    shutil.move(os.path.join(NSGbasePath, "popsize_scale%s.txt"%scale), os.path.join(resultDir, "popsize_scale%s.txt"%scale))
    shutil.move(os.path.join(NSGbasePath, "stderr.txt"), os.path.join(resultDir, "stderr.txt"))
    shutil.move(os.path.join(NSGbasePath, "stdout.txt"), os.path.join(resultDir, "stdout.txt"))
    print("results moved to: %s"%resultDir)
            
    # delete remaining directory...
    shutil.rmtree(os.path.join(NSGbasePath, zipName))
       
    return scale, resultDir


def get_simduration_dt(resultDir):
    """reads stdout.txt (console output saved by NSG) and finds run specific info(s)"""
    
    fName = os.path.join(resultDir, "stdout.txt")
    with open(fName) as f:
        line = f.readlines()[1]
        
    simduration = float(re.findall(r'\d+\.\d+', line)[0])
    dt = float(re.findall(r'\d+\.\d+', line)[1])
    print(">>> NetPyNE based simulation for %.1fms (dt: %.2fms)"%(simduration, dt))
    
    return simduration, dt


def get_popsize(resultDir, scale):
    """read popsize data"""

    dPops = {}
    fName = os.path.join(resultDir, "popsize_scale%s.txt"%scale)
    with open(fName, "r") as f:
        next(f)  # skip header
        for line in f:
            if "(stim)" not in line:
                cell_type = re.search(r'\_(.*)\:', line).group(1)
                ncells = int(re.findall(r'\d+', line)[0])
                dPops[cell_type] = ncells
                
    return dPops
                
    
if __name__ == "__main__":
    
    # untar results
    tarName = "output.tar.gz"       
    #scale, resultDir = extract_tar(tarName)    
    scale = 2500
    resultDir = os.path.join(NSGbasePath, "results_nml_scale%s"%scale)
    print("scale = %s"%scale)
    
    # get runspecific data
    simduration, dt = get_simduration_dt(resultDir)
    dPops = get_popsize(resultDir, scale)
    
    # load in traces, search spikes  #TODO: update this after fixing NetPyNE on NSG!
    dTraces = {}; dSpikeTimes = {}; dSpikingNeurons = {}
    for cell_type, ncells in dPops.iteritems():
        fName = os.path.join(resultDir, "Sim_HippocampalNet_scale%s_oc.pop_%s.v.dat"%(scale, cell_type))
        t, traces = get_traces(fName, simduration, dt, ncells)
        spikeTimes, spikingNeurons = get_spikes(t, traces)    
        dTraces[cell_type] = traces; dSpikeTimes[cell_type] = spikeTimes; dSpikingNeurons[cell_type] = spikingNeurons
    print("traces read from files, spikes read from traces")
    
    
    
    
