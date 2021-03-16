from sdg.open_sdg import open_sdg_build
import pandas as pd

sdmx_mapping=pd.read_csv('sdmx_mapping.csv')

def alter_data(data):
  for col in data.columns:
    if col not in ["Year", "Value"]:
        for i in data.index:
            data.at[i, col]=sdmx_mapping['OpenSDG_itemval'].loc[sdmx_mapping['CSV_itemval']==data.at[i, col]].item()
        newcol=sdmx_mapping['OpenSDG_colval'].loc[sdmx_mapping['CSV_colval']==col].item()
        data.rename(columns={col:newcol}, inplace=True)

  return data

open_sdg_build(config='config_data.yml', alter_data=alter_data)
