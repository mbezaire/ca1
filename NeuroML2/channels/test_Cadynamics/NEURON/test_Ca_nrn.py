#!/usr/bin/ipython -i

from neuron import *
from nrn import *
#from neuron import gui


def create_comp(name = 'soma'):
    
    comp = h.Section('soma')
    
    comp.insert('iconc_Ca')
    comp.catau_iconc_Ca = 9

    #comp.insert('ica_clamp')    

    comp.insert('ch_CavL')
    comp.gmax_ch_CavL = 15e-3

    comp.insert('ch_CavN')
    comp.gmax_ch_CavN = 5e-3

    comp.insert('ch_KvCaB')
    comp.gmax_ch_KvCaB = 10e-3
    comp.ek = -90

    comp.nseg = 1
    comp.L = 10
    comp.diam = 1
    
    comp.insert('pas')
    comp(0.5).g_pas = 3e-4 # S/cm2
    comp(0.5).e_pas = -65

    h.cao0_ca_ion = 2
    h.cai0_ca_ion = 5e-5

    h.celsius = 34

    return comp

    
def plot_timeseries(vdict, varlist):
    from pylab import plot, show, figure, title
    t = vdict['t']
    for n in varlist:
        figure()
        plot(t, vdict[n], label=n, color='r')
        title(n)
    
    show()

def create_dumps(section, varlist):
    recordings = {n: h.Vector() for n in varlist}

    for (vn, v) in recordings.iteritems():
        v.record(section(0.5).__getattribute__('_ref_' + vn))
    
    recordings['t'] = h.Vector()
    recordings['t'].record(h._ref_t)
    return recordings 


def dump_to_file(vdict, varlist, fname='nrn_ca.dat'):
    from numpy import savetxt, array

    vnames = ['t'] + varlist
    X = array([vdict[x].to_python() for x in vnames]).T
    savetxt(fname, X)


def run(tstop=10, dt=0.001):
    h.dt = dt
    h.finitialize(-65)
    h.fcurrent()
    h.frecord_init()
    while h.t < tstop:
        h.fadvance()



comp = create_comp('soma')

stim = h.IClamp(0.5, sec=comp)
stim.delay = 40
stim.dur = 120
stim.amp = 0.01

varlist = ['v', 'cai', 'ica']
ds = create_dumps(comp, varlist)

run(200, 0.001)

plot_timeseries(ds, varlist)
dump_to_file(ds, varlist)
