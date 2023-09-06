#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Helper script to export cells from .hoc template to NeuroML2. Mostly used to export morphology, the bioph. props. (usually) have to be updated manually"""

from pyneuroml.neuron import export_to_neuroml2

cells = ['axoaxonic', 'bistratified', 'cck', 'cutsuridis', 'ivy', 'ngf', 'olm', 'poolosyn', 'pvbasket', 'sca']


for cell in cells:

    export_to_neuroml2("%s.hoc"%cell, 
                       "cells/%s.cell.nml"%cell, 
                       includeBiophysicalProperties=True,
                       known_rev_potentials={'ch_CavL':-1, 'ch_CavN':-1, 'ch_HCNolm':-30})

    print "##### %s done #####"%cell



