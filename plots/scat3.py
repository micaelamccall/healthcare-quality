import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data.combine import mergedMUA_df
import seaborn as sns
from matplotlib.lines import Line2D


plt_df = mergedMUA_df


MUAdf_for_viz = mergedMUA_df.iloc[:,[0,1,3,5,22,35,36,37,40,41,42,44,45,46,47,48,49]]
MUAdf_for_viz = MUAdf_for_viz[MUAdf_for_viz['Infant Mortality Rate'].notnull()]















sns.set_style('white')
sns.set_style('ticks')
b = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "patients_recommending_the_facility_linear_mean_score", hue = "Rural Status Description",  palette="muted")
sns.despine()
b.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Recommendation of the Facility")

plt.close()


sns.set_style('white')
sns.set_style('ticks')
b = sns.scatterplot(data = plt_df, x = "rate_of_readmission", y = "patients_recommending_the_facility_linear_mean_score", hue = "MUA-population-type",  palette="muted")
sns.despine()
b.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xlabel("Readmission Rate")
plt.ylabel("Patients' Mean Recommendation of the Facility")

plt.close()


