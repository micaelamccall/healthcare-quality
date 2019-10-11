import pandas as pd

def double_merge(df1, df2, df3, merge1, merge2):
    """ A function to merge 3 datasets using a left merge
    Arguments: 
    df1 =  pandas dataframe of the limiting dataset / want to keep all the columns
    df2, df3 = the other two pandas dataframes 
    merge1 = a list of columns to merge on for the first merge
    merge2 = a list of columns to merge on for the 2nd merge 
    
    Returns: a pandas dataframe of mergerd data
    """

    first_merge = df1.merge(df2, how = 'left', on = merge1)

    second_merge = first_merge.merge(df3, how = 'left', on = merge2)

    return second_merge


def cleanup_merged_df(df):
    """ Function to clean up the merged data
    Argument: the merged data as pandas DataFrame
    Output: Cleaned up merged data as pandas DataFrame"""

    ## This filters out rows where the mean facility rating and rate of readmission are null
    df = df[df.patients_rating_of_the_facility_linear_mean_score.notnull()]
    df = df[df.rate_of_readmission.notnull()].reset_index()

    ## Mark rows that existed in the outcome measure (OC) DataFrame but not in the MUA DataFrame as not being MUAs
    df['is-MUA?'] = df['is-MUA?'].fillna(value="No")
    df['MUA-status-desc'] = df['MUA-status-desc'].fillna(value="Not Designated")
    df['MUA-population-type'] = df['MUA-population-type'].fillna(value="None")
    df['Rural Status Description'] = df['Rural Status Description'].fillna(value="No Info")

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
        df.loc[:,col] = df.loc[:,col].fillna(value=0)


    ## List columns to be integers, floats, and categories
    int_list = ['patients_rating_of_the_facility_linear_mean_score', 'communication_about_your_procedure_linear_mean_score','facilities_and_staff_linear_mean_score', 'number_of_completed_surveys','number_of_sampled_patients', 'patients_recommending_the_facility_linear_mean_score','patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest', 'patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest','patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends','patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends','patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean', 'patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean','patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean','patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends', 'survey_response_rate_percent', 'rate_denominator', 'provider_id']
    float_list = ['rate_of_readmission_higher_estimate', 'rate_of_readmission_lower_estimate', 'rate_of_readmission']
    category_list = ['county_name','state', 'is-MUA?', 'MUA-status-desc', 'MUA-population-type', 'Rural Status Description']

    ## Change data types as above
    for col in int_list:
        df[col] = df[col].astype('int')

    for col in float_list:
        df[col] = df[col].astype('float')

    for col in category_list:
        df[col] = df[col].astype('category')

    return df 