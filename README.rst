ca1: a NEURON network model
########################################

ca1 is a large-scale, detailed, biologically constrained NEURON network model of the rodent hippocampal CA1 area.

.. contents::

.. section-numbering::



Main features
=============

* Linux, Mac OS X and Windows support
* Documentation


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


Hello World:


.. code-block:: bash

    $ nrngui -nopython


Synopsis:

.. code-block:: bash

    $ nrngui [-c parameters] [main.hoc file]  -c "quit()"


See also ``nrngui help``.


Examples
--------

Custom `HTTP method`_, `HTTP headers`_ and `JSON`_ data:

.. code-block:: bash

    $ http PUT example.org X-API-Token:123 name=John



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

    nrngui ...

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

* `Check ModelDB <https://senselab.med.yale.edu/modeldb/>`_ — ModelDB contains many NEURON models and other neuroscience simulator models for various networks and cell types.



License
-------

.. |CC0| image:: https://i.creativecommons.org/p/zero/1.0/88x31.png
    :target: https://creativecommons.org/publicdomain/zero/1.0/
    :alt: CC0 1.0 Universal (CC0 1.0): Public Domain Dedication


Authors
-------

`Marianne Bezaire`_  (`@mbezaire`_) created the ca1 model with help from:


.. _Ivan Raikov
.. _Padraig Gleeson
.. _Andras Ecker
.. _Kelly Burk
.. _Michael Hines
.. _Ted Carnevale
.. _Ivan Soltesz
