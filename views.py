from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import json

from submit.models import Game
from export.models import Game as Export
# Create your views here.

def main_page(request):
    for game in Game.objects.all():
        if Export.objects.filter(name = game.name).count() == 0:
            export_this = Export(
                name = game.name, 
                developer = game.developer.name,
                site = game.developer.url,
                description = game.notes,
                buzz = 0,
                rawbuzz = 0.0,
                plays = 0,
            )
            export_this.save()
    exported = serializers.serialize('json', Export.objects.all())
    return HttpResponse(exported)
