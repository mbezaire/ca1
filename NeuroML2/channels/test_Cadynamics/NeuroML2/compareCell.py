import sys
from pyneuroml import pynml
import matplotlib.pyplot as plt


print("Comparing behaviour of cell to original NEURON code")

orig_dat = '../NEURON/nrn_ca.dat'
orig_results, indices = pynml.reload_standard_dat_file(orig_dat)
print("Reloaded NEURON data: %s"%orig_results.keys())

results = pynml.run_lems_with_jneuroml_neuron('LEMS_test_Ca.xml', nogui=True, load_saved_data=True)

print("Reloaded data: %s"%results.keys())

comp = {}
comp['v'] = ('pop/0/cell1/v',0)
comp['[Ca2+]'] = ('pop/0/cell1/caConc',1)
comp['iCa_CavL'] = ('pop/0/cell1/biophysicalProperties/membraneProperties/CavL_all/iDensity',3)
comp['iCa_CavN'] = ('pop/0/cell1/biophysicalProperties/membraneProperties/CavN_all/iDensity',4)

for var in comp.keys():
    lems, nrn = comp[var]
    xs = []
    ys = []
    labels = []

    xs.append([t*1000 for t in results['t']])
    factor = 1
    if var=='v': factor = 1000         #  1 V = 1000.0 mV
    if var=='iCa_CavL': factor = .1  #  1 A_per_m2 = 0.1 mA_per_cm2
    if var=='iCa_CavN': factor = .1  #  1 A_per_m2 = 0.1 mA_per_cm2
    ys.append([v*factor for v in results[lems]])
    labels.append('jNeuroML_NEURON')

    xs.append(orig_results['t'])
    ys.append(orig_results[nrn])
    labels.append('NEURON')

    pynml.generate_plot(xs,ys,'Plot of %s'%var,labels=labels, show_plot_already=False)

plt.show()
    

