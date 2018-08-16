import numpy as np
import pandas as pd
#needed for Jupyter Notebook, if want plots to show inline


import glob
import re


from collections import Counter
from datetime import datetime, timedelta

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score



def read2000sMatches(dirname):
    allFiles = glob.glob(dirname + "/atp_matches_2" + "*.csv")
    matches = pd.DataFrame()
    list_ = list()
    for filen in allFiles:
        df = pd.read_csv(filen,
                         index_col=None,
                         header=0,
                         parse_dates=[0])
                         #date_parser=lambda t:parse(t))
        list_.append(df)
    matches = pd.concat(list_)
    return matches

def read1900sMatches(dirname):
    allFiles = glob.glob(dirname + "/atp_matches_1" + "*.csv")
    matches = pd.DataFrame()
    list_ = list()
    for filen in allFiles:
        df = pd.read_csv(filen,
                         index_col=None,
                         header=0,
                         parse_dates=[0])
                         #date_parser=lambda t:parse(t))
        list_.append(df)
    matches = pd.concat(list_)
    return matches

def get_time(starting_df,early,late):
    return starting_df[(starting_df.tourney_date.apply(lambda x:x.year)<late+1) \
                        & (starting_df.tourney_date.apply(lambda x:x.year)>early-2)]


def get_player_dfs(starting_df,player_name):
    return starting_df[starting_df['name']==player_name]


matches2000s=read2000sMatches('tennis/')
matches1900s=read1900sMatches('tennis/')
matches_SackmannAll = pd.concat([matches1900s,matches2000s])
matches_SackmannAll.shape # (167879, 49)



df_stats = matches_SackmannAll[~pd.isnull(matches_SackmannAll['w_ace'])]

df_win = df_stats[['tourney_id', 'match_num','tourney_name', 'surface', 'draw_size', 'tourney_level',
       'tourney_date',  'score', 'best_of',
       'round', 'minutes','winner_id', 'winner_seed', 'winner_entry',
       'winner_name', 'winner_hand', 'winner_ht', 'winner_ioc', 'winner_age',
       'winner_rank', 'winner_rank_points','w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon', 'w_2ndWon', 'w_SvGms',
       'w_bpSaved', 'w_bpFaced']]
df_loss = df_stats[['tourney_id','match_num','tourney_name', 'surface', 'draw_size', 'tourney_level',
       'tourney_date',  'score', 'best_of',
       'round', 'minutes','loser_id', 'loser_seed',
       'loser_entry', 'loser_name', 'loser_hand', 'loser_ht', 'loser_ioc',
       'loser_age', 'loser_rank', 'loser_rank_points','l_ace', 'l_df',
       'l_svpt', 'l_1stIn', 'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved',
       'l_bpFaced']]

df_win.columns = [s.replace("winner_", "") for s in df_win.columns]
df_win.columns = [s.replace("w_", "") for s in df_win.columns]
df_loss.columns = [s.replace("loser_", "") for s in df_win.columns]
df_loss.columns = [s.replace("l_", "") for s in df_win.columns]

df_win['target']=1
df_loss['target']=0

df_win_loss = pd.concat([df_win,df_loss])

del(matches1900s,matches2000s)
del(df_win,df_loss)


## fill method of entry for most players with 'standard'; mostly missing values
df_win_loss['entry'] = df_win_loss['entry'].fillna('standard')

## better way might be max(33,rank) ## 33 is the minumum non-seeded value
##high positive value because negative associates with better rank
df_win_loss['seed'] = df_win_loss['seed'].fillna(9999)
df_win_loss['seed'] = df_win_loss['seed'].astype(int)

#rank, and rank_points have ~4000 missign out of 162000
df_win_loss[['rank','rank_points']] = df_win_loss.groupby('name')[['rank','rank_points']]\
                                        .transform(lambda x: x.fillna(x.mean()))
#rank, and rank_points have some more missing values: set to maximum ranking and minimum rank points
df_win_loss['rank'] = df_win_loss['rank']\
                                        .transform(lambda x: x.fillna(x.max()))
df_win_loss['rank_points'] = df_win_loss['rank_points']\
                                        .transform(lambda x: x.fillna(x.min()))

## set 'hand' to U ('unknown') ~35 missing 'hand'
df_win_loss['hand'] = df_win_loss['hand'].fillna('U')

# set missing height, age  to average for all people ~7000 missing heights, ~100 missing age
df_win_loss[['age','ht']] = df_win_loss[['age','ht']]\
                                        .transform(lambda x: x.fillna(x.mean()))

## set missing minutes to average age of all ~5000 missing minutes
df_win_loss['minutes'] = df_win_loss['minutes']\
                                        .transform(lambda x: x.fillna(x.mean()))

