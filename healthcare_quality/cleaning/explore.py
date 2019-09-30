import pandas as pd
import os
import sys
sys.path.append(os.path.abspath("healthcare_quality"))

#define some helpful functions
def get_cols(df):
    """get a list of column names in a DataFrame
    input: a pandas DataFrame
    returns: a list of columsn in the df"""
    cols = []
    for col in df:
        cols.append(col)
    return cols

def get_counts(df):
    """get a list of counts for each column in a DataFrame
    input: a pandas DataFrame
    returns: a list of counts for each column"""
    counts=[]
    for col in df:
        counts.append(df[col].value_counts())
    return counts

if __name__ == '__main__':
    from import_data import cahps_df, mua_df, readm_df
    #Explore the columns and counts in each DataFrame
    get_cols(cahps_df) #get a list of columns
    get_counts(cahps_df) #state is abbreviation; city, county, address, and facility name are in all caps; and there are several hospital names that appear more than once 

    get_cols(readm_df) #there's a column called location_state and one called state. Zip is called zip_code. 
    readm_counts=get_counts(readm_df) #state is abbreviation; city, county, address, and facility name are in all caps; and there are several hospital names that appear more than once 

    #There's tons of columns in the Medically Underserved Area DataFrame 
    mua_cols = get_cols(mua_df)
    mua_counts = get_counts(mua_df)
    #look closer at Designation Type
    mua_counts[6]
    #look at population type
    mua_counts[66]
    #look at MUA status description
    mua_counts[8]
    mua_counts[65]