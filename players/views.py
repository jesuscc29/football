from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from players.functions import LoginRequiredMixin
from players.models import Player
from players.player_forms import AddPlayerForm


class PlayerList(ListView):
    template_name = 'players/players_index.html'
    context_object_name = 'players_list'

    def get_queryset(self):
        players = Player.objects.all()
        return players

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data(**kwargs)
        authenticated = False
        if self.request.user.is_authenticated():
            authenticated = True
        context['authenticated'] = authenticated
        return context


class PlayerCreate(LoginRequiredMixin, CreateView):
    template_name = 'generic/generic_form.html'
    model = Player
    success_url = reverse_lazy('players_list')

    def get_context_data(self, **kwargs):
        context = super(PlayerCreate, self).get_context_data(**kwargs)
        context['form'] = AddPlayerForm()
        return context


class PlayerEdit(LoginRequiredMixin, UpdateView):
    template_name = 'generic/generic_form.html'
    success_url = reverse_lazy('players_list')
    model = Player

    def get_context_data(self, **kwargs):
        context = super(PlayerEdit, self).get_context_data(**kwargs)
        return context


class PlayerAdminList(LoginRequiredMixin, ListView):
    template_name = 'players/players_admin_index.html'
    context_object_name = 'players_list'

    def get_queryset(self):
        players = Player.objects.all()
        return players

    def get_context_data(self, **kwargs):
        context = super(PlayerAdminList, self).get_context_data(**kwargs)
        return context


class PlayerRemove(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('player_admin_list')

    def get_object(self, queryset=None):
        obj = super(PlayerRemove, self).get_object()
        return obj



