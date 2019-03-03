from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Game
from .forms import GameForm


def index(request):
    all_games = Game.objects.all()
    return render(request, 'index.html', { 'games': all_games })


def detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'detail.html', { 'game': game })


def new(request):
    return render(request, 'new.html', { 'form': GameForm() })


def create(request):
    form = GameForm(request.POST)
    if form.is_valid():
        game = form.save()
        return HttpResponseRedirect(reverse('games:index'))

    return HttpResponseRedirect('/games')
