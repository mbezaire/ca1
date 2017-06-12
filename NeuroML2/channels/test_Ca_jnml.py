import sys
from pyneuroml import pynml


lems_file = 'LEMS_test_Ca.xml'

results = pynml.run_lems_with_jneuroml(lems_file, max_memory='2G', nogui=True, load_saved_data=True)

if not '-nogui' in sys.argv:
    
    from pylab import plot, show, figure, title

    for key in results.keys():
        if key != 't':
            figure()
            plot(results['t'], results[key], label="jNeuroML: "+key, color="g")
            title(key)

    show()
