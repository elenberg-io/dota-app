# Create the models - database layout
from django.db import models


class Games(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True)
    duration = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    radiant_score = models.PositiveIntegerField()
    dire_score = models.PositiveIntegerField()
    radiant_win = models.BooleanField()


class GameStats(models.Model):
    match_id = models.ForeignKey(Games, to_field='match_id', on_delete=models.CASCADE)
    first_blood_time = models.PositiveIntegerField()
    game_mode = models.PositiveIntegerField()
    human_players = models.PositiveIntegerField()
    version = models.PositiveIntegerField()
    patch = models.PositiveIntegerField()
    players = models.TextField()
    objectives = models.TextField()
    radiant_gold_adv = models.TextField()
    radiant_xp_adv = models.TextField()
    skill = models.FloatField()
    region = models.PositiveIntegerField()

