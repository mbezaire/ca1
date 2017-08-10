#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Helper script to check network connectivity (based on the NeuroML version of the model)
"""

import pprint
# NeuroML specific libraries
import neuroml
import neuroml.loaders as loaders
# helper functions from other scripts
from GenerateHippocampalNet_oc import get_projdata


def check_projections(networkName, dSyns):
    """checks projections in the nml doc and compares with the config files"""

    # load in network
    nml_doc = loaders.NeuroMLLoader.load("%s.net.nml"%networkName)    
    
    # get size of the populations for normalization
    dPopsizes = {}
    for pop in nml_doc.networks[0].populations:
        cell_type = pop.id.split('_')[1]
        dPopsizes[cell_type] = pop.size
    
    out_ = []
    for proj in nml_doc.networks[0].projections:
        # get data from the network
        precell_type = proj.presynaptic_population.split('_')[1]
        postcell_type = proj.postsynaptic_population.split('_')[1]
        ncons_net = len(proj.connection_wds)/dPopsizes[postcell_type]
        # get data from the dictionary built from config files
        ncons_config = dSyns["proj_%spop_to_%spop"%(precell_type, postcell_type)]["ncons"]
        if ncons_net == ncons_config:
            out_.append("%s <- %s: %i connections (as specified)"%(postcell_type, precell_type, ncons_net))
        else:    
            out_.append("%s <- %s: %i connections (vs: %i specified)"%(postcell_type, precell_type, ncons_net, ncons_config))
    
    # oc generated networks have input lists for CA3, and EC stimulation   
    if nml_doc.networks[0].input_lists:
        for input_ in nml_doc.networks[0].input_lists:
            # get data from the network
            precell_type = input_.id.split('_')[1][:-3]
            postcell_type = input_.populations.split('_')[1]
            ncons_net = len(input_.input)/dPopsizes[postcell_type]
            # get data from the dictionary built from config files
            ncons_config = dSyns["proj_%spop_to_%spop"%(precell_type, postcell_type)]["ncons"]
            if ncons_net == ncons_config:
                out_.append("%s <- %s: %i connections (as specified)"%(postcell_type, precell_type, ncons_net))
            else:    
                out_.append("%s <- %s: %i connections (vs: %i specified)"%(postcell_type, precell_type, ncons_net, ncons_config))
                
    # print out results:
    out_.sort()
    pprint.pprint(out_)
        
        
if __name__ == "__main__":

    netName = "HippocampalNet_oc"
    # get data from spec. config files
    dSyns = get_projdata(connData=430, synData=120)
    
    check_projections(netName, dSyns) 
