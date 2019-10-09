import pandas as pd
from healthcare_quality.import_data import cahps_df, mua_df, readm_df
import healthcare_quality.cleaning.explore as explore
from healthcare_quality.cleaning.binarize import binarize_categorical_variable
from healthcare_quality.cleaning.combine import double_merge, cleanup_merged_df


## CAHPS
# This removes some columns I'm not interested in and renames the county column
cahps_df_clean = cahps_df.drop(
    columns = [
        'cms_certification_number',
        'measure_start_date', 
        'measure_end_date', 
        'footnote', 'telephone'
        ]).rename(
            columns = {"county":"county_name"})



## Readmission
# This removes some columns I'm not interested in and renames some columns to be more descriptive, e.g. the score to have the column name of the measure name 
readm_df_clean = readm_df.drop(
    columns = [
        'footnote',
        'measure_id', 
        'measure_name',
        'phone_number',
        'location_address',
        'location_city',
        'location_state',
        'location_zip'
        ]).rename(
            columns = {
                'hospital_name':'facility_name',
                'compared_to_national':'rate_of_readmission_national_comparison',
                'score':'rate_of_readmission', 
                'denominator':'rate_denominator',
                'higher_estimate':'rate_of_readmission_higher_estimate',
                'lower_estimate':'rate_of_readmission_lower_estimate',
                'zip_code':'zip'})




## MUA
# This drop a bunch of columns from the MUA DataFrame that I'm not interested in 
mua_df_clean= mua_df.drop(
    columns = [
        'MUA/P ID', 
        'Common County Name', 
        'Complete County Name', 
        'MUA/P Service Area Name',
        'County Description',
        'State Name',
        'U.S. - Mexico Border 100 Kilometer Indicator', 
        'U.S. - Mexico Border County Indicator',
        'Medically Underserved Area/Population (MUA/P) Metropolitan Indicator.1', 
        'Medically Underserved Area/Population (MUA/P) Metropolitan Description', 
        'Medically Underserved Area/Population (MUA/P) Metropolitan Indicator', 
        'Rural Status Code', 
        'Designation Type Code', 
        'Minor Civil Division FIPS Code', 
        'Minor Civil Division Census Code', 
        'Minor Civil Division Name', 
        'MUA/P Status Code', 
        'Census Tract', 
        'Designation Date',
        'Designation Date.1', 
        'State and County Federal Information Processing Standard Code', 
        'County or County Equivalent Federal Information Processing Standard Code', 
        'HHS Region Code',
        'HHS Region Name',
        'State FIPS Code', 
        'Data Warehouse Record Create Date',
        'Data Warehouse Record Create Date Text',
        'Primary State FIPS Code',
        'HPSA Primary State Abbreviation', 
        'Primary State Name',
        'Primary HHS Region Code',
        'Primary HHS Region Name',
        'Common Region Code',
        'Common Region Name',
        'Common State Name',
        'Common State Abbreviation',
        'Common State FIPS Code',
        'Common State County FIPS Code', 
        'Break in Designation',
        'Medically Underserved Area/Population (MUA/P) Component Designation Date',
        'Ratio of Providers per 1000 Population',
        'Medically Underserved Area/Population (MUA/P) Component Designation Date.1',  
        'Medically Underserved Area/Population (MUA/P) Component Geographic Name',
        'Medically Underserved Area/Population (MUA/P) Component Geographic Type Code',
        'Medically Underserved Area/Population (MUA/P) Component Geographic Type Description',
        'Medically Underserved Area Geography Type Surrogate Key',
        'Medically Underserved Area/Population (MUA/P) Component Last Update Date',
        'Medically Underserved Area/Population (MUA/P) Component Status Code',
        'Medically Underserved Area/Population (MUA/P) Component Status Description',
        'Medically Underserved Area/Population (MUA/P) Component Update Date',
        'Designation Population in a Medically Underserved Area/Population (MUA/P)', 
        'Medically Underserved Area/Population (MUA/P) Population Type ID',
        'Medically Underserved Area/Population (MUA/P) Population Type Code',
        'Medically Underserved Area/Population (MUA/P) Total Resident Civilian Population',
        'Medically Underserved Area/Population (MUA/P) Withdrawal Date',
        'Medically Underserved Area/Population (MUA/P) Withdrawal Date in Text Format', 
        'Unnamed: 74'
        ]).rename(
            columns={
                'Designation Type':'is-MUA?',
                'MUA/P Status Description':'MUA-status-desc', 
                'County Equivalent Name' : 'county_name',
                'State Abbreviation' : 'state',
                'Medically Underserved Area/Population (MUA/P) Population Type': 'MUA-population-type'})



# Change the is-MUA? column to a yes/no category using the function from binarize
mua_df_clean=binarize_categorical_variable(mua_df_clean, 'is-MUA?', ['Medically Underserved Area'])

# Change the county name to be all uppercase to match the other DataFrames
mua_df_clean['county_name'] = mua_df_clean.county_name.str.upper()


## Merge 3 datasets 

merge1=['facility_name','address','city','county_name','state','zip'] #the columns on which to merge cahps_df_clean and readm_df_clean
merge2=['state', 'county_name'] #the column on which to merge mua_df_clean with the other two

merged_df=double_merge(cahps_df_clean, readm_df_clean, mua_df_clean, merge1, merge2).drop_duplicates(subset="address")

# Cleanup merged data
merged_df=cleanup_merged_df(merged_df)


if __name__ == "__main__":

    # Check columns and counts of merged MUA DataFrame
    all_counts = explore.get_counts(merged_df)
    all_cols = explore.get_cols(merged_df)

    all_counts[35] #check dist of is-MUA
    all_counts[36] #check dist of MUA-status
    all_counts[48] #check dist of MUA-population-type

    # Check merged MUA data types
    merged_df.dtypes
