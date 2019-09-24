from data.combine import mergedMUA_df

location_df=mergedMUA_df[mergedMUA_df['location'].notnull()].reset_index()

for i, row in location_df.iterrows():
    location_df.loc[i,'lat']=row['location']['coordinates'][1]
    location_df.loc[i,'lon']=row['location']['coordinates'][0]


