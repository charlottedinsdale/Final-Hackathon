from . import views
from django.urls import path
from .views import LeaderboardView, profile_view, update_profile, delete_profile_pic

urlpatterns = [
    path('',  views.HomePage.as_view(), name='home'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/delete_pic/', delete_profile_pic, name='delete_profile_pic'),
]
