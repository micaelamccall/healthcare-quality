import plotly.graph_objects as go
from CAHPSresp import grp_df

# Get statewide count sums
grp_df=grp_df.groupby(by='state').sum().reset_index()


def plot_resp_by_state(columns, names, graphTitle):
    """Plots the proportion of patients who gave each response to a survey question
    args:
    columns = bracketed list of column names
    names = bracketed list of column names to-be
    graphTilte = string"""

    # create dict of current and to-be column names 
    name_dict={}

    for i, col in enumerate(columns):
        name_dict[col]=names[i]
    
    # add the following two columns to column list
    col_list=['state','number_of_completed_surveys']
    col_list.extend(columns)

    # create new df from grp_df and rename columns
    df=grp_df[col_list].rename(columns=name_dict)

    # change measure from count to proportion of total surveyed patients
    l=len(col_list)
    df.iloc[:,2:l]=df.values[:,2:l]/df.values[:,1,None]

    # restructure DataFrame
    df=df.melt(id_vars='state', value_vars=names, var_name='rating', value_name='proportion of patients')

    # create plot
    fig = go.Figure(data=[go.Box(x=df['rating'], y=df['proportion of patients'], boxpoints='all', jitter=0.5, width=.3, hoverinfo='text', hovertext=comm_df['state'])])
    fig.update_layout(title_text=graphTitle, template="plotly_white")
    fig.update_xaxes(title_text="response")
    fig.update_yaxes(title_text="proportion of patients")
    fig.show()


# create a list of column lists, a list of name lists, and a list of graph ttiles for 4 measures

columns=[['patients_who_reported_that_staff_did_not_communicate_about_what_to_expect_during_and_after_the_procedure','patients_who_reported_that_staff_somewhat_communicated_about_what_to_expect_during_and_after_the_procedure', 'patients_who_reported_that_staff_definitely_communicated_about_what_to_expect_during_and_after_the_procedure'],
['patients_who_reported_no_they_would_not_recommend_the_facility_to_family_or_friends','patients_who_reported_probably_yes_they_would_recommend_the_facility_to_family_or_friends','patients_who_reported_yes_they_would_definitely_recommend_the_facility_to_family_or_friends'],
['patients_who_reported_that_staff_did_not_give_care_in_a_professional_way_or_the_facility_was_not_clean','patients_who_reported_that_staff_somewhat_gave_care_in_a_professional_way_or_the_facility_was_somewhat_clean','patients_who_reported_that_staff_definitely_gave_care_in_a_professional_way_and_the_facility_was_clean'],
['patients_who_gave_the_facility_a_rating_of_0_to_6_on_a_scale_from_0_lowest_to_10_highest','patients_who_gave_the_facility_a_rating_of_7_or_8_on_a_scale_from_0_lowest_to_10_highest','patients_who_gave_the_facility_a_rating_of_9_or_10_on_a_scale_from_0_lowest_to_10_highest']]
names_list=[['not at all', 'somewhat', 'definitely'],
['no','probably', 'yes definitely'],
['not at all', 'somewhat', 'definitely'],
['0-6','7-8','9-10']]
graphTitle_list=["Patient Ratings of Staff Communication about the Procedure", "Patient Ratings of If They Would Recommend the Facility", "Patient Ratings of Professional Care and Facility Cleanliness","Overall Rating of the Facility (scale from 0 lowest to 10 highest)"]


# plot each of 4 measures

for i, o in enumerate(columns):
    columns=o
    names=names_list[i]
    graphTitle=graphTitle_list[i]
    plot_resp_by_state(columns, names, graphTitle)