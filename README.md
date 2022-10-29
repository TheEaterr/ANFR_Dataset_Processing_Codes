# ANFR Dataset Processing - Source Code
This repository contains the source code for data processing of the ANFR dataset. The results of this source code are described in the paper (submitted for review at ICC2023) titled as **"The Long Road to Sobriety: Estimating the Operational Power Consumption of Cellular Base Stations in France"**. The contacts for the project include **Arsalan Ahmed** (<arsalanqasimahmed@gmail.com>) and **Dr. Marceau Coupechoux** (<marceau.coupechoux@telecom-paris.fr>) from Télécom Paris.


For details regarding the dataset and data processing, please consult the included PDF file.


This installation guide assumes that GNU Radio has been installed using PyBOMBS. Also, please note that gr-owc is currently only compatible with GNURadio 3.8 version.

To download and install, follow the steps below:

1-) First of all source the setup of your desired GNU Radio prefix in the terminal

2-) Download this repository by cloning with git clone (url)

3-) cd to the gr-owc directory

4-) Create a build directory with 'mkdir build' and move into the directory with 'cd build/'

5-) Run cmake (the path to the sourced GNU Radio installation would be found automatically): 'cmake ../'

6-) Run 'make'

7-) Test the build with 'make test' (shouldn't be any failures)

8-) Install with 'make install'

9-) Configure your linker/debugger with 'sudo ldconfig'

10-) Open gnuradio-companion and you should find a module for gr-owc

Alternatively, gr-owc can also be installed directly into the desired GNURadio prefix using PyBOMBS. For this, follow the steps below:

1-) Configure PyBOMBS for default configuration with 'pybombs auto-config'

2-) Point PyBOMBS to the recipes for installing OOT modules. As a default, you can use 'pybombs recipes add-defaults' (adds gr-recipes and gr-etcetra) 

3-) cd into the desired GNURadio prefix folder

4-) Install gr-owc using pybombs with 'pybombs install gr-owc' 

5-) Open gnuradio-comapanion from that prefix and you should find a module for gr-owc