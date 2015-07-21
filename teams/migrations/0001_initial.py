# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150719_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Nombre de Equipo', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('logo', models.ImageField(upload_to=b'pictures', null=True, verbose_name=b'Logo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamHasPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player', models.ForeignKey(verbose_name=b'Jugador', to='players.Player')),
                ('team', models.ForeignKey(verbose_name=b'Equipo', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
