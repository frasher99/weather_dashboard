import pandas as pd
import numpy as np
import json

##
def get_element_value(df_src: pd.DataFrame, target_element_name: str) -> pd.DataFrame:

    ##
    cities = df_src["city"].unique().tolist()
    
    ##
    results = []
    for city in cities:
    
        ## filter raw data
        c1 = (df_src["city"]==city)
        c2 = (df_src["element_name"]==target_element_name)
        _df = df_src[c1 & c2].copy()
        
        ## trun json to dict
        measurement_dict = eval(json.loads(json.dumps(_df["measurement"].values[0]))) ## assure correct json format
        
        for d in measurement_dict["time"]:
            result = {
                "city":city,
                "start_time":d["startTime"],
                "end_time":d["endTime"],
                "value":d["elementValue"][0]["value"],
                "element_name":target_element_name,
                }
            results.append(result)

    return pd.DataFrame(results)
