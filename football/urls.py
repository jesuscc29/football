from django.conf.urls import patterns, include, url
from django.contrib import admin
from football import settings

urlpatterns = patterns('',
    url(r'^$', 'football.views.home', name='home'),
    url(r'^login/$', 'football.views.user_login', name='login'),
    url(r'^logout/$', 'football.views.user_logout', name='logout'),
    url(r'^jugadores/', include('players.urls')),
    url(r'^torneos/', include('tournaments.urls')),
    url(r'^equipos/', include('teams.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
