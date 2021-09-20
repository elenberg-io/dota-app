import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import pairwise_distances_argmin_min
import os

match_data_df = pd.read_csv(r'output\matchData.csv')
heroes_data_df = pd.read_csv(r'output\heroesData.csv')

match_data_df = match_data_df[['duration', 'match_id', 'radiant_win', 'dire_score', 'isRadiant',
                               'radiant_score', 'account_id', 'hero_id', 'player_slot', 'skill']]

merged_data_df = match_data_df.merge(heroes_data_df, left_on='hero_id', right_on='id', how='left')[[
    'match_id', 'radiant_win', 'dire_score', 'isRadiant',
    'radiant_score', 'hero_id', 'player_slot',
    'base_str', 'base_agi', 'base_int']]

merged_data_df['same_team_str'] = merged_data_df.groupby(['match_id', 'isRadiant']).base_str.transform(
    lambda x: x.sum() - x)
merged_data_df['same_team_int'] = merged_data_df.groupby(['match_id', 'isRadiant']).base_int.transform(
    lambda x: x.sum() - x)
merged_data_df['same_team_agi'] = merged_data_df.groupby(['match_id', 'isRadiant']).base_agi.transform(
    lambda x: x.sum() - x)

merged_data_df['enemy_team_str'] = merged_data_df.groupby(['match_id']).base_str.transform(lambda x: x.sum()) - \
                                   merged_data_df.groupby(['match_id', 'isRadiant']).base_str.transform(
                                       lambda x: x.sum())
merged_data_df['enemy_team_int'] = merged_data_df.groupby(['match_id']).base_int.transform(lambda x: x.sum()) - \
                                   merged_data_df.groupby(['match_id', 'isRadiant']).base_int.transform(
                                       lambda x: x.sum())
merged_data_df['enemy_team_agi'] = merged_data_df.groupby(['match_id']).base_agi.transform(lambda x: x.sum()) - \
                                   merged_data_df.groupby(['match_id', 'isRadiant']).base_agi.transform(
                                       lambda x: x.sum())

merged_data_df['won'] = ((merged_data_df.isRadiant == False) & (
        merged_data_df.radiant_win == False)) | ((merged_data_df.isRadiant & merged_data_df.radiant_win))

winning_teams_df = merged_data_df[merged_data_df.won == True].copy()

winning_teams_df.dropna(subset=['same_team_str', 'same_team_int', 'same_team_agi',
                                'enemy_team_str', 'enemy_team_int', 'enemy_team_agi', 'base_str', 'base_agi',
                                'base_int'], inplace=True)

X = winning_teams_df[['same_team_str', 'same_team_int', 'same_team_agi',
                      'enemy_team_str', 'enemy_team_int', 'enemy_team_agi']]
y = winning_teams_df[['base_str', 'base_agi', 'base_int']]

mo_reg = MultiOutputRegressor(LinearRegression()).fit(X, y)

params_reg = pd.DataFrame(data={'base_str': list(mo_reg.estimators_[0].coef_) + [mo_reg.estimators_[0].intercept_],
                                'base_agi': list(mo_reg.estimators_[1].coef_) + [mo_reg.estimators_[1].intercept_],
                                'base_int': list(mo_reg.estimators_[2].coef_) + [mo_reg.estimators_[2].intercept_],
                                }, index=['same_team_str', 'same_team_int', 'same_team_agi',
                                          'enemy_team_str', 'enemy_team_int', 'enemy_team_agi', 'intercept'])
