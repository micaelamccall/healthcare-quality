import pandas as pd
from data.clean import mua_df_clean, readm_df_clean, cahps_df_clean
import data.explore as explore

# Merge readmission and patient report outcome measure DataFrames
mergedOC_df = cahps_df_clean.merge(readm_df_clean, how='left', on=['facility_name','address','city','county_name','state','zip'])
## This filters out rows where the mean facility rating and rate of readmission are null
mergedOC_df = mergedOC_df[mergedOC_df.patients_rating_of_the_facility_linear_mean_score.notnull()]
mergedOC_df = mergedOC_df[mergedOC_df.rate_of_readmission.notnull()]

# Merge outcome measure and MUA datasets 
mergedMUA_df = mergedOC_df.merge(mua_df_clean, how='left', on=['state', 'county_name']).drop_duplicates(subset="address")
## Mark rows that existed in the outcome measure (OC) DataFrame but not in the MUA DataFrame as not being MUAs
mergedMUA_df['is-MUA?'] = mergedMUA_df['is-MUA?'].fillna(value="No")
mergedMUA_df['MUA-status-desc'] = mergedMUA_df['MUA-status-desc'].fillna(value="Not Designated")
mergedMUA_df['MUA-population-type'] = mergedMUA_df['MUA-population-type'].fillna(value="None")
mergedMUA_df['Rural Status Description'] = mergedMUA_df['Rural Status Description'].fillna(value="No Info")

# Fill missing count values with 0 (0 respondents)
fill_list=['number_of_completed_surveys','number_of_sampled_patients','patients_rating_of_the_facility_linear_mean_score','patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest','patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest','patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest','patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends','patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends','patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean','patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean','patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean','patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends']
for col in fill_list:
    mergedMUA_df.loc[:,col] = mergedMUA_df.loc[:,col].fillna(value=0)

# Check columns and counts of merged MUA DataFrame
all_counts = explore.get_counts(mergedMUA_df)
all_cols = explore.get_cols(mergedMUA_df)

all_counts[35] #check dist of is-MUA
all_counts[36] #check dist of MUA-status
all_counts[48] #check dist of MUA-population-type

# Check merged MUA data types
mergedMUA_df.dtypes

## List columns to be integers, floats, and categories
int_list = ['patients_rating_of_the_facility_linear_mean_score', 'communication_about_your_procedure_linear_mean_score','facilities_and_staff_linear_mean_score', 'number_of_completed_surveys','number_of_sampled_patients', 'patients_recommending_the_facility_linear_mean_score','patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest','patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends','patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends','patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean', 'patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean','patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean','patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends', 'survey_response_rate_percent', 'rate_denominator', 'provider_id']
float_list = ['rate_of_readmission_higher_estimate', 'rate_of_readmission_lower_estimate', 'rate_of_readmission']
category_list = ['county_name','state', 'is-MUA?', 'MUA-status-desc', 'MUA-population-type', 'Rural Status Description']

## Change data types as above
for col in int_list:
    mergedMUA_df[col] = mergedMUA_df[col].astype('int')

for col in float_list:
    mergedMUA_df[col] = mergedMUA_df[col].astype('float')

for col in category_list:
    mergedMUA_df[col] = mergedMUA_df[col].astype('category')