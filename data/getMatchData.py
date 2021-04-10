import requests
import pandas as pd
import json


# read in match id data
matchID_df = pd.read_csv('promatchID.csv')
matchID_list = matchID_df['match_id'].to_list()
total_matches_df = pd.DataFrame()

for i in matchID_list[:2]:
    match = requests.get("https://api.opendota.com/api/matches/{}".format(i))
    match = json.loads(match.text)
    match_df = pd.json_normalize(match)
    match_df = match_df[['match_id',
                         'first_blood_time',
                         'game_mode',
                         'human_players',
                         'objectives',
                         'version',
                         'patch',
                         'players',
                         'objectives',
                         'radiant_gold_adv',
                         'radiant_xp_adv',
                         'skill',
                         'region']].copy()
    total_matches_df = total_matches_df.append(match_df, ignore_index=True)

total_matches_df.to_csv('matchData.csv', index=False)