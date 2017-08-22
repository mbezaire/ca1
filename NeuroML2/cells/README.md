### NeuroML2 cells

This repo host the NeuroML2 cell models and tests linked to [omv](https://github.com/OpenSourceBrain/osb-model-validation). To see more about the properties of individual cell models, go to the [notebooks folder](https://github.com/mbezaire/ca1/tree/development/NeuroML2/notebooks).

To visualize cell morphologies alongside each other install [povray](http://www.povray.org/) and run:

    pynml-povray visualize_cells.net.nml -scalez 350 -mindiam 1.5
    povray Antialias=On Antialias_Depth=10 Antialias_Threshold=0.1 +W1200 +H900 visualize_cells.net.nml.pov
