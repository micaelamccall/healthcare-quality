import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from combineData import mergedMUA_df
import seaborn as sns
from matplotlib.lines import Line2D


plt_df = mergedMUA_df

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

sns.set_style('white')
sns.set_style('ticks')
b = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "patients_recommending_the_facility_linear_mean_score", hue = "is-MUA?",  palette=["#9b59b6", "#2ecc71"])
sns.despine()
b.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Recommendation of the Facility")
custom = [Line2D([], [], marker='.', color="#9b59b6", linestyle='None'),Line2D([], [], marker='.', color="#2ecc71", linestyle='None')]
plt.legend(custom, ['MUA', 'Not MUA'], loc='lower right')

plt.close()

sns.set_style('white')
sns.set_style('ticks')
c = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "communication_about_your_procedure_linear_mean_score", hue = "is-MUA?",  palette=["#9b59b6", "#e74c3c"])
sns.despine()
c.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Rating of Communication")
custom = [Line2D([], [], marker='.', color="#9b59b6", linestyle='None'),Line2D([], [], marker='.', color="#e74c3c", linestyle='None')]
plt.legend(custom, ['MUA', 'Not MUA'], loc='lower right')

plt.close()

sns.set_style('white')
sns.set_style('ticks')
b = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "patients_recommending_the_facility_linear_mean_score", hue = "MUA-population-type",  palette="muted")
sns.despine()
b.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Recommendation of the Facility")

plt.close()