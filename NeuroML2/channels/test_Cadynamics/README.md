#### Compare Ca++ dynamics of .mod files and .nml version:

    cd NeuroML2/channels/test_Cadynamics/NEURON
    nrnivmodl ../../../../
    python test_Ca_nrn.py
    cd ../NeuroML2
    python test_Ca_jnml.py  # or python compareCell.py
