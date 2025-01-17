from . import views
from django.urls import path

urlpatterns = [
    path('easy/', 
        views.easy, name='easy'),
     path('submit-high-score/', views.submit_high_score, name='submit_high_score'),
]