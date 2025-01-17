from . import views
from django.urls import path

urlpatterns = [
     path('easy/', 
          views.easy, name='easy'),
     path('submit-high-score/',
          views.submit_high_score, name='submit_high_score'),
     path('hard/', 
          views.hard, name='hard'),
     path('heck/', 
          views.heck, name='heck'),
     path('increment-total-games/', views.increment_total_games, name='increment_total_games'),    
]