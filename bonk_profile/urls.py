from . import views
from django.urls import path
from .views import LeaderboardView, update_profile

urlpatterns = [
    path('',  views.HomePage.as_view(), name='home'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('profile/', views.BonkProfile.as_view(), name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
]
    

