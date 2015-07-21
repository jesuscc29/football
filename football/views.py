# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'jesuscc29'


def home(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('index.html',
                              request_context)


def user_login(request):
    context = dict()
    error = ''
    print request.user
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if 'rememberme' not in request.POST:
                    request.session.set_expiry(900)

                login(request, user)
                request.session['user_name'] = user.first_name
                request.session['user_last_name'] = user.last_name
                request.session['authenticated'] = True

                url = "/"
                if not error:
                    try:
                        ur_get = request.META['HTTP_REFERER']
                    except KeyError:
                        pass
                    else:
                        ur_get = ur_get.split("next=")
                        if len(ur_get) > 1:
                            url = ur_get[1]
                    return HttpResponseRedirect(url)
            else:
                error = "Tu cuenta ha sido desactivada, por favor " \
                        "ponte en contacto con tu administrador"
        else:
            error = "Tu nombre de usuario o contraseña son " \
                    "incorrectos."

    context['error'] = error
    var_template = RequestContext(request, context)
    return render_to_response("login.html", var_template)


def user_logout(request):
    logout(request)
    request.session['authenticated'] = False
    return HttpResponseRedirect(reverse('home'))