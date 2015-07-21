from django.contrib import admin
from tournaments.models import Tournament, TournamentHasTeam

admin.site.register(Tournament)
admin.site.register(TournamentHasTeam)
