import sys
from pyneuroml import pynml

cell = sys.argv[1]

print("Comparing behaviour of cell %s to original NEURON code"%cell)

orig_dat = '../%s.soma.dat'%cell
orig_results, indices = pynml.reload_standard_dat_file(orig_dat)
print("Reloaded NEURON data: %s"%orig_results.keys())

results = pynml.run_lems_with_jneuroml_neuron('LEMS_%s.xml'%cell, nogui=True, load_saved_data=True)

print("Reloaded data: %s"%results.keys())

xs = []
ys = []
labels = []

xs.append([t*1000 for t in results['t']])
ys.append([v*1000 for v in results['Pop_%scell/0/%scell/v'%(cell,cell)]])
labels.append('jNeuroML_NEURON')

xs.append(orig_results['t'])
ys.append(orig_results[0])
labels.append('NEURON')



pynml.generate_plot(xs,ys,'Plot of %s'%cell,labels=labels)
