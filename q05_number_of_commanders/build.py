# %load q05_number_of_commanders/build.py
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('white')
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
import matplotlib
matplotlib.use('Agg')
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import sys,os
plt.switch_backend('agg') 


battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')
battles, character_predictions = q01_feature_engineering(battles, character_predictions)
data1 = battles[['attacker_king', 'att_comm_count']]

def q05_number_of_commanders(data):
    'write your solution here'
    
    # Plot boxplot on battles datasets and columns 'att_comm_count', 'attacker_king' 
    data.plot(kind='box', figsize=(12,8))
    plt.show()
    #return df

q05_number_of_commanders(data1)


