from django.shortcuts import render, get_object_or_404

from .models import Game


def index(request):
    all_games = Game.objects.all()
    return render(request, 'index.html', { 'games': all_games })


def detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'detail.html', { 'game': game })


def new(request):
    return render(request, 'new.html')
