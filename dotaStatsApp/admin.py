from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Games, GameStats

admin.site.register(Games)
admin.site.register(GameStats)
