import pandas as pd
from data.getData import cahps_df, mua_df, readm_df
import data.exploreData as exploreData

# Function to use for MUA dataset
def yesno(df, column, yescat):
    """ Turns a categorical variable in a DataFrame into a "yes" or "no" response
    df = pandas DataFrame, 
    column = quoted column name
    yes = quoted *and bracketed* list of category names that you wish to turn to "yes" """
    df[column]=df[column].astype('category')
    
    cat_list=[] 

    for cat in df[column].cat.categories:
        cat_list.append(cat)

    repl_dict = {}

    for cat in cat_list:
        for yes in yescat:
            if cat == yes:
                repl_dict[cat]= "Yes"   
        if repl_dict.get(cat) == None:
            repl_dict[cat]="No"

    df[column] = df[column].replace(repl_dict)

    return df


## CAHPS
# This removes some columns I'm not interested in and renames the county column
cahps_df_clean = cahps_df.drop(columns = ['cms_certification_number','measure_start_date', 'measure_end_date', 'footnote', 'telephone']).rename(columns = {"county":"county_name"})

## Readmission
# This removes some columns I'm not interested in and renames some columns to be more descriptive, e.g. the score to have the column name of the measure name 
readm_df_clean = readm_df.drop(columns = ['footnote','measure_id', 'measure_name','phone_number','location_address','location_city','location_state','location_zip']).rename(columns = {'hospital_name':'facility_name','compared_to_national':'rate_of_readmission_national_comparison','score':'rate_of_readmission', 'denominator':'rate_denominator','higher_estimate':'rate_of_readmission_higher_estimate','lower_estimate':'rate_of_readmission_lower_estimate','zip_code':'zip'})

## MUA
# This drop a bunch of columns from the MUA DataFrame that I'm not interested in 
mua_df_s = mua_df.drop(columns = ['MUA/P ID', 'Common County Name', 'Complete County Name', 'MUA/P Service Area Name','County Description','State Name','U.S. - Mexico Border 100 Kilometer Indicator', 'U.S. - Mexico Border County Indicator','Medically Underserved Area/Population (MUA/P) Metropolitan Indicator.1', 'Medically Underserved Area/Population (MUA/P) Metropolitan Description', 'Medically Underserved Area/Population (MUA/P) Metropolitan Indicator', 'Rural Status Code', 'Designation Type Code', 'Minor Civil Division FIPS Code', 'Minor Civil Division Census Code', 'Minor Civil Division Name', 'MUA/P Status Code', 'Census Tract', 'Designation Date','Designation Date.1', 'State and County Federal Information Processing Standard Code', 'County or County Equivalent Federal Information Processing Standard Code', 'HHS Region Code','HHS Region Name','State FIPS Code', 'Data Warehouse Record Create Date','Data Warehouse Record Create Date Text','Primary State FIPS Code','HPSA Primary State Abbreviation', 'Primary State Name','Primary HHS Region Code','Primary HHS Region Name','Common Region Code','Common Region Name','Common State Name','Common State Abbreviation','Common State FIPS Code','Common State County FIPS Code', 'Break in Designation','Medically Underserved Area/Population (MUA/P) Component Designation Date','Ratio of Providers per 1000 Population','Medically Underserved Area/Population (MUA/P) Component Designation Date.1',  'Medically Underserved Area/Population (MUA/P) Component Geographic Name','Medically Underserved Area/Population (MUA/P) Component Geographic Type Code','Medically Underserved Area/Population (MUA/P) Component Geographic Type Description','Medically Underserved Area Geography Type Surrogate Key','Medically Underserved Area/Population (MUA/P) Component Last Update Date','Medically Underserved Area/Population (MUA/P) Component Status Code','Medically Underserved Area/Population (MUA/P) Component Status Description','Medically Underserved Area/Population (MUA/P) Component Update Date','Designation Population in a Medically Underserved Area/Population (MUA/P)', 'Medically Underserved Area/Population (MUA/P) Population Type ID','Medically Underserved Area/Population (MUA/P) Population Type Code','Medically Underserved Area/Population (MUA/P) Total Resident Civilian Population','Medically Underserved Area/Population (MUA/P) Withdrawal Date','Medically Underserved Area/Population (MUA/P) Withdrawal Date in Text Format', 'Unnamed: 74'])

# Now I want to re-assess which columns are in the MUA DataFrame and which ones I want to rename
mua_cols_clean = exploreData.get_cols(mua_df_s)
mua_counts_clean = exploreData.get_counts(mua_df_s)

# Rename some columns to match up with other DataFrames and be more descriptive
mua_df_p=mua_df_s.rename(columns={'Designation Type':'is-MUA?','MUA/P Status Description':'MUA-status-desc', "County Equivalent Name":"county_name", "State Abbreviation":"state", 'Medically Underserved Area/Population (MUA/P) Population Type': 'MUA-population-type'})

# Change the is-MUA? column to a yes/no category using the yesno() function defined below
mua_df_clean=yesno(mua_df_p, 'is-MUA?', ['Medically Underserved Area'])

# Change the county name to be all uppercase to match the other DataFrames
mua_df_clean['county_name'] = mua_df_clean.county_name.str.upper()



