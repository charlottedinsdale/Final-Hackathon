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

        return render(request, self.template_name, {
            'easy_leaderboard': easy_leaderboard,
            'hard_leaderboard': hard_leaderboard,
            'heck_leaderboard': heck_leaderboard,
        })
        return render(request, 'bonk_profile/global_leaderboard.html', context)

def profile_view(request):
    try:
        bonk_profile = request.user.bonkprofile 
    except BonkProfile.DoesNotExist:
        bonk_profile = None 
    return render(request, 'bonk_profile/bonk_profile.html', {
        'bonkprofile': bonk_profile,
    })
    def save(self, *args, **kwargs):
        if not self.profile_pic:
            self.profile_pic = 'Bonk-profile-default_fjze4j'
        super(BonkProfile, self).save(*args, **kwargs)


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