#!/usr/bin/python
# -*- coding: utf8 -*-
"""
creates .zip archive from the necessary files, (and sends job to NSG REST API)
note: Scale = 300 -> ~ 1100 PCs, 5s: takes ~ 1.2h on 1 node and 24 cores (Comet NEURON 7.4)
author: András Ecker, last update 08.2017
"""

import os
import shutil
import zipfile

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
nmlFolder = os.path.join(basePath, "NeuroML2")


def create_zip(zipName, runName, networkName, copysyn=False, rm=True):
    """copies the necessary files to a subfolder and zips it afterwards (NSG prefered way)"""
    
    # create directory (if exist it will delete and recreate)
    mainDirName = os.path.join(basePath, "NSG", zipName)
    if os.path.isdir(mainDirName):
        shutil.rmtree(mainDirName)
    os.mkdir(mainDirName)
    
    # cp channels
    os.mkdir(os.path.join(mainDirName, "channels"))
    for file_ in os.listdir(os.path.join(nmlFolder, "channels")):
        if file_.endswith(".channel.nml") or file_ == "Capool.nml":
            shutil.copy2(os.path.join(nmlFolder, "channels", file_), os.path.join(mainDirName, "channels", file_))            
    # cp cells
    os.mkdir(os.path.join(mainDirName, "cells"))
    for file_ in os.listdir(os.path.join(nmlFolder, "cells")):
        if file_.endswith(".cell.nml"):
            shutil.copy2(os.path.join(nmlFolder, "cells", file_), os.path.join(mainDirName, "cells", file_))
    # cp synapses
    if copysyn:   # only for regenerated network (the one generated from scratch in oc. has the synapses inside the .net.nml file)    
        os.mkdir(os.path.join(mainDirName, "synapses"))
        shutil.copy2(os.path.join(nmlFolder, "synapses", "exp2Synapses.synapse.nml"),
                     os.path.join(mainDirName, "synapses", "exp2Synapses.synapse.nml"))
        shutil.copy2(os.path.join(nmlFolder, "synapses", "customGABASynapses.synapse.nml"),
                     os.path.join(mainDirName, "synapses", "customGABASynapses.synapse.nml")) 
    # cp network and LEMS file
    os.mkdir(os.path.join(mainDirName, "network"))
    shutil.copy2(os.path.join(nmlFolder, "network", "%s.net.nml"%networkName),
                 os.path.join(mainDirName, "network", "%s.net.nml"%networkName))
    shutil.copy2(os.path.join(nmlFolder, "network", "LEMS_%s.xml"%networkName),
                 os.path.join(mainDirName, "network", "LEMS_%s.xml"%networkName))
    
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
    
    print("zip file created: %s.zip"%mainDirName)


if __name__ == "__main__":

    zipName = "CA1"
    runName = "new_repeatconn"
    networkName = "HippocampalNet_scale100000_oc"
    
    create_zip(zipName, runName, networkName,
               copysyn=False, rm=True)
    
    
    

