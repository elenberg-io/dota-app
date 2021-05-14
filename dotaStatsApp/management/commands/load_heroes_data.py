"""
Load heroes data
"""
from csv import DictReader
import os

from django.core.management import BaseCommand

from dotaStatsApp.models import Heroes


class Command(BaseCommand):
    help = 'Loads Dota heroes data and stats'

    def handle(self, *args, **options):
        if Heroes.objects.exists():
            print('Heroes data already loaded')
            return
        heroes_fp = os.path.join('data', 'output', 'heroesData.csv')
        print('Loading heroes data')
        with open(heroes_fp) as heroes_file:
            for row in DictReader(heroes_file):
                row = {i: (j if len(j) != 0 else None) for i, j in row.items()}
                hero = Heroes()
                hero.hero_id = row['id']
                hero.dname = row['dname']
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
