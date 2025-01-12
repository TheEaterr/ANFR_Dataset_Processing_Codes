import pandas as pd

from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join, isdir

# read the csv file with first line as labels
communes_pop = pd.read_csv('insee_pop.csv', sep=';', header=0)
communes_pop = communes_pop[communes_pop['an'] == 2020]
communes_pop = communes_pop.dropna()
communes_pop = communes_pop[['codgeo', 'p_pop']]
communes_pop.to_csv('communes_pop.csv', index=False)
communes_super = pd.read_csv('insee_super.csv', sep=';', header=0)
communes_super = communes_super[communes_super['an'] == 2020]
communes_super = communes_super.dropna()
communes_super = communes_super[['codgeo', 'superf_choro']]
communes_super.to_csv('communes_super.csv', index=False)

communes_data = pd.merge(communes_pop, communes_super, on='codgeo')
communes_data = communes_data.rename(columns={'codgeo': 'code_insee', 'p_pop': 'population', 'superf_choro': 'superficie'})
# modify superficie (number with a comma) to a python float
communes_data['superficie'] = communes_data['superficie'].str.replace(',', '.')
communes_data['superficie'] = communes_data['superficie'].astype(float)
communes_data['population'] = communes_data['population'].astype(int)
communes_data['densite'] = communes_data['population'] / communes_data['superficie']
print(communes_data)

# export to csv
communes_data.to_csv('communes_data.csv', index=False)