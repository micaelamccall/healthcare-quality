import pandas as pd 
import requests
import json

auth = ('9asut06cuhbleteyw87dhfibv', '4bllkisduibcmxokd9r9xv0bkiwo3a2lhl87oz14yflogimhzf')

queries = [["https://data.medicare.gov/resource/qk5r-kh7u.json?$limit=5000", pd.DataFrame()], ["https://data.medicare.gov/resource/r32h-32z5.json?$limit=5000&$where=measure_name= 'Rate of readmission after discharge from hospital (hospital-wide)' AND score != 'Not Available'", pd.DataFrame()]]


for query in queries:
    r=requests.get(query[0], auth=auth).json()
    query[1] = pd.DataFrame.from_records(r)

cahps_df = queries[0][1]
readm_df = queries[1][1]

mua_df= pd.read_csv("https://data.hrsa.gov//DataDownload/DD_Files/MUA_DET.csv")

