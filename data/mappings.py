# This file contains static mappings

# map the region ID's to region names
regions_map = {0: 'unspecified',
               1: 'North America',
               2: 'North America',
               3: 'Europe',
               8: 'Europe',
               9: 'Europe',
               11: 'Europe',
               5: 'SE Asia',
               6: 'SE Asia',
               7: 'SE Asia',
               12: 'SE Asia',
               16: 'SE Asia',
               19: 'SE Asia',
               37: 'SE Asia',
               13: 'China',
               17: 'China',
               18: 'China',
               20: 'China',
               25: 'China',
               10: 'South America',
               14: 'South America',
               15: 'South America',
               }

# map the game_mode ID's to game_mode names
game_mode_map = {
    "0": {
        "id": 0,
        "name": "game_mode_unknown",
        "balanced": True
    },
    "1": {
        "id": 1,
        "name": "game_mode_all_pick",
        "balanced": True
    },
    "2": {
        "id": 2,
        "name": "game_mode_captains_mode",
        "balanced": True
    },
    "3": {
        "id": 3,
        "name": "game_mode_random_draft",
        "balanced": True
    },
    "4": {
        "id": 4,
        "name": "game_mode_single_draft",
        "balanced": True
    },
    "5": {
        "id": 5,
        "name": "game_mode_all_random",
        "balanced": True
    },
    "6": {
        "id": 6,
        "name": "game_mode_intro"
    },
    "7": {
        "id": 7,
        "name": "game_mode_diretide"
    },
    "8": {
        "id": 8,
        "name": "game_mode_reverse_captains_mode"
    },
    "9": {
        "id": 9,
        "name": "game_mode_greeviling"
    },
    "10": {
        "id": 10,
        "name": "game_mode_tutorial"
    },
    "11": {
        "id": 11,
        "name": "game_mode_mid_only"
    },
    "12": {
        "id": 12,
        "name": "game_mode_least_played",
        "balanced": True
    },
    "13": {
        "id": 13,
        "name": "game_mode_limited_heroes"
    },
    "14": {
        "id": 14,
        "name": "game_mode_compendium_matchmaking"
    },
    "15": {
        "id": 15,
        "name": "game_mode_custom"
    },
    "16": {
        "id": 16,
        "name": "game_mode_captains_draft",
        "balanced": True
    },
    "17": {
        "id": 17,
        "name": "game_mode_balanced_draft",
        "balanced": True
    },
    "18": {
        "id": 18,
        "name": "game_mode_ability_draft"
    },
    "19": {
        "id": 19,
        "name": "game_mode_event"
    },
    "20": {
        "id": 20,
        "name": "game_mode_all_random_death_match"
    },
    "21": {
        "id": 21,
        "name": "game_mode_1v1_mid"
    },
    "22": {
        "id": 22,
        "name": "game_mode_all_draft",
        "balanced": True
    },
    "23": {
        "id": 23,
        "name": "game_mode_turbo"
    },
    "24": {
        "id": 24,
        "name": "game_mode_mutation"
    }
}

match_cols = ['match_id',
              'radiant_win',
              'start_time',
              'duration',
              'region',
              'version',
              'patch',
              'leagueid',
              'skill',
              'game_mode',
              'human_players',
              'radiant_score',
              'dire_score',
              'first_blood_time',
              'objectives',
              'players'
              ]

player_cols = ['player_slot',
               'isRadiant',
               'account_id',
               'gold_per_min',
               'hero_damage',
               'hero_healing',
               'hero_id',
               'kill_streaks',
               'kills',
               'kills_per_min',
               'deaths',
               'kda',
               'last_hits',
               'level',
               'total_gold',
               'net_worth',
               'tower_damage',
               'xp_per_min',
               'total_xp',
               'rank_tier',
               'randomed',
               'item_0',
               'item_1',
               'item_2',
               'item_3',
               'item_4',
               'item_5']

item_cols = ['id',
             'dname',
             'cost',
             'notes',
             'lore',
             'img']
