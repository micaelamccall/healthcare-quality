from getData import cahps_df, mua_df, readm_df
import pandas as pd

def get_cols(df):
    cols = []
    for col in df:
        cols.append(col)
    return cols

def get_counts(df):
    counts=[]
    for col in df:
        counts.append(df[col].value_counts())
    return counts


readm_cols = get_cols(readm_df)
cahps_cols= get_cols(cahps_df)
mua_cols = get_cols(mua_df)

mua_df=mua_df.drop(columns=['Minor Civil Division FIPS Code', 'Minor Civil Division Census Code', 'Minor Civil Division Name', 'MUA/P Status Code', 'Census Tract', 'Designation Date','Designation Date.1', 'State and County Federal Information Processing Standard Code', 'County or County Equivalent Federal Information Processing Standard Code', 'HHS Region Code','HHS Region Name','State FIPS Code', 'Data Warehouse Record Create Date','Data Warehouse Record Create Date Text','Primary State FIPS Code','HPSA Primary State Abbreviation', 'Primary State Name','Primary HHS Region Code','Primary HHS Region Name','Common Region Code','Common Region Name','Common State Name','Common State Abbreviation','Common State FIPS Code','Common State County FIPS Code', 'Break in Designation','Medically Underserved Area/Population (MUA/P) Component Designation Date','Medically Underserved Area/Population (MUA/P) Component Designation Date.1',  'Medically Underserved Area/Population (MUA/P) Component Geographic Name','Medically Underserved Area/Population (MUA/P) Component Geographic Type Code','Medically Underserved Area/Population (MUA/P) Component Geographic Type Description','Medically Underserved Area Geography Type Surrogate Key','Medically Underserved Area/Population (MUA/P) Component Last Update Date','Medically Underserved Area/Population (MUA/P) Component Status Code','Medically Underserved Area/Population (MUA/P) Component Status Description','Medically Underserved Area/Population (MUA/P) Component Update Date','Designation Population in a Medically Underserved Area/Population (MUA/P)', 'Medically Underserved Area/Population (MUA/P) Population Type ID','Medically Underserved Area/Population (MUA/P) Total Resident Civilian Population','Medically Underserved Area/Population (MUA/P) Withdrawal Date','Medically Underserved Area/Population (MUA/P) Withdrawal Date in Text Format', 'Unnamed: 74'])
mua_cols = get_cols(mua_df)
mua_df=mua_df.drop(columns=['MUA/P ID', 'Medically Underserved Area/Population (MUA/P) Population Type','Medically Underserved Area/Population (MUA/P) Metropolitan Indicator.1', 'Medically Underserved Area/Population (MUA/P) Metropolitan Description', 'Medically Underserved Area/Population (MUA/P) Metropolitan Indicator', 'Rural Status Code', 'Designation Type Code'])
mua_counts=get_counts(mua_df)


#align county columns
mua_df=mua_df.rename(columns={"County Equivalent Name":"county_name"})
cahps_df=cahps_df.rename(columns={"county":"county_name"})
cahps_df['county_name'] = cahps_df.county_name.str.capitalize()

readm_df=readm_df.rename(columns={"hospital_name":"facility_name"})

full_df=pd.merge(cahps_df, mua_df, how='left', on='county_name')


get_counts(cahps_df)
cahps_df=cahps_df.drop(columns=['measure_start_date', 'measure_end_date', 'footnote', 'telephone'])


join=

V=cahps_df['facility_name'].value_counts()
cahps_df.loc[cahps_df['facility_name']=="WAYNE MEMORIAL HOSPITAL"]


cahps_df.info
cahps_df.describe()
cahps_df.columns
cahps_df['footnote']
len(mua_df.columns)
mua_df.iloc[1, 60:75]
mua_df.describe()
cahps_df_long=cahps_df