import pandas as pd
from cleanData import mua_df_clean, readm_df_clean, cahps_df_clean
import exploreData

mergedOC_df=cahps_df_clean.merge(readm_df_clean, how='left', on=['facility_name','address','city','county_name','state','zip'])
mergedOC_df=mergedOC_df[mergedOC_df.patients_rating_of_the_facility_linear_mean_score.notnull()]
mergedOC_df=mergedOC_df[mergedOC_df.rate_of_readmission.notnull()]

mergedMUA_df=mergedOC_df.merge(mua_df_clean, how='left', on=['state', 'county_name']).drop_duplicates(subset="address")
mergedMUA_df['is-MUA?']= mergedMUA_df['is-MUA?'].fillna(value="No")
mergedMUA_df['MUA-status-desc']= mergedMUA_df['MUA-status-desc'].fillna(value="Not Designated")
mergedMUA_df['MUA-population-type']= mergedMUA_df['MUA-population-type'].fillna(value="None")


all_counts=exploreData.get_counts(mergedMUA_df)
all_cols=exploreData.get_cols(mergedMUA_df)

all_counts[35] #check dist of is-MUA
all_counts[36] #check dist of MUA-status
all_counts[48] #check dist of MUA-population-type