#!/usr/bin/python
# -*- coding: utf8 -*-
"""
creates .zip archive from the necessary files, (and sends job to NSG REST API)
note: Scale = 300 -> ~ 1100 PCs, 5s: takes ~ 1.2h on 1 node and 24 cores (Comet NEURON 7.4)
author: András Ecker, last update 06.2017
"""

import os
import shutil
import zipfile

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])


def create_zip(zipName, runName="TestRun", simDuration=100, rm=True,
               scale=300, numData=101, connData=430, synData=120, rateP=0.65):
    """copies the necessary files to a subfolder and zips it afterwards (NSG prefered way)"""
    
    # create directory (if exist it will delete and recreate)
    mainDirName = os.path.join(basePath, "NSG", zipName)
    if os.path.isdir(mainDirName):
        shutil.rmtree(mainDirName)
    os.mkdir(mainDirName)
    
    # cp hoc and mod files (root folder)
    for file_ in os.listdir(basePath):
        if file_.endswith(".mod") or file_.endswith(".hoc"):
            shutil.copy2(os.path.join(basePath, file_), os.path.join(mainDirName, file_))
    # cp cell templates
    path_ = os.path.join(basePath, "cells")
    shutil.copytree(path_, os.path.join(mainDirName, "cells"))
    # cp connectivity
    path_ = os.path.join(basePath, "connectivity")
    shutil.copytree(path_, os.path.join(mainDirName, "connectivity"))
    # cp selected files from datasets
    os.mkdir(os.path.join(mainDirName, "datasets"))
    shutil.copy2(os.path.join(basePath, "datasets", "cellnumbers_%i.dat"%numData),
                 os.path.join(mainDirName, "datasets", "cellnumbers_%i.dat"%numData))
    shutil.copy2(os.path.join(basePath, "datasets", "conndata_%i.dat"%connData),
                 os.path.join(mainDirName, "datasets", "conndata_%i.dat"%connData))
    shutil.copy2(os.path.join(basePath, "datasets", "syndata_%i.dat"%synData),
                 os.path.join(mainDirName, "datasets", "syndata_%i.dat"%synData))
    # create results folder (quick and dirty way to zip empty directory...)
    os.mkdir(os.path.join(mainDirName, "results"))
    with open(os.path.join(mainDirName, "results", "placeholder.txt"), "w") as f:
        f.write("hacky placeholder to make sure, that results dir gets zipped...")
    # cp setupfiles
    path_ = os.path.join(basePath, "setupfiles")
    shutil.copytree(path_, os.path.join(mainDirName, "setupfiles"))
    # cp stimulation
    path_ = os.path.join(basePath, "stimulation")
    shutil.copytree(path_, os.path.join(mainDirName, "stimulation"))
            
    # set parameters (insted of specifying them from command line)
    fName = os.path.join(mainDirName, "setupfiles", "parameters.hoc")
    with open(fName+"_tmp", "w") as outf:
        with open(fName, "r") as f:
            for line in f:
                if "RunName" in line:
                    outf.write('default_var("RunName","%s")\n'%runName)
                if "Connectivity" in line:
                    outf.write('default_var("Connectivity","try_all_repeatstim")\n')  # allows multiple connection from save precell to postcell (usefull for the downscaled version)
                elif "Scale" in line:
                    outf.write('default_var("Scale",%i)\n'%scale)
                elif "SimDuration" in line:
                    outf.write('default_var("SimDuration",%i)\n'%simDuration)
                elif "NumData" in line:
                    outf.write('default_var("NumData",%i)\n'%numData)
                elif "ConnData" in line:
                    outf.write('default_var("ConnData",%i)\n'%connData)
                elif "SynData" in line:
                    outf.write('default_var("SynData",%i)\n'%synData)
                elif "DegreeStim" in line:
                    outf.write('default_var("DegreeStim",%f)\n'%rateP)  # rate of the input Poisson proc.
                else:
                    outf.write(line)
                # note: JobHours is set to 4, which might be changed for bigger simulations...
    os.remove(fName)
    shutil.move(fName+"_tmp", fName)
    
    # rename main.hoc to init.hoc
    shutil.move(os.path.join(mainDirName, "main.hoc"), os.path.join(mainDirName, "init.hoc"))
    
    # zip created directory (shutils.make_archive won't work here...)
    zf = zipfile.ZipFile(mainDirName+".zip", "w")
    for root, subfolders, files in os.walk(mainDirName):
        for file_ in files:
            fName = os.path.join(root, file_)
            arcName = os.path.join(os.path.relpath(root, os.path.join(basePath, "NSG")), file_)
            zf.write(fName, arcName)
    zf.close()  

    if rm: # remove directory (and keep only the .zip file)
        shutil.rmtree(mainDirName)
    
    print("zip file created: %s"%mainDirName+".zip")


if __name__ == "__main__":

    zipName = "CA1"
    runName = "repeatconn"
    simDuration = 2e3  # ms
    create_zip(zipName, runName=runName, simDuration=simDuration, rm=False)
    
    
    

