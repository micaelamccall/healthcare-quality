import pandas as pd 
from sodapy import Socrata

client = Socrata("data.medicare.gov", None)

results = client.get("qk5r-kh7u", limit=5000)

results_df=pd.DataFrame.from_records(results)

metadat = client.get_metadata("r32h-32z5")
[x['name'] for x in metadat['columns']]

[x for x in metadat['columns'] if x['name']=='Measure Name'][0]
[x for x in metadat['columns'] if x['name']=='Score'][0]

results3 = client.get("r32h-32z5", where = "measure_name = 'Rate of readmission after discharge from hospital (hospital-wide)' AND score !='Not Available'", limit = 3000)
results3_df = pd.DataFrame.from_records(results3)

MUA_df= pd.read_csv("https://data.hrsa.gov//DataDownload/DD_Files/MUA_DET.csv")

