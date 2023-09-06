#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Runs jNeuroML and plots membrane potential, [Ca++]_i and single channel currents (to compare Ca++ dynamics)
Authors: András Ecker, Padraig Gleeson, last update: 11.2017
"""

import sys
from pyneuroml import pynml

results = pynml.run_lems_with_jneuroml_neuron("LEMS_test_Ca.xml", nogui=True, load_saved_data=True)

if not '-nogui' in sys.argv:
    
    from pylab import plot, show, figure, title

    for key in results.keys():
        if key != 't':
            figure()
            plot(results['t'], results[key], label="jNeuroML: "+key, color="g")
            title(key)

    show()
