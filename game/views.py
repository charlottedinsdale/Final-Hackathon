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
        highscores = HighScore.objects.filter(username=request.user)
        context = {
        'user': user,
        'highscores': highscores
        }
    return render(request, 'game/bonk-it-game.html', context)


@login_required
def submit_high_score(request):
    if request.method == 'POST':
        user = request.user
        score = request.POST.get('score')
        difficulty = request.POST.get('difficulty')
        
        # Create a new HighScore record
        HighScore.objects.create(
            username=user,
            score=int(score),
            difficulty=difficulty
        )
        
        # Redirect to a page showing high scores or back to the game
        return redirect('leaderboard')  
    
    # If not a POST request, redirect back to the game
    return redirect('easy')  #
