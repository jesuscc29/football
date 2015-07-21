# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='picture',
            field=models.ImageField(upload_to=b'pictures', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.SmallIntegerField(default=0, choices=[(0, b'No Definido'), (1, b'Portero'), (2, b'Defensa'), (3, b'Medio'), (4, b'Delantero')], max_length=1, blank=True, null=True, verbose_name=b'Posici\xc3\xb3n'),
        ),
    ]
