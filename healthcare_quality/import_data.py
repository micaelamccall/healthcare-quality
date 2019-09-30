import pandas as pd 
import requests
import json

API_TOKEN=''
API_SECRET=''

try:
    from private import *
except Exception: 
    pass

auth = (API_TOKEN, API_SECRET)

queries = [["https://data.medicare.gov/resource/qk5r-kh7u.json?$limit=5000", pd.DataFrame()], ["https://data.medicare.gov/resource/r32h-32z5.json?$limit=5000&$where=measure_name= 'Rate of readmission after discharge from hospital (hospital-wide)' AND score != 'Not Available'", pd.DataFrame()]]


for query in queries:
    if len(API_TOKEN)>0:
        r=requests.get(query[0], auth=auth).json()
        query[1] = pd.DataFrame.from_records(r)
    else:
        r=requests.get(query[0]).json()
        query[1] = pd.DataFrame.from_records(r)
        print("Querying SODA API without auth")


cahps_df = queries[0][1]
readm_df = queries[1][1]

mua_df= pd.read_csv("https://data.hrsa.gov//DataDownload/DD_Files/MUA_DET.csv")

