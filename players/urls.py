# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from players.views import PlayerList, PlayerCreate, PlayerEdit, PlayerAdminList, PlayerRemove

__author__ = 'jesuscc29'

urlpatterns = patterns('',
    url(r'^$', PlayerList.as_view(), name='players_list'),
    url(r'^nuevo/$', PlayerCreate.as_view(), name='player_create'),
    url(r'^editar/(?P<pk>\d+)/$', PlayerEdit.as_view(), name='player_edit'),
    url(r'^administrar_jugadores/$', PlayerAdminList.as_view(),
        name='player_admin_list'),
    url(r'^remove_player/(?P<pk>\d+)/$', PlayerRemove.as_view(),
        name='remove_player'),

)

