import matplotlib.pyplot as plt
from combineData import mergedOC_df, mergedMUA_df
import seaborn as sns

qual = mergedMUA_df
sns.set(style='white')
sns.relplot(data = qual, x = "rate_of_readmission", y = "patients_rating_of_the_facility_linear_mean_score", hue = "is-MUA?")