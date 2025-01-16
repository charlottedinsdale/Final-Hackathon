from django.shortcuts import render
from bonk_profile.models import Highscore
# Create your views here.

def home(request):
    return render(request, 'game/home.html')


def easy(request):
    user = request.user
    
    return render(request, 'game/bonk-it-game.html')
    