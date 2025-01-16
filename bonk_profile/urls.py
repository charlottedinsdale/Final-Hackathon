from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('profile/', views.BonkProfile.as_view(), name='profile'),
]
