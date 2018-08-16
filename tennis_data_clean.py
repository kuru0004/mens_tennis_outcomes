import numpy as np
import pandas as pd



def read2000sMatches(dirname):
	"""
	Inputs: folder (directory) name, str
	Outputs: a data frame of tennis matches, dataframe

	Takes csv files of 1900s tennis matches 
    from directory and converts 
    to a combined dataframe
	"""
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

    """
    Inputs: folder (directory) name, str
    Outputs: a data frame of tennis matches, dataframe

    Takes csv files of 2000s tennis matches 
    from directory and converts 
    to a combined dataframe
    """
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


def make_single_df(dfs,win_list,loss_list):

    """
    Inputs: list of dataframes, list of columns of winner
            list of columns for loser
    Outputs: a data frame of tennis matches
           formatted by winners and losers, dataframe

    Returns dataframe of concatenated winner rows and 
    loser rows
    """

    all_cat = pd.concat(dfs)
    df_win = all_cat[win_list]
    df_loss = all_cat[loss_list]
    df_win.columns = [s.replace("winner_", "") for s in df_win.columns]
    df_win.columns = [s.replace("w_", "") for s in df_win.columns]
    df_loss.columns = [s.replace("loser_", "") for s in df_win.columns]
    df_loss.columns = [s.replace("l_", "") for s in df_win.columns]

    df_win['target']=1
    df_loss['target']=0

    return pd.concat([df_win,df_loss])



def fill_na_vals(df,na_fill_seed=9999,):


    ## fill method of entry for most players with 'standard'; mostly missing values
    df_win_loss['entry'] = df_win_loss['entry'].fillna('standard')

    ## better way might be max(33,rank) ## 33 is the minumum non-seeded value
    ##high positive value because negative associates with better rank
    df_win_loss['seed'] = df_win_loss['seed'].fillna(na_fill_seed)
    df_win_loss['seed'] = df_win_loss['seed'].astype(int)

    #rank, and rank_points have ~4000 missign out of 162000
    df_win_loss[['rank','rank_points']] = df_win_loss.groupby('name')[['rank','rank_points']]\
                                            .transform(lambda x: x.fillna(x.mean()))
    #rank, and rank_points have some more missing values: set to maximum ranking and minimum rank points
    df_win_loss['rank'] = df_win_loss['rank']\
                                            .transform(lambda x: x.fillna(x.max()))
    df_win_loss['rank_points'] = df_win_loss['rank_points']\
                                            .transform(lambda x: x.fillna(x.min()))

    df_win_loss['hand'] = df_win_loss['hand'].fillna('U')

    df_win_loss[['age','ht']] = df_win_loss[['age','ht']]\
                                        .transform(lambda x: x.fillna(x.mean()))
    ## set missing minutes to average age of all ~5000 missing minutes
df_win_loss['minutes'] = df_win_loss['minutes']\
                                        .transform(lambda x: x.fillna(x.mean()))





if __name__ == '__main__':
	
    main()

