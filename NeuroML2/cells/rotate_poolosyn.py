# -*- coding: utf-8 -*-
""" 
    Rotates poolosyncell (just to be consistent with the other cells -> will look better on OSB):
    Authors: András Ecker, Padraig Gleeson
"""

import neuroml
import neuroml.loaders as loaders
import neuroml.writers as writers

orig_nml_file = "poolosyn_orig_unrotated.cell.nml"
doc = loaders.NeuroMLLoader.load(orig_nml_file)
print("Loaded morphology file from: " + orig_nml_file)

# iterating over segments and changeing x and y coordinates 
for seg in doc.cells[0].morphology.segments:
    if seg.proximal:
        prox = [seg.proximal.x, seg.proximal.y, seg.proximal.z]
        seg.proximal.x = prox[1]; seg.proximal.y = prox[0]
    dist = [seg.distal.x, seg.distal.y, seg.distal.z]    
    seg.distal.x = dist[1]; seg.distal.y = dist[0]
    

nml_file = "poolosyn.cell.nml"
writers.NeuroMLWriter.write(doc,nml_file)
print("Saved modified morphology file to: " + nml_file)