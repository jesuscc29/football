from django.contrib import admin
from teams.models import Team, TeamHasPlayer

admin.site.register(Team)
admin.site.register(TeamHasPlayer)
