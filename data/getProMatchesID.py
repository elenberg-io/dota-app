import requests
import pandas as pd
import json


# read in existing match id data
try:
    promatchID_df_exist = pd.read_csv('promatchID.csv')
except pd.errors.EmptyDataError:
    promatchID_df_exist = pd.DataFrame()
    print('There is no existing data in the pro matches ID .csv file')

# get new data for pro matches
total_promatchID_df = pd.DataFrame()
iter_var = 0
for i in range(5964710000, 5964795547, 1000):
    iter_var += 1
    if i % 100 == 0:
        print('Pinging Dota Open API for matches - iteration {}'.format(iter_var))
    # make the API call for match id data
    try:
        promatchID = requests.get('https://api.opendota.com/api/proMatches?less_than_match_id={}'.format(i))

        promatchID = json.loads(promatchID.text)
        promatchID_df = pd.json_normalize(promatchID)
        promatchID_df = promatchID_df[['match_id',
                                       'duration',
                                       'start_time',
                                       'radiant_score',
                                       'dire_score',
                                       'radiant_win']].copy()
        total_promatchID_df = total_promatchID_df.append(promatchID_df, ignore_index=True)
    except KeyError:
        continue

# combine existing and new data for match id's
total_promatchID_df = total_promatchID_df.append(promatchID_df_exist, ignore_index=True)
# total_promatchID_df.drop_duplicates(inplace=True)

# save in csv the combined data of match id's
total_promatchID_df.to_csv('promatchID.csv', index=False)



