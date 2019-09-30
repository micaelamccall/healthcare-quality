import pandas as pd

def double_merge(df1, df2, df3, merge1, merge2):
    """
    Left merges 3 datasets using a left merge
    arguments: 
    df1 =  pandas dataframe of the limiting dataset / want to keep all the columns
    df2, df3 = the other two pandas dataframes 
    merge1 = a list of columns to merge on for the first merge
    merge2 = a list of columns to merge on for the 2nd merge 
    returns: a pandas dataframe of mergerd data
    """

    first_merge = df1.merge(df2, how = 'left', on = merge1)

    second_merge = first_merge.merge(df3, how = 'left', on = merge2)

    return second_merge
