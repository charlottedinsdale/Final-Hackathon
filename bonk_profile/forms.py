from django import forms
from .models import BonkProfile

class BonkProfileForm(forms.ModelForm):
    class Meta:
        model = BonkProfile
        fields = ['profile_pic']