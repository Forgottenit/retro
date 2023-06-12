from django.shortcuts import render
from django.http import HttpResponseRedirect
from .spotify_data import create_fixtures


def update_albums(request):
    create_fixtures()
    return HttpResponseRedirect('/')
