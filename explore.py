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

mua_df=mua_df.drop(columns=['MUA/P ID', 'Common County Name', 'Complete County Name', 'MUA/P Service Area Name','County Description','State Name','Medically Underserved Area/Population (MUA/P) Population Type','Medically Underserved Area/Population (MUA/P) Metropolitan Indicator.1', 'Medically Underserved Area/Population (MUA/P) Metropolitan Description', 'Medically Underserved Area/Population (MUA/P) Metropolitan Indicator', 'Rural Status Code', 'Designation Type Code', 'Minor Civil Division FIPS Code', 'Minor Civil Division Census Code', 'Minor Civil Division Name', 'MUA/P Status Code', 'Census Tract', 'Designation Date','Designation Date.1', 'State and County Federal Information Processing Standard Code', 'County or County Equivalent Federal Information Processing Standard Code', 'HHS Region Code','HHS Region Name','State FIPS Code', 'Data Warehouse Record Create Date','Data Warehouse Record Create Date Text','Primary State FIPS Code','HPSA Primary State Abbreviation', 'Primary State Name','Primary HHS Region Code','Primary HHS Region Name','Common Region Code','Common Region Name','Common State Name','Common State Abbreviation','Common State FIPS Code','Common State County FIPS Code', 'Break in Designation','Medically Underserved Area/Population (MUA/P) Component Designation Date','Medically Underserved Area/Population (MUA/P) Component Designation Date.1',  'Medically Underserved Area/Population (MUA/P) Component Geographic Name','Medically Underserved Area/Population (MUA/P) Component Geographic Type Code','Medically Underserved Area/Population (MUA/P) Component Geographic Type Description','Medically Underserved Area Geography Type Surrogate Key','Medically Underserved Area/Population (MUA/P) Component Last Update Date','Medically Underserved Area/Population (MUA/P) Component Status Code','Medically Underserved Area/Population (MUA/P) Component Status Description','Medically Underserved Area/Population (MUA/P) Component Update Date','Designation Population in a Medically Underserved Area/Population (MUA/P)', 'Medically Underserved Area/Population (MUA/P) Population Type ID','Medically Underserved Area/Population (MUA/P) Total Resident Civilian Population','Medically Underserved Area/Population (MUA/P) Withdrawal Date','Medically Underserved Area/Population (MUA/P) Withdrawal Date in Text Format', 'Unnamed: 74'])
mua_counts=get_counts(mua_df)

get_counts(cahps_df)
cahps_df=cahps_df.drop(columns=['measure_start_date', 'measure_end_date', 'footnote', 'telephone'])

#align county columns
mua_df=mua_df.rename(columns={"County Equivalent Name":"county_name", "State Abbreviation":"state"})
cahps_df=cahps_df.rename(columns={"county":"county_name"})
cahps_df['county_name'] = cahps_df.county_name.str.title()

readm_df=readm_df.rename(columns={"hospital_name":"facility_name"})

full_df=cahps_df.merge(mua_df, how='left', on=['state', 'county_name']).drop_duplicates(subset="address")
full_df['Designation Type']= full_df['Designation Type'].fillna(value="Non")
full_df['MUA/P Status Description']= full_df['MUA/P Status Description'].fillna(value="Non")
full_df=full_df[full_df.patients_rating_of_the_facility_linear_mean_score.notnull()]

for col in full_df:
    print(col)
    print(full_df[col].nunique())



full_counts=get_counts(full_df)


mua_df['county_name'].value_counts()
cahps_df['county_name'].value_counts()

full_cols=get_cols(full_df)

