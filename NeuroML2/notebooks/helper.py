#!/usr/bin/python
# -*- coding: utf8 -*-
"""
helper file to call pyneuroml functions and visualize results - for cleaner notebooks
author: András Ecker last update 07.2017
"""

import os
import re
import numpy as np
import matplotlib.pyplot as plt

basePath = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])


def input_currents(cell_file, custom_amps_nA, analysis_duration, pre_zero_pulse, post_zero_pulse, verbose=False):
    """
    injects specified currents to NeuroML cell, using pyneuroml
    :param celltype: string - name of the cell
    :param custom_amps_nA: list of input currents in nA
    :param analysis_duration: int - simulation duration in ms
    :param pre_zero_pulse: int - offset of input current(s) in ms
    :param post_zero_pulse: int - simulated time after the input in ms
    :param verbose: verbose output
    """
    from pyneuroml.analysis import generate_current_vs_frequency_curve
    
    tmp = re.match(r"../cells/(.*).cell.nml", cell_file)  # hard coded for path-sep: "/" (linux, mac)
    cell_id = tmp.group(1)+"cell"
    
    if verbose:
        print("Running input_currents() on %s, cell_id=%s"%(cell_file, cell_id))

    curve = generate_current_vs_frequency_curve(cell_file,
                                                cell_id,
                                                custom_amps_nA=custom_amps_nA,
                                                analysis_duration=analysis_duration,
                                                pre_zero_pulse=pre_zero_pulse,
                                                post_zero_pulse=post_zero_pulse,
                                                analysis_delay=0,
                                                dt=0.001,
                                                simulator="jNeuroML_NEURON",
                                                plot_voltage_traces=True,
                                                plot_if=False,
                                                plot_iv=False,
                                                temperature="34degC",
                                                title_above_plot=True,
                                                save_voltage_traces_to="figures/%s_traces.png"%cell_id,
                                                verbose=verbose)
    
def fI_curve(cell_file):
    """
    injects different currents to NeuroML cell and calculates f-I curve, using pyneuroml
    :param celltype: string - name of the cell
    """
    from pyneuroml.analysis import generate_current_vs_frequency_curve
    
    tmp = re.match(r"../cells/(.*).cell.nml", cell_file)  # hard coded for path-sep: "/" (linux, mac)
    cell_id = tmp.group(1)+"cell"

    curve = generate_current_vs_frequency_curve(cell_file,
                                                cell_id,
                                                start_amp_nA=-0.1, 
                                                end_amp_nA=0.4, 
                                                step_nA=0.02, 
                                                analysis_duration=1000,
                                                pre_zero_pulse=0,
                                                post_zero_pulse=0,
                                                analysis_delay=100,
                                                dt=0.005,
                                                simulator="jNeuroML_NEURON",
                                                plot_voltage_traces=False,
                                                plot_if=True,
                                                plot_iv=False,
                                                temperature="34degC",
                                                title_above_plot=True,
                                                save_if_figure_to="figures/%s_fI.png"%cell_id)


def get_data_from_datfile(fName):
    """helper function to load in dat files"""
    
    data = []
    with open(fName) as f:
        for line in f:
            data.append(line.split()[1])          
    return data


def get_chan_variables():
    """helper function to get channel variables from channel name (stored in a dictionary)"""
    
    channels = {"Nav":["m", "h"], "Navbis":["m", "h"], "Navcck":["m", "h"], "Navaxonp":["m", "h"],
                "Navngf":["m", "h"], "Navp":["m", "h", "s"], "Navapicalp":["m", "h", "s"],
                "Kdrslow":["n"], "Kdrfast":["n"], "Kdrp":["n"], "Kdrfastngf":["n"],
                "KvAolm":["a", "b"], "KvA":["n", "l"], "KvAproxp":["n", "l"], "KvAdistp":["n", "l"],
                "KvAngf":["n", "l"], "KvGroup":["n"], "KvCaB":["o"],
                "CavN":["c", "d"],
                "HCNolm":["r"], "HCN":["h"], "HCNp":["l"], "HCNsomap":["l"]}  # very hard coded!
    return channels


def plot_inf(channel_list):
    """plots inf (or steady state) variable of channels, specified in the input list"""
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1)
       
    channels = get_chan_variables()
    for channel in channel_list:  # iterate over diff. chans
        assert channel in channels, "%s not available. Check spelling!"%channel
        for variable in channels[channel]:  # iterate over diff. variables within a single channel
            fName = os.path.join(basePath, "NeuroML2", "channels", "%s.%s.inf.lems.dat"%(channel, variable))
            data = get_data_from_datfile(fName)            
            v = np.linspace(-100, 100, len(data)) # shouldn't be recalculated every time            
            ax.plot(v, data, label="%s '%s'"%(channel, variable))
    
    ax.set_title("Steady state varibale of channel(s)")
    ax.set_xlabel("V (mV)")
    ax.set_xlim([-100, 100])
    ax.set_ylabel("inf - steady state")
    ax.set_ylim([0, 1])
    ax.legend()    
    fig.savefig("steady_state.png")


def plot_tau(channel_list):
    """plots tau variable of channels, specified in the input list"""
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1, 1, 1)
       
    channels = get_chan_variables()
    for channel in channel_list:  # iterate over diff. chans
        assert channel in channels, "%s not available. Check spelling!"%channel
        for variable in channels[channel]:  # iterate over diff. variables within a single channel
            fName = os.path.join(basePath, "NeuroML2", "channels", "%s.%s.tau.lems.dat"%(channel, variable))
            data = get_data_from_datfile(fName)            
            v = np.linspace(-100, 100, len(data)) # shouldn't be recalculated every time            
            ax.plot(v, data, label="%s '%s'"%(channel, variable))
    
    ax.set_title("Steady state varibale of channel(s)")
    ax.set_xlabel("V (mV)")
    ax.set_xlim([-100, 100])
    ax.set_ylabel("tau (ms)")
    ax.legend()    
    fig.savefig("tau.png")
    



    
