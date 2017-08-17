## NeuroML2 version of the model

The network was originally developed in [NEURON](https://www.neuron.yale.edu/neuron/) and all the (necessary) files got converted to [NeuroML](https://www.neuroml.org/neuromlv2). In the new version the model transparency imporved, by which we aimed to facilitate reusability! The NeuroML version allows testing in a standardized, continuous way by [omv](https://github.com/OpenSourceBrain/osb-model-validation) and clean and easy modifications.

#### Using the NeuroML 2 models
**Installation**

Install [jNeuroML](https://github.com/NeuroML/jNeuroML). *Installation from source is recommended, using the latest development version, i.e.:*

    git clone git://github.com/NeuroML/jNeuroML.git neuroml_dev/jNeuroML
    cd neuroml_dev/jNeuroML
    python getNeuroML.py development
    
Ensure the `jnml` executable is present on your PATH.

Clone this repo:

    git clone https://github.com/mbezaire/ca1.git

**channels**

To see the converted channel files, and the comparison to the original ones, click [here](https://github.com/mbezaire/ca1/tree/development/NeuroML2/channels)

**cell models**

Individual cells are illustrated in jupyter notebooks. To run the notebooks and learn more about the cell models install [pyNeuroML](https://github.com/NeuroML/pyNeuroML) and run:

    cd ca1/NeuroML2/notebooks
    jupyter notebook

> See more [here](https://github.com/mbezaire/ca1/tree/development/NeuroML2/notebooks)
  
**networks**

To be able to rebuild the networks install [OpenCortex](https://github.com/OpenSourceBrain/OpenCortex) and run:

    cd ca1/NeuroML2/netwok
    python GenerateHippocampalNet_oc.py 100000  # builds a scaled down (to 100000) network
    
or just skip this step and use the provided example (also scaled down to 100000) and run:

    jnml LEMS_HippocampalNetwork_scale100000_oc.xml -neuron -run  # run with NERUON (you will need NEURON installed) 
    
Want to run paralell? NetPyNE is a NeuroML friendly NEURON parallelization package which does the work under the hood.
You just have to install [NetPyNE](https://github.com/Neurosim-lab/netpyne) and run:

    jnml LEMS_HippocampalNetwork_scale100000_oc.xml -netpyne -np -4  # will run on 4 cores

> See more [here](https://github.com/mbezaire/ca1/tree/master/NeuroML2/network)

The **CA1 network model** got converted as part of a [Google Summer of Code 2017](https://developers.google.com/open-source/gsoc/) project, with [INCF](https://www.incf.org/) by András Ecker and Padraig Gleeson

> For further support please contact: ecker.andris@gmail.com, or just open an issue!

