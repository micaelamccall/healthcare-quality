import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from combineData import mergedMUA_df
import seaborn as sns
from matplotlib.lines import Line2D


plt_df = mergedMUA_df



d = sns.pairplot(plt_df, height = 4, vars=['patients_rating_of_the_facility_linear_mean_score', 'patients_recommending_the_facility_linear_mean_score', 'communication_about_your_procedure_linear_mean_score'], )
replacements = {'communication_about_your_procedure_linear_mean_score': 'communication', 'patients_recommending_the_facility_linear_mean_score': 'recommendation', 'patients_rating_of_the_facility_linear_mean_score': 'overall rating'}
for i in range(3):
    for j in range(3):
        xlabel = d.axes[i][j].get_xlabel()
        ylabel = d.axes[i][j].get_ylabel()
        if xlabel in replacements.keys():
            d.axes[i][j].set_xlabel(replacements[xlabel])
        if ylabel in replacements.keys():
            d.axes[i][j].set_ylabel(replacements[ylabel])
plt.close()


sns.set_style('white')
sns.set_style('ticks')
a = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "patients_rating_of_the_facility_linear_mean_score", hue = "is-MUA?",  palette=["#9b59b6", "#3498db"])
sns.despine()
a.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Rating of the Facility")
custom = [Line2D([], [], marker='.', color="#9b59b6", linestyle='None'),Line2D([], [], marker='.', color="#3498db", linestyle='None')]
plt.legend(custom, ['MUA', 'Not MUA'], loc='lower right')

plt.close()

