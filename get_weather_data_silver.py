## import package
import requests
import json
import pandas as pd
from datetime import datetime, date
from os.path import exists
from udf import get_element_value

## extract
### file path of src data
src_ds = date.today()
src_file_name = f"""raw_weather_data_{src_ds}.csv"""
src_file_path = f"""./data_bronze/{src_file_name}"""

### read csv
df_src = (
    pd.read_csv(src_file_path)
)

## transform
element_name_mapping_dict = {
    "T":"temperature"
}

df_temperature = (
    get_element_value(df_src=df_src, target_element_name="T")
    .assign(element_description = lambda x:x["element_name"].map(element_name_mapping_dict))
)

## load
### file path of processed data
target_file_name = src_file_name.replace("raw_", "fct_")
target_file_path = f"""./data_silver/{target_file_name}"""

# ### write data to directory
if exists(target_file_path):
    print(f"""{target_file_path} already existed""")
else:
    df_temperature.to_csv(target_file_path, index=False)
    print(f"""{target_file_path} successfully wrote""")
