"""
Create the models
"""
from django.db import models
from django.db.models import JSONField


class Heroes(models.Model):
    hero_id = models.PositiveIntegerField(primary_key=True)
    localized_name = models.TextField()
    dname = models.TextField()
    roles = JSONField(default=None, blank=True, null=True)
    primary_attr = models.TextField(default=None, blank=True, null=True)
    attack_type = models.TextField(default=None, blank=True, null=True)
    base_health = models.PositiveIntegerField(default=None, blank=True, null=True)
    base_health_regen = models.FloatField(default=None, blank=True, null=True)
    base_mana = models.PositiveIntegerField(default=None, blank=True, null=True)
    base_mana_regen = models.FloatField(default=None, blank=True, null=True)
    base_armor = models.FloatField(default=None, blank=True, null=True)
    base_str = models.PositiveIntegerField(default=None, blank=True, null=True)
    base_agi = models.PositiveIntegerField(default=None, blank=True, null=True)
    base_int = models.PositiveIntegerField(default=None, blank=True, null=True)
    str_gain = models.FloatField(default=None, blank=True, null=True)
    agi_gain = models.FloatField(default=None, blank=True, null=True)
    int_gain = models.FloatField(default=None, blank=True, null=True)
    attack_range = models.PositiveIntegerField(default=None, blank=True, null=True)
    attack_rate = models.FloatField(default=None, blank=True, null=True)
    move_speed = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.localized_name


class GameStats(models.Model):
    # blank allows you to pass a null value, null tells the database to accept null values
    # match_id = models.ForeignKey(Games, to_field='match_id', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True, default=None)
    match_id = models.BigIntegerField()
    start_time = models.DateTimeField()
    duration = models.FloatField()
    account_id = models.BigIntegerField(default=None, blank=True, null=True)
    hero_id = models.PositiveIntegerField()
    isRadiant = models.BooleanField()
    player_slot = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    xp_per_min = models.PositiveIntegerField(default=None, blank=True, null=True)
    league_id = models.PositiveIntegerField(default=None, blank=True, null=True)
    patch = models.PositiveIntegerField(default=None, blank=True, null=True)
    radiant_score = models.PositiveIntegerField()
    dire_score = models.PositiveIntegerField()
    radiant_win = models.BooleanField()
    first_blood_time = models.FloatField(default=None, blank=True, null=True)
    game_mode = models.TextField(default=None, blank=True, null=True)
    human_players = models.PositiveIntegerField(default=None, blank=True, null=True)
    skill = models.FloatField(default=None, blank=True, null=True)
    version = models.FloatField(default=None, blank=True, null=True)
    region = models.TextField(default=None, blank=True, null=True)
    total_xp = models.PositiveIntegerField(default=None, blank=True, null=True)
    last_hits = models.PositiveIntegerField(default=None, blank=True, null=True)
    hero_damage = models.PositiveIntegerField(default=None, blank=True, null=True)
    kill_streaks = models.PositiveIntegerField(default=None, blank=True, null=True)
    hero_healing = models.PositiveIntegerField(default=None, blank=True, null=True)
    total_gold = models.PositiveIntegerField(default=None, blank=True, null=True)
    kills = models.PositiveIntegerField(default=None, blank=True, null=True)
    kda = models.PositiveIntegerField(default=None, blank=True, null=True)
    rank_tier = models.PositiveIntegerField(default=None, blank=True, null=True)
    deaths = models.PositiveIntegerField(default=None, blank=True, null=True)
    randomed = models.BooleanField(default=None, blank=True, null=True)
    net_worth = models.FloatField(default=None, blank=True, null=True)
    tower_damage = models.PositiveIntegerField(default=None, blank=True, null=True)
    kills_per_min = models.FloatField(default=None, blank=True, null=True)
    gold_per_min = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_0 = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_1 = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_2 = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_3 = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_4 = models.PositiveIntegerField(default=None, blank=True, null=True)
    item_5 = models.PositiveIntegerField(default=None, blank=True, null=True)
