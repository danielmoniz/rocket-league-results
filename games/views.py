from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Game


def index(request):
    all_games = Game.objects.all()
    return render(request, 'index.html', { 'games': all_games })


def detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'detail.html', { 'game': game })


def new(request):
    return render(request, 'new.html')


def create(request):
    overtime = request.POST['overtime'] == 'true'
    new_game = Game(
        blue_score=request.POST['blue_score'],
        orange_score=request.POST['orange_score'],
        overtime=overtime,
        overtime_length=request.POST['overtime_length'],
    )
    new_game.save()
    return HttpResponseRedirect(reverse('games:index'))
