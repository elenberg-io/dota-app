"""
Get items static data, like cost, notes, description, etc.
"""
import requests
import pandas as pd
import json
import os
from static.mappings import item_cols

items_map_raw = requests.get('https://api.opendota.com/api/constants/items')
items_map = json.loads(items_map_raw.text)
items_df = pd.json_normalize(items_map, max_level=0)
items_df = items_df.T
items_df.columns = ['json_field']


items_clean_df = pd.DataFrame()
for index, row in items_df.iterrows():
    item_row = pd.json_normalize(row, max_level=0)
    missing_cols = set(item_cols).difference(item_row.columns)
    existing_cols = set(item_cols).intersection(item_row.columns)
    item_row = item_row[existing_cols]
    item_missing = pd.DataFrame(columns=missing_cols)
    item_row_union = pd.concat([item_row, item_missing], 1)
    items_clean_df = items_clean_df.append(item_row_union)
items_clean_df = items_clean_df[item_cols]
items_clean_df['img'] = items_clean_df['img'].apply(lambda x: 'https://cdn.dota2.com' + x.split("?")[0])
items_clean_df.to_csv(os.path.join('output', 'itemsData.csv'), index=False)
