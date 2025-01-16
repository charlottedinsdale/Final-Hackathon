from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import HighScore

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

class BonkProfile(TemplateView):
    template_name = 'bonk_profile/bonk_profile.html'
