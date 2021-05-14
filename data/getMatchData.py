"""
Get data for past matches
"""
import requests
import pandas as pd
import json
import os
from mappings import regions_map, game_mode_map, match_cols, player_cols


# get the starting gameID for the API calls
try:
    final_gameID_df = pd.read_csv(os.path.join('output', 'matchData.csv'), usecols=['match_id'])
    if len(final_gameID_df) == 1:
        final_gameID = 5992892504
    else:
        final_gameID = final_gameID_df.min()[0] - 1
except pd.errors.EmptyDataError:
    final_gameID = 5992892504

# instantiate dataframe that will hold API call processed data
total_match_df = pd.DataFrame()
try:
    for match_id in range(final_gameID, final_gameID - 300, -1):
        match = requests.get('https://api.opendota.com/api/matches/{}'.format(match_id))

        match = json.loads(match.text)
        if len(match) == 1:
            continue
        match_df = pd.json_normalize(match)
        match_missing_cols = set(match_cols).difference(match_df.columns)
        match_existing_cols = set(match_cols).intersection(match_df.columns)

        match_df = match_df[match_existing_cols]
        match_missing_df = pd.DataFrame(columns=match_missing_cols)
        match_df = pd.concat([match_df, match_missing_df], 1)

        player_df = pd.DataFrame()
        for player_ID in range(10):
            player_long = pd.json_normalize(match_df.players[0][player_ID])

            missing_cols = set(player_cols).difference(player_long.columns)
            existing_cols = set(player_cols).intersection(player_long.columns)

            player_long_exist = player_long[existing_cols]
            player_long_missing = pd.DataFrame(columns=missing_cols)
            player_long_union = pd.concat([player_long_exist, player_long_missing], 1)

            player_df = player_df.append(player_long_union)

        match_df = match_df.drop('players', 1).merge(player_df, how='cross')
        total_match_df = total_match_df.append(match_df)
    # convert start_time from Unix timestamp to Pandas datetime
    total_match_df['start_time'] = pd.to_datetime(total_match_df['start_time'], unit='s')
    # convert duration from seconds to minutes
    total_match_df['duration'] = (total_match_df['duration'] / 60).round(2)
    # convert first_blood_time from seconds to minutes
    total_match_df['first_blood_time'] = (total_match_df['first_blood_time'] / 60).round(2)
    # map region ID's to region names
    total_match_df['region'] = total_match_df['region'].map(regions_map)
    # convert game mode ID's to game mode names
    total_match_df['game_mode'] = total_match_df['game_mode'].astype(str).map(lambda x: game_mode_map[x]['name'])
    # tens place indicates rank, ones place indicates stars
    total_match_df['rank_tier'] = total_match_df['rank_tier'].map(lambda x: str(x)[0], na_action='ignore')

except Exception as e:
    # generic exception that informs the user what issue arose
    print('Encountered error ' + str(e))
finally:
    # regardless of how many API calls were successful save the data downloaded up until that point to output
    with open(os.path.join('output', 'matchData.csv'), 'w') as file_matches:
        file_matches.write(total_match_df.to_csv(index=False))
