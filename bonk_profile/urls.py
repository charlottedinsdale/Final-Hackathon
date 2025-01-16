from . import views
from django.urls import path
from .views import LeaderboardView

urlpatterns = [
    path('',  views.HomePage.as_view(), name='home'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]
    

