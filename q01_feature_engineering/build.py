# %load q01_feature_engineering/build.py
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q01_feature_engineering(df_1, df_2):
    'write your solution here'
    
    # initializing data with resp datasets
    data_1 = df_1
    data_2 = df_2
    
    # defining and assiging new columns
    data_1['attacker_count'] = data_1[['attacker_1', 'attacker_2', 'attacker_3', 'attacker_4']].sum(1)
    data_1['defender_count'] = data_1[['defender_1', 'defender_2', 'defender_3', 'defender_4']].sum(1)
    data_1['att_comm_count'] = data_1['attacker_commander'].map(lambda x: 0 if str(x) == 'nan' else len(str(x).split(',')))
    data_2['no_of_books'] = data_2[['book1', 'book2', 'book3', 'book4', 'book5']].sum(1)
    return(data_1, data_2)
    #print(data_2)

q01_feature_engineering(battles, character_predictions)
#df1= battles
#df1.columns
#df1.attacker_commander.value_counts()
#df1['defender_3']


