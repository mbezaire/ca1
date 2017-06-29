ca1: a NEURON network model
########################################

ca1 is a large-scale, detailed, biologically constrained NEURON network model of the rodent hippocampal CA1 area.

.. contents::

.. section-numbering::



Main features
=============

* Linux, Mac OS X and Windows support
* Documentation

Documentation
============
Full documentation is available `here <http://ca1.readthedocs.io/en/latest/>`_.


Installation
============


macOS
-----


On macOS, ca1 code can be installed via `Homebrew <http://brew.sh/>`_
(recommended):

.. code-block:: bash

    $ brew install ...


A MacPorts *port* is also available:

.. code-block:: bash

    $ port install ...

Linux
-----

.. code-block:: bash

    # Debian, Ubuntu, etc. using Docker
    $ apt-get install ....

.. code-block:: bash

    # FDebian, Ubuntu, etc.  manual install
    $ yum install ...


Windows, etc.
-------------

A universal installation method (that works on Windows, Mac OS X, Linux, …,
and always provides the latest version) is to use `pip`_:


.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools

    $ pip install --upgrade ...


(If ``pip`` installation fails for some reason, you can try
``easy_install ...`` as a fallback.)


Usage
=====


Scaled-down model:


.. code-block:: bash

    $ nrngui main.hoc # Runs a network at scale 1:10000 for 100 ms to ensure all works
    
    # OR
    
    $ nrngui -c "SimDuration=600" main.hoc -c "quit()" # Runs a network at scale 1:10000 for 600 ms, long enough to see theta emerge
    
    # OR

    $ nrngui -nopython ... # if there is no python installed
    
    # OR

    $ nrniv ... # if using without a GUI popup (depends on your NEURON installation; sometimes nrngui must be invoked to ensure all necessary libraries are loaded when NEURON launches)

Synopsis:

.. code-block:: bash

    $ nrngui [-c parameters] [main.hoc file]  -c "quit()"  # adding the quit() command after ensures the code stops immediately after an error


See also ``nrngui help``.


Examples
--------

Scaled down model to run directly on a personal computer:

.. code-block:: bash

    $ nrngui main.hoc # Runs a network at scale 1:10000 for 100 ms to ensure all works
    
    # OR
    
    $ nrngui -c "Scale=1000" -c "SimDuration=600" main.hoc -c "quit()" # Runs a network at scale 1:1000 (will take a long time) for 600 ms, long enough to see theta emerge
    
    # OR

    $ nrngui -nopython -c "SimDuration=1000"  -c "ConnData=446" main.hoc -c "quit()" # try a different connectivity configuration and a longer simulation with the default Scale of 1:10000, use the nopython flag if NEURON has errors due to not finding the site module, etc.
    
    # OR
    
    $ nrngui -c "Scale=1" main.hoc -c "quit()" # run a full scale network - this is not feasible for the ca1 network on a personal computer, but could be used for tiny networks such as ringdemo.
    

On a supercomputer, after creating a submission jobscript and moving to the model repository directory, enter:


.. code-block:: bash

    $ sbatch ./jobscripts/MyTestRun.sh
    
    # OR

    $ qsub ./jobscripts/MyTestRun.sh
    
According to the batch queueing software used by the computer. Or, use SimTracker to create the jobscript, export the script, code, and parameter sets to the supercomputer, and submit the job request to the queue.

Environment variables
=======

You may wish to set...

In your ``~/.bash_profile``:

.. code-block:: bash

 export N=samplesample
 export NEURONHOME=samplesample
 export PYTHONPATH=samplesample




Outputs
==============

The result files output from each run include certain files that are always written as well as optional results files:

=================   =====================================================
``spikerast.dat``   All spike times and gids of spiking cells.
``numcons.dat``   Summary of number of connections between each pre and post cell type, on each processor.
``connections.dat``   Detailed list of every synapse in model.
================   =====================================================


Customizing
=========

To run this code with different parameters:

.. code-block:: bash

    #!/bin/bash

    nrngui [-c "Parameter=Value"]  [-c "strdef StringParam" "StringParam=\"StringValue\""]   ...

To run a network clamp simulation:

.. code-block:: bash

    #!/bin/bash
    
    nrngui -nopython -c gidOI=21310 -c cellindOI=6 -c stimflag=0 -c "strdef runname" -c runname="\"ca1_1x_exc_08\""  -c "strdef origRunName" -c origRunName="\"ca1_1x_exc_08\""  -c "strdef celltype2use" -c celltype2use="\"poolosyncell\""     -c "strdef resultsfolder" -c resultsfolder="\"00001\"" ./networkclamp_results/ca1_1x_exc_08/00001/run.hoc -c "quit()"


To customize this code...



Best practices
--------------

The blah blah blah.



Meta
====

Interface design
----------------

Blah blah.



User support
------------

Please use the following support channels:

* `GitHub issues <https://github.com/mbezaire/ca1/issues>`_
  for bug reports and feature requests.
* `Our NEURON forum thread <https://www.neuron.yale.edu/phpBB/viewtopic.php?f=18&t=3688>`_
  to ask questions, discuss features, and for general discussion.


Related projects
----------------

Dependencies
~~~~~~~~~~~~

ca1 uses NEURON with HOC:

* `Requests <http://python-requests.org>`_
  — Python HTTP library for humans
* `Pygments <http://pygments.org/>`_
  — Python syntax highlighter


ca1 friends
~~~~~~~~~~~~~~

ca1 can be used with:

* `SimTracker <https://stedolan.github.io/jq/>`_
  — Simulation management tool
* `Neuroscience Gateway <https://github.com/eliangcs/http-prompt>`_
  —  user-friendly parallel computing for large scale neural networks


Alternatives
~~~~~~~~~~~~

* `ModelDB <https://senselab.med.yale.edu/modeldb/>`_ — ModelDB contains many NEURON models and other neuroscience simulator models for various networks and cell types.


Citation
-------

Please cite this code if you use it or derive a model from it, using the most appropriate citation below:

* Our ModelDB entry: Cite `Bezaire et al (2016) <https://elifesciences.org/articles/18566>`_, ModelDB (accession number 187604), and `McDougal et al (2017) <https://link.springer.com/article/10.1007/s10827-016-0623-7>`_. See `these instructions <https://senselab.med.yale.edu/ModelDB/HowToCite.cshtml>`_ for further details. 

* Our Open Source Brain entry: Cite `Bezaire et al (2016) <https://elifesciences.org/articles/18566>`_ and see `this link <http://www.opensourcebrain.org/docs#FAQ>`_ for more information.

License
-------
CC0 1.0 Universal (CC0 1.0): Public Domain Dedication

For more information, see the `CC0 Description <https://creativecommons.org/publicdomain/zero/1.0/>`_.

.. class:: no-web

    .. image:: https://i.creativecommons.org/p/zero/1.0/88x31.png
        :alt: CC0 License
        :width: 10%
        :align: left
        


Authors
-------

Marianne Bezaire created the ca1 model with help from:


* Ivan Raikov
* Padraig Gleeson
* Andras Ecker
* Kelly Burk
* Michael Hines
* Ted Carnevale
* Ivan Soltesz
