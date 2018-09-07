# %load q02_eda_major_death/build.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering

pd.set_option('display.max_columns', 500)
battles = pd.read_csv('data/battles.csv')
data3 = pd.DataFrame()
character_predictions = pd.read_csv('data/character-predictions.csv')

# using groupby function to form dataframe where index as year.
data3['major_death'] = battles.groupby(battles['year'])['major_death'].agg('sum')
data3['major_capture'] = battles.groupby(battles['year'])['major_capture'].agg('sum')

def q02_eda_major_death(data):
    'write your solution here'
    
    #fig, ax = plt.subplots()
    ax = data3[['major_death','major_capture']].plot(kind='bar',title ='', figsize=(15, 10), legend=True)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('No of Death/Capture Event', fontsize=12)
    plt.show()
    #return(data3)
    

q02_eda_major_death(data3)



