from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from django.template.defaultfilters import lower
from django.core.cache import cache

from .utils import *


def index(request, id):
    pokemon = get_pokemon(id)

    context = {
        'pokemon': pokemon,
    }
    return render(request, './index.html', context)


def add_team(request, id):
    done = False
    if request.method == 'POST':
        for key in range(6):
            if cache.get(str(key)) is None and done is False:
                cache.set(str(key), id, timeout=3600)
                done = True
        return redirect('../../' + str(id))


def remove_team(request, key):
    if request.method == 'POST':
        cache.delete(str(key))
        return redirect('../../team')


def search_pokemon(request):
    search = request.GET.get('search')
    search = lower(search)
    pokemon = get_pokemon(search)
    context = {
        'search': search,
        'pokemon': pokemon
    }
    return render(request, "./search.html", context)


def team(request):
    team_pokemon = [None, None, None, None, None, None]
    cpt = 1
    while 0 < cpt < 7:
        for key in range(6):
            if cache.get(str(key)) is None:
                cpt = 0
            else:
                team_pokemon[key] = get_pokemon(cache.get(str(key)))
                cpt += 1
    context = {
        'pokemon': team_pokemon
    }
    return render(request, "./team.html", context)


def previous_pokemon(request, id):
    previous_id = max(1, id - 1)
    return redirect('index', id=previous_id)


def next_pokemon(request, id):
    next_id = min(1008, id + 1)
    return redirect('index', id=next_id)
