# ANFR Dataset Processing - Source Code
This repository contains the source code for data processing of the ANFR dataset. The results of this source code are described in the paper (submitted for review at 
ICT4S23) titled as **"The Long Road to Sobriety: Estimating the Operational Power Consumption of Cellular Base Stations in France"**. The contacts for the project include **Arsalan Ahmed** (<arsalanqasimahmed@gmail.com>) and **Dr. Marceau Coupechoux** (<marceau.coupechoux@telecom-paris.fr>) from Télécom Paris.


For details regarding the dataset and data processing, please consult the included PDF file.


Before running the source code, the following steps are to be completed:

* Firstly, three new folders should be created within the code directory. The first should be named as "ANFR Dataset", the second should be "Pre-processed data" and the last one should be "Graphs".
* Within the 'ANFR Dataset' folder, the entire ANFR dataset is to be placed. The dataset including the data and the reference files can be downloaded from the dataset website. The downloading process is tedious as the files for each month needs to be downloaded one by one.
* There are a few mistakes in the downloaded files from the ANFR website. Hence, for specific month's files, the following should be done manually:
    * **April 2022**: In the folder name, 2023 should be changed to 2022.
    * **May 2018**: The date format should be changed from 31052018 to 20180531 in the folder names.
    * **March 2018**: The data and reference folders are within the same folder so they should be separated.
    * **January 2018**: The date should be moved in the front of the folder name. Also it should be formatted similar to what is mentioned for May 2018.
    * **January 2017**: There is no reference folder, so the reference folder for February 2017 should be utilized. A new folder should be created with the correct naming.
    * **May 2016**: The date in the folder name should be changed from 20160402 to 20160430.
    * **April and May 2015**: The dates are missing so they should be added in the correct format with the folder names.
* The 'Dataset_Preprocessing.ipynb' file should be executed first before running the other files.
* The script download_data.sh allows the downloading of the whole ANFR database 
