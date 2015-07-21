# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from tournaments.views import TournamentList

__author__ = 'jesuscc29'

urlpatterns = patterns('',
    url(r'^torneos/$', TournamentList.as_view(), name='tournament_list'),

)


