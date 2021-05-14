"""
Load game stats data
"""
from csv import DictReader
import pandas as pd
import os
from django.core.management import BaseCommand
from dotaStatsApp.models import GameStats


class Command(BaseCommand):
    help = 'Loads Dota heroes data and stats'

    def handle(self, *args, **options):
        # if GameStats.objects.exists():
        #     print('Game stats data already loaded')
        #     return
        matchData_fp = os.path.join('data', 'output', 'matchData.csv')
        print('Loading match data')
        with open(matchData_fp) as matchData_file:
            for row in DictReader(matchData_file):
                row = {i: (j if len(j) != 0 else None) for i, j in row.items()}
                match_stats = GameStats()
                match_stats.match_id = row['match_id']
                match_stats.start_time = pd.to_datetime(row['start_time'],
                                                        format='%Y-%m-%d %H:%M:%S').tz_localize('UTC')
                match_stats.duration = row['duration']
                match_stats.account_id = row['account_id']
                match_stats.hero_id = row['hero_id']
                match_stats.isRadiant = row['isRadiant']
                match_stats.player_slot = row['player_slot']
                match_stats.level = row['level']
                match_stats.xp_per_min = row['xp_per_min']
                match_stats.league_id = row['leagueid']
                match_stats.radiant_score = row['radiant_score']
                match_stats.dire_score = row['dire_score']
                match_stats.radiant_win = row['radiant_win']
                match_stats.version = row['version']
                match_stats.patch = row['patch']
                match_stats.skill = row['skill']
                match_stats.first_blood_time = row['first_blood_time']
                match_stats.game_mode = row['game_mode']
                match_stats.human_players = row['human_players']
                match_stats.region = row['region']
                match_stats.total_xp = row['total_xp']
                match_stats.last_hits = row['last_hits']
                match_stats.hero_damage = row['hero_damage']
                match_stats.kill_streaks = row['kill_streaks']
                match_stats.hero_healing = row['hero_healing']
                match_stats.total_gold = row['total_gold']
                match_stats.kills = row['kills']
                match_stats.kda = row['kda']
                match_stats.rank_tier = row['rank_tier']
                match_stats.deaths = row['deaths']
                match_stats.randomed = row['randomed']
                match_stats.net_worth = row['net_worth']
                match_stats.tower_damage = row['tower_damage']
                match_stats.kills_per_min = row['kills_per_min']
                match_stats.gold_per_min = row['gold_per_min']
                match_stats.item_0 = row['item_0']
                match_stats.item_1 = row['item_1']
                match_stats.item_2 = row['item_2']
                match_stats.item_3 = row['item_3']
                match_stats.item_4 = row['item_4']
                match_stats.item_5 = row['item_5']
                match_stats.save()
