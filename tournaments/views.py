from django.shortcuts import render
from django.views.generic import ListView
from tournaments.models import Tournament


class TournamentList(ListView):
    template_name = 'tournament/tournament_list.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
        tournaments = Tournament.objects.all()
        return tournaments

    def get_context_data(self, **kwargs):
        context = super(TournamentList, self).get_context_data(**kwargs)
        return context