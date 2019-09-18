import pandas as pd 
import requests
import json

auth = ('9asut06cuhbleteyw87dhfibv', '4bllkisduibcmxokd9r9xv0bkiwo3a2lhl87oz14yflogimhzf')

url = "https://data.medicare.gov/resource/qk5r-kh7u.json"
r=requests.get(url, auth=auth).json()
cahps_df = pd.DataFrame.from_records(r)

url2 = "https://data.medicare.gov/resource/r32h-32z5.json?$where=measure_name = 'Rate of readmission after discharge from hospital (hospital-wide)' AND score != 'Not Available'"
r2=requests.get(url2, auth=auth).json()
readm_df = pd.DataFrame.from_records(r2)

mua_df= pd.read_csv("https://data.hrsa.gov//DataDownload/DD_Files/MUA_DET.csv")

