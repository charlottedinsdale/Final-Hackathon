from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bonk_profile.models import HighScore
# Create your views here.

def home(request):
    return render(request, 'game/home.html')


def easy(request):
    context = {
        'highscores': None
    }
    
    if request.user.is_authenticated:
        user = request.user
        highscores = HighScore.objects.filter(username=request.user, difficulty="Easy")
        context = {
        'user': user,
        'highscores': highscores
        }
    return render(request, 'game/bonk-it-game.html', context)


def hard(request):
    context = {
        'highscores': None
    }
    
    if request.user.is_authenticated:
        user = request.user
        highscores = HighScore.objects.filter(username=request.user, difficulty="Hard")
        
        context = {
        'user': user,
        'highscores': highscores
        }
    return render(request, 'game/hard-mode.html', context)


def heck(request):
    context = {
        'highscores': None
    }
    
    if request.user.is_authenticated:
        user = request.user
        highscores = HighScore.objects.filter(username=request.user, difficulty="Heck")
        
        context = {
        'user': user,
        'highscores': highscores
        }
    return render(request, 'game/heck-mode.html', context)


@login_required
def submit_high_score(request):
    if request.method == 'POST':
        user = request.user
        score = int(request.POST.get('score'))
        difficulty = request.POST.get('difficulty')
        
        # Try to get the existing high score for this user and difficulty
        high_score, created = HighScore.objects.get_or_create(
            username=user,
            difficulty=difficulty,
            defaults={'score': score}
        )
        # Create a new HighScore record
        if not created and score > high_score.score:
            high_score.score = score
            high_score.save()
        
        # Redirect to a page showing high scores or back to the game
        return redirect('leaderboard')  
    
    # If not a POST request, redirect back to the game
    return redirect('home')  
