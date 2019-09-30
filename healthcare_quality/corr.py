from healthcare_quality.clean_data import merged_df
import pandas as pd

corr = {
    "readmission rate" : merged_df.corr()['rate_of_readmission'], 
    "recommendation" : merged_df.corr()['patients_recommending_the_facility_linear_mean_score'], 
    "overall rating" : merged_df.corr()['patients_rating_of_the_facility_linear_mean_score']}
corr = pd.DataFrame(corr)


