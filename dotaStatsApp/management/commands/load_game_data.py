from csv import DictReader
from datetime import datetime
import os

from django.core.management import BaseCommand

from dotaStatsApp.models import Heroes, GameStats


class Command(BaseCommand):
    help = 'Loads Dota heroes data and stats into the Heroes and GameStats models'

    def handle(self, *args, **options):
        if Heroes.objects.exists() or GameStats.objects.exists():
            return
        matchID_fp = os.path.join('data', 'promatchID.csv')
        matchData_fp = os.path.join('data', 'matchData.csv')
        print('Loading Dota match data')

        with open(matchID_fp) as matchID_file:
            for row in DictReader(matchID_file):
                match = Games()
                match.match_id = row['match_id']
                match.duration = row['duration']
                match.start_time = row['start_time']
                match.radiant_score = row['radiant_score']
                match.dire_score = row['dire_score']
                match.radiant_win = row['radiant_win']
                match.save()

        with open(matchData_fp) as matchData_file:
            for row in DictReader(matchData_file):
                match_stats = GameStats()
                match_stats.match_id = row['match_id']
                match_stats.first_blood_time = row['first_blood_time']
                match_stats.game_mode = row['game_mode']
                match_stats.human_players = row['human_players']
                match_stats.version = row['version']
                match_stats.patch = row['patch']
                match_stats.players = row['players']
                match_stats.objectives = row['objectives']
                match_stats.radiant_gold_adv = row['radiant_gold_adv']
                match_stats.radiant_xp_adv = row['radiant_xp_adv']
                match_stats.skill = row['skill']
                match_stats.region = row['region']
                match_stats.save()

