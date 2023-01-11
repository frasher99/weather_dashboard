## import package
import requests
import json
import pandas as pd
from datetime import datetime, date
from os.path import exists

## extract
### get weather data thru API
authorization = "CWB-363ED938-B2F2-415A-B5C7-97933ECB8F92"
url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091"
res = requests.get(url, {"Authorization": authorization})
res_json = res.json()

## transform
### extract values from json
results = []

locations = res_json["records"]["locations"][0]["location"]
for location in locations:
    city = location["locationName"]
    for i in range(len(location["weatherElement"])):
        result = {
            "city":city,
            "measurement":location["weatherElement"][i] ## iter thru then store every measurement for each city
            }
        results.append(result)

### transform to panda dataframe
schemas = {
    "city":str,
    "measurement":str,
    "element_name":str,
    "description":str,
    "ds":"datetime64[ns]"
}

df_bronze = (
    pd.DataFrame(results)
    .assign(element_name = lambda x:x["measurement"].apply(lambda xx:xx["elementName"]))
    .assign(description = lambda x:x["measurement"].apply(lambda xx:xx["description"]))
    .assign(ds = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    .astype(schemas)
)

## load
### set up file path
target_ds = date.today()
target_file_name = f"""raw_weather_data_{target_ds}.csv"""
target_file_path = f"""./data_bronze/{target_file_name}"""

### write data to directory
if exists(target_file_path):
    print(f"""{target_file_path} already existed""")
else:
    df_bronze.to_csv(target_file_path, index=False)
    print(f"""{target_file_path} successfully wrote""")
