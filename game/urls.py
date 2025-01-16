from . import views
from django.urls import path

urlpatterns = [
    path('easy/', 
        views.easy, name='easy'),
    
]