df_win_loss = pd.concat([df_win_loss,\
                         pd.get_dummies(df_win_loss['surface'])],axis=1)
df_win_loss.drop('surface', axis=1,inplace=True)    


df_win_loss = pd.concat([df_win_loss,\
                         pd.get_dummies(df_win_loss['hand'])],axis=1)
df_win_loss.drop('hand', axis=1,inplace=True)

df_win_loss = pd.concat([df_win_loss,\
                         pd.get_dummies(df_win_loss['tourney_level'])],axis=1)
df_win_loss.drop('tourney_level', axis=1,inplace=True)

# Conversion to Datetime

## Set up a time delta
one_year = timedelta(days=365)
## this conversion works, have to reassign becuase operation is not inplace
df_win_loss['tourney_date']= pd.to_datetime(df_win_loss['tourney_date'].apply(str))

df_win_loss.index = df_win_loss['tourney_date']
df_win_loss.set_index(np.arange(1,len(df_win_loss)+1),inplace=True)




date = pd.datetime(2010,11,23)
one_year=timedelta(days=370) 



df_wl_sort = df_win_loss.sort_values(['tourney_date','match_num'],ascending=[1,1],axis=0)

df_wl_sort_colSlct = df_wl_sort[['name','match_num','tourney_date','minutes', 
       'ht', 'age', 'rank_points', 'ace', 'df',
       'svpt', '1stIn', '1stWon', '2ndWon', 'SvGms', 'bpSaved', 'bpFaced',
       'Carpet', 'Clay', 'Grass', 'Hard', 'None', 'L', 'R', 'U', 'A',
       'C', 'D', 'F', 'G', 'M','target']]



tr_start = 1993
tr_end = 2011
years_df = get_time(df_wl_sort_colSlct,tr_start,tr_end)


### should be a fuction: def
plyr_yr_df = pd.DataFrame()
new_df = pd.DataFrame()
# I want
computed_df = pd.DataFrame()
# new_cols = plyr_yr_df.columns.append('name')
train_target = pd.Series()

for player in years_df['name'].unique():
    plyr_yr_df = get_player_dfs(years_df,player)
    part_train_target = plyr_yr_df['target']
    part_compute_df =  plyr_yr_df.drop('name',axis=1).rolling(one_year,on='tourney_date').mean().shift(1)
    part_compute_df['name'] = player
    new_df = new_df.append(part_compute_df)
    train_target = train_target.append(part_train_target)

new_df['target'] = train_target    
train_computed_df = new_df.dropna()

### end: should be a fuction: def



### should be same functionas above, but called
## ... a separate tiem : def:
## Test data set

tr_start = 2012
tr_end = 2017
years_df = get_time(df_wl_sort_colSlct,tr_start,tr_end)



plyr_yr_df = pd.DataFrame()
new_df = pd.DataFrame()
computed_df = pd.DataFrame
test_target = pd.Series()

for player in years_df['name'].unique():
    plyr_yr_df = get_player_dfs(years_df,player)
    part_test_target = plyr_yr_df['target']
    part_compute_df =  plyr_yr_df.drop('name',axis=1).rolling(one_year,on='tourney_date').mean().shift(1)
    part_compute_df['name'] = player
    new_df = new_df.append(part_compute_df)
    test_target = test_target.append(part_test_target)
    
new_df['target'] = test_target
new_df.dropna(inplace=True)
test_computed_df = new_df[new_df.tourney_date.apply(lambda x:x.year>2011)]



## gradient boosting itself

# Data prep
gbr_train_df = train_computed_df.drop(['name','tourney_date','match_num'],axis=1)
gbr_test_df = test_computed_df.drop(['name','tourney_date','match_num'],axis=1)


params = {'n_estimators': [180,200,500],
          'max_features': [.1,.3,.4],
          'max_depth': [2,3,4],
          'learning_rate': [0.0001,.0005,.001]}
gbr = GradientBoostingClassifier()
gs = GridSearchCV(gbr, params, scoring='accuracy')
gs.fit(gbr_train_df.drop('target',axis=1), gbr_train_df['target'])

print('Best Params for Gradient Boosting are: ')
print(gs.best_params_)

gbr_tuney_model = GradientBoostingClassifier(gs.best_params_)
gbr_tuney_model.fit(gbr_train_df.drop('target',axis=1), gbr_train_df['target'])
# score from training data: 
print('score for Gradient Boosting (training) are: ')
print(gbr_tuney_model.score(gbr_train_df.drop('target',axis=1), gbr_train_df['target']))

# score from test data:
print('score for Gradient Boosting (training) are: ')
print(gbr_tuney_model.score(gbr_test_df.drop('target',axis=1), gbr_test_df['target']))



