from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from bonk_profile.models import HighScore, BonkProfile
# Create your views here.

def home(request):
    return render(request, 'game/home.html')


def easy(request):
    context = {'highscore': 0}  # Default highscore to 0
    
    if request.user.is_authenticated:
        user = request.user
        # Get all highscores for 'Easy' difficulty
        highscores = HighScore.objects.filter(
            username=user, 
            difficulty="Easy"
        )
        
        # If highscores exist, get the highest one
        if highscores.exists():
            # Order by score in descending order and take the first one
            highest_score = highscores.order_by('-score').first()
            context.update({
                'user': user,
                'highscore': highest_score.score
            })

    return render(request, 'game/bonk-it-game.html', context)


def hard(request):
    context = {'highscore': 0}  # Default highscore to 0
    
    if request.user.is_authenticated:
        user = request.user
        # Get all highscores for 'Hard' difficulty
        highscores = HighScore.objects.filter(
            username=user, 
            difficulty="Hard"
        )
        
        # If highscores exist, get the highest one
        if highscores.exists():
            # Order by score in descending order and take the first one
            highest_score = highscores.order_by('-score').first()
            context.update({
                'user': user,
                'highscore': highest_score.score
            })

    return render(request, 'game/hard-mode.html', context)


def heck(request):
    context = {'highscore': 0}  # Default highscore to 0
    
    if request.user.is_authenticated:
        user = request.user
        # Get all highscores for 'Heck' difficulty
        highscores = HighScore.objects.filter(
            username=user, 
            difficulty="Heck"
        )
        
        # If highscores exist, get the highest one
        if highscores.exists():
            # Order by score in descending order and take the first one
            highest_score = highscores.order_by('-score').first()
            context.update({
                'user': user,
                'highscore': highest_score.score
            })

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

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def increment_total_games(request):
    if request.method == 'POST':
        request.user.bonkprofile.total_games += 1
        request.user.bonkprofile.save()
        return JsonResponse({'total_games': request.user.bonkprofile.total_games})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)