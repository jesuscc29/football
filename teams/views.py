from django.shortcuts import render
from django.views.generic import ListView, DetailView
from teams.models import Team, TeamHasPlayer


class TeamList(ListView):
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        teams = Team.objects.all()
        return teams

    def get_context_data(self, **kwargs):
        context = super(TeamList, self).get_context_data(**kwargs)
        return context


class TeamDetail(DetailView):
    template_name = 'teams/team_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            team = Team.objects.get(pk=pk)
            return team
        else:
            raise AttributeError('No PK Found for a Team.')

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data(**kwargs)
        team_players = TeamHasPlayer.objects.filter(team__pk=self.get_object().pk)
        context['team_players'] = team_players
        return context
