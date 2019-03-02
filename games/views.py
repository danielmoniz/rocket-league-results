from django.shortcuts import render, get_object_or_404

from .models import Game


def index(request):
    return render(request, 'index.html', {})


def detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'detail.html', { 'game': game })
