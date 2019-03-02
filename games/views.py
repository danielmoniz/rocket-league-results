from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Game

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
    # return HttpResponse("index page")

def detail(request, id):
    game = get_object_or_404(Game, pk=id)
    # game = Game.objects.get(pk=id)
    # return HttpResponse(f"The game's score was: {game.get_game_result()}")
    return render(request, 'detail.html', { 'game': game })
