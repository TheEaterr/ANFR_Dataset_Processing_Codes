# ANFR Dataset Processing - Source Code
This repository contains the source code for data processing of the ANFR dataset. The results of this source code are described in the paper (submitted for review at Annals of Telecommunications) titled as **"Radio Access Network Carbon Footprint in France: Historical Trend and Prospective Scenarios"**. The contacts for the project include **M. Paul Breuil** (<tykapl.breuil@gmail.com>), **Dr. Marceau Coupechoux** (<marceau.coupechoux@telecom-paris.fr>) from Télécom Paris and **Dr. Juan-Antonio Cordero-Fuertes** (<juan-antonio.cordero-fuertes@polytechnique.edu>) from École polytechnique.


For details regarding the dataset and data processing, please consult the included PDF file.

Before running the source code, the following steps are to be completed:

* Firstly, three new folders should be created within the code directory. The first should be named as "ANFR Dataset", the second should be "Pre-processed data" and the last one should be "Graphs".
* Within the 'ANFR Dataset' folder, the entire ANFR dataset is to be placed. The dataset including the data and the reference files can be downloaded from the dataset website. The downloading process is tedious as the files for each month needs to be downloaded one by one.
* The script download_data.sh allows the downloading of the whole ANFR database
* The 'Dataset_Preprocessing.ipynb' file should then be executed first before running the other notebooks, and Production_Cost_Analysis.ipynb should be executed last.

Note: the communes_data.csv was generated using the script parse_communes.py and the data found at the following links:
* https://www.observatoire-des-territoires.gouv.fr/superficie
* https://www.observatoire-des-territoires.gouv.fr/population-au-dernier-recensement