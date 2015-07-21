# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

__author__ = 'jesuscc29'


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='login')
