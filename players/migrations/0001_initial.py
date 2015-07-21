# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'Nombre', blank=True)),
                ('number', models.SmallIntegerField(max_length=3, null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('position', models.SmallIntegerField(default=0, max_length=1, verbose_name=b'Posici\xc3\xb3n', choices=[(0, b'No Definido'), (1, b'Portero'), (2, b'Defensa'), (3, b'Medio'), (4, b'Delantero')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
