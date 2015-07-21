# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from players.models import Player


@python_2_unicode_compatible
class Team(models.Model):
    name = models.CharField(verbose_name='Nombre de Equipo',
                            blank=True, null=True, max_length=100)
    description = models.TextField(verbose_name='Descripción',
                                   blank=True, null=True)
    logo = models.ImageField(verbose_name='Logo', blank=True,
                             null=True, upload_to='pictures')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TeamHasPlayer(models.Model):
    player = models.ForeignKey(Player, verbose_name='Jugador')
    team = models.ForeignKey(Team, verbose_name='Equipo')

    def __str__(self):
        return self.team.name + ' - ' + self.player.name