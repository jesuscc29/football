# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from teams.models import Team


@python_2_unicode_compatible
class Tournament(models.Model):
    STATUS = (
        (0, 'En Curso'),
        (1, 'Terminado')
    )
    name = models.CharField(verbose_name='Nombre de Torneo',
                            blank=True, null=True, max_length=100)
    description = models.TextField(verbose_name='Descripción',
                                   blank=True, null=True)
    status = models.SmallIntegerField(max_length=1, choices=STATUS,
                                      default=0)

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class TournamentHasTeam(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name='Torneo')
    team = models.ForeignKey(Team, verbose_name='Equipo')

    def __str__(self):
        return self.tournament.name + ' - ' + self.team.name