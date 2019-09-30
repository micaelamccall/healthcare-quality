import pandas as pd
from healthcare_quality.import_data import cahps_df, mua_df, readm_df
import healthcare_quality.cleaning.explore as explore
from healthcare_quality.cleaning.binarize import binarize_categorical_variable
from healthcare_quality.cleaning.combine import double_merge
import os
import sys
sys.path.append(os.path.abspath("healthcare_quality"))

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

## This filters out rows where the mean facility rating and rate of readmission are null
merged_df = merged_df[merged_df.patients_rating_of_the_facility_linear_mean_score.notnull()]
merged_df = merged_df[merged_df.rate_of_readmission.notnull()].reset_index()

## Mark rows that existed in the outcome measure (OC) DataFrame but not in the MUA DataFrame as not being MUAs
merged_df['is-MUA?'] = merged_df['is-MUA?'].fillna(value="No")
merged_df['MUA-status-desc'] = merged_df['MUA-status-desc'].fillna(value="Not Designated")
merged_df['MUA-population-type'] = merged_df['MUA-population-type'].fillna(value="None")
merged_df['Rural Status Description'] = merged_df['Rural Status Description'].fillna(value="No Info")

# Fill missing count values with 0 (0 respondents)
fill_list=[
    'number_of_completed_surveys',
    'number_of_sampled_patients',
    'patients_rating_of_the_facility_linear_mean_score',
    'patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest',
    'patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest',
    'patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest',
    'patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends',
    'patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends',
    'patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure',
    'patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean',
    'patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure',
    'patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean',
    'patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure',
    'patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean',
    'patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends']

for col in fill_list:
    merged_df.loc[:,col] = merged_df.loc[:,col].fillna(value=0)


# Check columns and counts of merged MUA DataFrame
all_counts = explore.get_counts(merged_df)
all_cols = explore.get_cols(merged_df)

all_counts[35] #check dist of is-MUA
all_counts[36] #check dist of MUA-status
all_counts[48] #check dist of MUA-population-type

# Check merged MUA data types
merged_df.dtypes

## List columns to be integers, floats, and categories
int_list = ['patients_rating_of_the_facility_linear_mean_score', 'communication_about_your_procedure_linear_mean_score','facilities_and_staff_linear_mean_score', 'number_of_completed_surveys','number_of_sampled_patients', 'patients_recommending_the_facility_linear_mean_score','patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest','patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends','patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends','patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean', 'patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean','patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean','patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends', 'survey_response_rate_percent', 'rate_denominator', 'provider_id']
float_list = ['rate_of_readmission_higher_estimate', 'rate_of_readmission_lower_estimate', 'rate_of_readmission']
category_list = ['county_name','state', 'is-MUA?', 'MUA-status-desc', 'MUA-population-type', 'Rural Status Description']


## Change data types as above
for col in int_list:
    merged_df[col] = merged_df[col].astype('int')

for col in float_list:
    merged_df[col] = merged_df[col].astype('float')

for col in category_list:
    merged_df[col] = merged_df[col].astype('category')