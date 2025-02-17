============
Installation
============

-------------------------
Installation From Release
-------------------------

pyNastran is an easy package to install once you have the required Python
modules.  It's a pure Python package so you shouldn't have too many problems.
Just type:

``pip install pyNastran``


Python
------
The software is tested against:
 * Python 3.7 **(Windows/Linux)**
 * Python 3.8 **(Windows/Linux)**

Packages
--------
pyNastran is tested against a range of package versions (lowest to highest
based on availbility), so should work.  The recommended set of packages are:
 * **Required**:

   * numpy >= 1.14
   * scipy >= 1.0
   * cpylog >= 1.4.0
   * docopt-ng == 0.7.2    **(required for command line tools)**

 * **Optional**:

   * colorama >= 0.3.9    **(colored logging)**
   * pandas ???
   * matplotlib >= 2.2.4  **(plotting)**
   * h5py >= 2.8.0        **(HDF5 support)**

 * **GUI**:

   * vtk 7.1.1 or 8.1.1
   * qtpy >= 1.4.0
   * Qt **(pick one)**

     * PyQt5 >= 5.9.2
     * PySide2 >= 5.11.2
   * QScintilla >= ??? **(optional for fancy scripting)**
   * pygments >= 2.2.0 **(optional for fancy scripting)**
   * imageio >= 2.4.1 **(optional for animation support)**

***********************************************
Install Procedure - From Anaconda (recommended)
***********************************************
Base functionality:
 * `64-bit Python <https://www.python.org/downloads/>`_
 * ``pip install numpy``
 * ``pip install scipy``
 * ``pip install docopt-ng``   **(required for command line tools)**
 * ``pip install pandas``   **(optional)**
 * ``pip install h5py``       **(optional for HDF5 support)**
 * ``pip install matplotlib`` **(optional for plotting)**
 * ``pip install colorama``   **(optional for colored logging)**
 * ``pip install cpylog``
 * ``pip install pyNastran``

For **optional** GUI support:

 * On the command line:
    * ``pip install imageio`` **(optional for animation support)**
    * ``pip install pyside2``
    * ``pip install VTK*.whl``
    * ``pip install qtpy``

 * Additional source for `Windows binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_


Use Web docs
------------
See `docs <https://pynastran-git.readthedocs.io/en/1.3/>`_

-------------------------
Installation From Source
-------------------------

pyNastran is an easy package to install once you have the required Python
modules.  It's a pure Python package so you shouldn't have too many problems.

Installing from source is recommened if:
 - You want the most recent version (see installation.rst-master)
 - You want easier access to the source
 - You're on an air-gapped machine

Overview
========
 * Install Python (see :doc:`installation_release`)

   * skip the ``pip install pyNastran`` step
 * Install Sphinx, GraphViz, alabaster **(for documentation)**

 * Install Git
 * Clone pyNastran-master from Github
 * Install pyNastran

Install extra packages (for Doucmentation)
==========================================

Install `GraphViz  <https://www.graphviz.org/>`_

Install additional python packages

.. code-block:: console

  pip install Sphinx
  pip install alabaster
  pip install numpydoc

Install Git
===========

 * Download & install `Git <http://git-scm.com/>`_
 * Download a GUI for Git (optional)
    * `TortoiseGit <https://code.google.com/p/tortoisegit/>`_ (recommended for Windows)


Install pyNastran
=================
There are two ways to install the 1.2 (master/dev) version of pyNastran

 1. Download the most recent `zip version <https://github.com/SteveDoyle2/pyNastran/archive/1.3.zip>`_

 2. Clone pyNastran (see below).  Using Git allows you to easily update to the
    latest dev version when you want to as well as push any commits of your own.

If you don't want the gui, use ``setup_no_gui.py`` instead of ``setup.py``.

.. code-block:: console

  >>> python setup.py install

or:

.. code-block:: console

  >>> python setup_no_gui.py install


Cloning pyNastran using TortoiseGit
===================================
Right-click in a folder and select ``Git Clone``.

.. image:: clone.png

Enter the above information.  If desired, click the branch box and and enter a branch name
and click ``OK``.

Cloning pyNastran Using Command Line
====================================
Checkout/clone the dev code by typing **(preferred)**:

.. code-block:: console

  >>> git clone https://github.com/SteveDoyle2/pynastran


To checkout a branch

.. code-block:: console

  >>> git.exe clone --branch 1.3 --progress -v "https://github.com/SteveDoyle2/pyNastran.git" "C:\\work\\pyNastran_1.3"


Documentation
=============
Two options for documentation exist.

Build Docs
----------
Navigate to ``pyNastran/docs_sphinx`` directory on the command line.

.. code-block:: console

  >>> make html

