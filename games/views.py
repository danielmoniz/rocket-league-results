from django.shortcuts import render
from django.http import HttpResponse

from .models import Game

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
    # return HttpResponse("index page")

def show(request, id):
    game = Game.objects.get(pk=id)
    # return HttpResponse(f"The game's score was: {game.get_game_result()}")
    return render(request, 'show.html', { 'game': game })
