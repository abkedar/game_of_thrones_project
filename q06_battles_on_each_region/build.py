# %load q06_battles_on_each_region/build.py
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('white')
import matplotlib.pyplot as plt
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
plt.switch_backend('agg') 
pd.set_option('display.max_columns', 500)
battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

df_1 = pd.DataFrame()
df_1['major_death'] = battles.groupby(['region'])['major_death'].agg('sum')
df_1['major_capture'] = battles.groupby(['region'])['major_capture'].agg('sum')



def q06_battles_on_each_region(df):
    'write your solution here'
    
    # Plotting bar graph on number of battle took place at given region.
    ax = df[['major_death','major_capture']].plot(kind='bar',title ='', figsize=(15, 10), legend=True)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('No of Death/Capture Event', fontsize=12)
    plt.show()
    return df_1
    

q06_battles_on_each_region(df_1)



