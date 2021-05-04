from csv import DictReader
import os

from django.core.management import BaseCommand

from dotaStatsApp.models import Heroes, GameStats


class Command(BaseCommand):
    help = 'Loads Dota heroes data and stats'

    def handle(self, *args, **options):
        if Heroes.objects.exists() or GameStats.objects.exists():
            return
        heroes_fp = os.path.join('data', 'heroesData.csv')
        matchData_fp = os.path.join('data', 'matchData.csv')
        print('Loading Dota heroes and match data')

        with open(heroes_fp) as heroes_file:
            for row in DictReader(heroes_file):
                hero = Heroes()
                hero.hero_id = row['hero_id']
                hero.localized_name = row['localized_name']
                hero.roles = row['roles']
                hero.primary_attr = row['primary_attr']
                hero.attack_type = row['attack_type']
                hero.base_health = row['base_health']
                hero.base_health_regen = row['base_health_regen']
                hero.base_mana = row['base_mana']
                hero.base_mana_regen = row['base_mana_regen']
                hero.base_armor = row['base_armor']
                hero.base_str = row['base_str']
                hero.base_agi = row['base_agi']
                hero.base_int = row['base_int']
                hero.str_gain = row['str_gain']
                hero.agi_gain = row['agi_gain']
                hero.int_gain = row['int_gain']
                hero.attack_range = row['attack_range']
                hero.attack_rate = row['attack_rate']
                hero.move_speed = row['move_speed']
                hero.save()

        with open(matchData_fp) as matchData_file:
            for row in DictReader(matchData_file):
                match_stats = GameStats()
                match_stats.match_id = row['match_id']
                match_stats.start_time = row['start_time']
                match_stats.duration = row['duration']
                match_stats.account_id = row['account_id']
                match_stats.hero_id = row['hero_id']
                match_stats.isRadiant = row['isRadiant']
                match_stats.player_slot = row['player_slot']
                match_stats.level = row['level']
                match_stats.xp_per_min = row['xp_per_min']
                match_stats.league_id = row['league_id']
                match_stats.radiant_score = row['radiant_score']
                match_stats.dire_score = row['dire_score']
                match_stats.radiant_win = row['radiant_win']
                match_stats.version = row['version']
                match_stats.patch = row['patch']
                match_stats.skill = row['skill']
                match_stats.first_blood_time = row['first_blood_time']
                match_stats.objectives = row['objectives']
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
                match_stats.save()
