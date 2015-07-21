# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from teams.views import TeamList, TeamDetail

__author__ = 'jesuscc29'

urlpatterns = patterns('',
    url(r'^equipos/$', TeamList.as_view(), name='team_list'),
    url(r'^equipos/(?P<pk>\d+)/$', TeamDetail.as_view(), name='team_detail'),

)

