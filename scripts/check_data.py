from sdg.open_sdg import open_sdg_check
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

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_data=alter_data)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
