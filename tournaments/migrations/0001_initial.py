# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Nombre de Torneo', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('status', models.SmallIntegerField(default=0, max_length=1, choices=[(0, b'En Curso'), (1, b'Terminado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TournamentHasTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.ForeignKey(verbose_name=b'Equipo', to='teams.Team')),
                ('tournament', models.ForeignKey(verbose_name=b'Torneo', to='tournaments.Tournament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
