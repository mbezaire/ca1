#!/usr/bin/python
# -*- coding: utf8 -*-
"""
analyses output of NSG simulation (based on the NeuroML version)
author: András Ecker, last update 09.2017
"""

import os
import re
import shutil
import tarfile
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from plots import plot_LFP, plot_SDF, plot_raster

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1])


def extract_tar(tarName):
    """extract run specific results from NSG output file"""

    fName = os.path.join(basePath, tarName)
    tf = tarfile.open(fName, "r:gz")
    scale = int(re.findall(r'\d+', tf.getmembers()[0].name)[1])  # get scale from dirname ([0] would be '1' -> because of 'CA1_*')
    zipName = "CA1_nml_scale%s"%scale
    
    subdir_and_files = [tarinfo for tarinfo in tf.getmembers()
                        if tarinfo.name.startswith(os.path.join(".", zipName, "network"))
                        or tarinfo.name == os.path.join(".", "stderr.txt") or tarinfo.name == os.path.join(".", "stdout.txt")]
    tf.extractall(members=subdir_and_files)
    tf.close()
    
    # move zipName/network to a new result directory (if exist it will delete and recreate)
    resultDir = os.path.join(basePath, "results_nml_scale%s"%scale)
    if os.path.isdir(resultDir):
        shutil.rmtree(resultDir)
    os.mkdir(resultDir)
    
    # move .dat files into separate directory (+ err and out files)
    for file_ in os.listdir(os.path.join(basePath, zipName, "network")):
        if file_.endswith(".dat"):  # you might extend this to keep net.nml or .xml files too !!!
            shutil.move(os.path.join(basePath, zipName, "network", file_), os.path.join(resultDir, file_))
    shutil.move(os.path.join(basePath, "stderr.txt"), os.path.join(resultDir, "stderr.txt"))
    shutil.move(os.path.join(basePath, "stdout.txt"), os.path.join(resultDir, "stdout.txt"))
    print("results moved to: %s"%resultDir)
            
    # delete remaining directory...
    shutil.rmtree(os.path.join(basePath, zipName))
       
    return scale, resultDir
    
    
if __name__ == "__main__":
        
    tarName = "output.tar.gz"
       
    scale, resultDir = extract_tar(tarName)
    
    
    
    
    
