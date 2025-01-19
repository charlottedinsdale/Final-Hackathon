from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .models import HighScore, BonkProfile
from .forms import BonkProfileForm

class HomePage(TemplateView):
    template_name = 'index.html'

class LeaderboardView(View):
    template_name = 'bonk_profile/global_leaderboard.html'

    def get(self, request):
        # ---Get top 10 scores for each difficulty level ---# 
        easy_leaderboard = HighScore.objects.filter(difficulty='Easy').order_by('-score')[:10]
        hard_leaderboard = HighScore.objects.filter(difficulty='Hard').order_by('-score')[:10]
        heck_leaderboard = HighScore.objects.filter(difficulty='Heck').order_by('-score')[:10]

        if request.user.is_authenticated:
            # If authenticated, fetch high scores and ranks for the user
            heck_highscore = HighScore.objects.filter(username=request.user, difficulty='Heck').order_by('-score').first()
            hard_highscore = HighScore.objects.filter(username=request.user, difficulty='Hard').order_by('-score').first()
            easy_highscore = HighScore.objects.filter(username=request.user, difficulty='Easy').order_by('-score').first()

            heck_rank = get_user_rank(request.user, 'Heck') if heck_highscore else None
            hard_rank = get_user_rank(request.user, 'Hard') if hard_highscore else None
            easy_rank = get_user_rank(request.user, 'Easy') if easy_highscore else None
        else:
            # If not authenticated, set high scores and ranks to None
            heck_highscore = hard_highscore = easy_highscore = None
            heck_rank = hard_rank = easy_rank = None

        return render(request, self.template_name, {

            'easy_leaderboard': easy_leaderboard,
            'hard_leaderboard': hard_leaderboard,
            'heck_leaderboard': heck_leaderboard,
            'heck_rank': heck_rank,
            'hard_rank': hard_rank,
            'easy_rank': easy_rank,
        })
        return render(request, 'bonk_profile/global_leaderboard.html', context)

def get_user_rank(user, difficulty):
    all_highscores = HighScore.objects.filter(difficulty=difficulty).order_by('-score')

    for rank, highscore in enumerate(all_highscores, start=1):
        if highscore.username == user:
            return rank
    return None

def profile_view(request):
    if request.user.is_authenticated:
        try:
            bonk_profile = request.user.bonkprofile 
        except BonkProfile.DoesNotExist:
            bonk_profile = None 

        heck_highscore = HighScore.objects.filter(username=request.user, difficulty='Heck').order_by('-score').first()
        hard_highscore = HighScore.objects.filter(username=request.user, difficulty='Hard').order_by('-score').first()
        easy_highscore = HighScore.objects.filter(username=request.user, difficulty='Easy').order_by('-score').first()
        
        heck_rank = get_user_rank(request.user, 'Heck') if heck_highscore else None
        hard_rank = get_user_rank(request.user, 'Hard') if hard_highscore else None
        easy_rank = get_user_rank(request.user, 'Easy') if easy_highscore else None

        return render(request, 'bonk_profile/bonk_profile.html', {
            'bonkprofile': bonk_profile,
            'heck_highscore': heck_highscore,
            'hard_highscore': hard_highscore,
            'easy_highscore': easy_highscore,
            'heck_rank': heck_rank,
            'hard_rank': hard_rank,
            'easy_rank': easy_rank,
        })
        def save(self, *args, **kwargs):
            if not self.profile_pic:
                self.profile_pic = 'Bonk-profile-default_fjze4j'
            super(BonkProfile, self).save(*args, **kwargs)
    else:
        # If the user is not authenticated, render a different template or pass appropriate data
        return render(request, 'bonk_profile/bonk_profile.html', {
            'bonkprofile': None,
            'heck_highscore': None,
            'hard_highscore': None,
            'easy_highscore': None,
            'heck_rank': None,
            'hard_rank': None,
            'easy_rank': None,
        })


def update_profile(request):
    user_profile = request.user.bonkprofile

    if request.method == 'POST':
        form = BonkProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = BonkProfileForm(instance=user_profile)

    return render(request, 'bonk_profile/update_profile.html', {'form': form})

def delete_profile_pic(request):
    user_profile = request.user.bonkprofile

    # Set the profile picture back to the default image
    user_profile.profile_pic = 'Bonk-profile-default_fjze4j'  # Cloudinary public ID of the default image
    user_profile.save()

    return redirect('profile')