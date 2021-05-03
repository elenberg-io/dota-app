"""
Get heroes static data, like base health, mana, armor, etc.
"""
import requests
import pandas as pd
import json
import os

heroes_map_raw = requests.get('https://api.opendota.com/api/constants/hero_names')
heroes_map = json.loads(heroes_map_raw.text)
heroes_df = pd.json_normalize(heroes_map, max_level=0)
heroes_df = heroes_df.T
heroes_df.columns = ['json_field']
heroes_df['id'] = heroes_df.json_field.apply(lambda x: dict(x)['id'])
heroes_df['localized_name'] = heroes_df.json_field.apply(lambda x: dict(x)['localized_name'])
heroes_df['roles'] = heroes_df.json_field.apply(lambda x: dict(x)['roles'])
heroes_df['primary_attr'] = heroes_df.json_field.apply(lambda x: dict(x)['primary_attr'])
heroes_df['attack_type'] = heroes_df.json_field.apply(lambda x: dict(x)['attack_type'])
heroes_df['base_health'] = heroes_df.json_field.apply(lambda x: dict(x)['base_health'])
heroes_df['base_health_regen'] = heroes_df.json_field.apply(lambda x: dict(x)['base_health_regen'])
heroes_df['base_mana'] = heroes_df.json_field.apply(lambda x: dict(x)['base_mana'])
heroes_df['base_mana_regen'] = heroes_df.json_field.apply(lambda x: dict(x)['base_mana_regen'])
heroes_df['base_armor'] = heroes_df.json_field.apply(lambda x: dict(x)['base_armor'])
heroes_df['base_str'] = heroes_df.json_field.apply(lambda x: dict(x)['base_str'])
heroes_df['base_agi'] = heroes_df.json_field.apply(lambda x: dict(x)['base_agi'])
heroes_df['base_int'] = heroes_df.json_field.apply(lambda x: dict(x)['base_int'])
heroes_df['str_gain'] = heroes_df.json_field.apply(lambda x: dict(x)['str_gain'])
heroes_df['agi_gain'] = heroes_df.json_field.apply(lambda x: dict(x)['agi_gain'])
heroes_df['int_gain'] = heroes_df.json_field.apply(lambda x: dict(x)['int_gain'])
heroes_df['attack_range'] = heroes_df.json_field.apply(lambda x: dict(x)['attack_range'])
heroes_df['attack_rate'] = heroes_df.json_field.apply(lambda x: dict(x)['attack_rate'])
heroes_df['move_speed'] = heroes_df.json_field.apply(lambda x: dict(x)['move_speed'])
heroes_df['img_sb'] = heroes_df.json_field.apply(
    lambda x: 'https://cdn.dota2.com' + dict(x)['img'].split("full.png")[0] + "sb.png")
heroes_df['img_full'] = heroes_df.json_field.apply(
    lambda x: 'https://cdn.dota2.com' + dict(x)['img'].split("full.png")[0] + "full.png")
heroes_df['img_vert'] = heroes_df.json_field.apply(
    lambda x: 'https://cdn.dota2.com' + dict(x)['img'].split("full.png")[0] + "vert.jpg")
heroes_df.drop('json_field', 1, inplace=True)
heroes_df.index = heroes_df.index.map(lambda x: x.split('npc_dota_hero_')[1])

heroes_df.to_csv(os.path.join('output', 'heroesData.csv'))
