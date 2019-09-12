import pandas as pd 
from sodapy import Socrata

client = Socrata("data.medicare.gov", None)

results = client.get("v7vx-dht4", limit=2000)

results_df=pd.DataFrame.from_records(results)