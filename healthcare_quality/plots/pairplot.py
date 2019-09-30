import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
from healthcare_quality.clean_data import merged_df
import seaborn as sns
from matplotlib.lines import Line2D

# Pairplot to look at the relationship between the CAHPS measures

d = sns.pairplot(merged_df, height = 4, vars=[
    'patients_rating_of_the_facility_linear_mean_score', 
    'patients_recommending_the_facility_linear_mean_score',
    'facilities_and_staff_linear_mean_score', 
    'communication_about_your_procedure_linear_mean_score'], )
replacements = {
    'communication_about_your_procedure_linear_mean_score': 'communication', 
    'patients_recommending_the_facility_linear_mean_score': 'recommendation', 
    'facilities_and_staff_linear_mean_score' : 'facilities+staff',
    'patients_rating_of_the_facility_linear_mean_score': 'overall rating'}
for i in range(3):
    for j in range(3):
        xlabel = d.axes[i][j].get_xlabel()
        ylabel = d.axes[i][j].get_ylabel()
        if xlabel in replacements.keys():
            d.axes[i][j].set_xlabel(replacements[xlabel])
        if ylabel in replacements.keys():
            d.axes[i][j].set_ylabel(replacements[ylabel])


# MUA status is a category that is composed of multiple measures. 
# The following pairplot looks at the relationship between these 4 measures

mua_filter = merged_df[merged_df['Infant Mortality Rate'].notnull()]

sns.pairplot(
    mua_filter, 
    height = 6, 
    vars=[
        'Ratio of Providers per 1000 Population IMU Score',
        'Infant Mortality Rate', 
        'Percent of Population with Incomes at or Below 100 Percent of the U.S. Federal Poverty Level',
        'Percentage of Population Age 65 and Over'],
    hue = "is-MUA?" )
