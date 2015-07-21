# -*- coding: utf-8 -*-
from django.forms import ModelForm
from players.models import Player

__author__ = 'jesuscc29'


class AddPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'number', 'position', 'picture']