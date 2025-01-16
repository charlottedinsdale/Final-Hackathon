from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class BonkProfile(TemplateView):
    template_name = 'bonk_profile/bonk_profile.html'
