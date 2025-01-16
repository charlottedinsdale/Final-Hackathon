from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'game/home.html')


def easy(request):
    # if request == 'POST':
    #     form = 
    return render(request, 'game/bonk-it-game.html')
    