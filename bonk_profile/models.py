from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class BonkProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bonkprofile")
    profile_pic = CloudinaryField('image', default=)
    total_games = models.PositiveIntegerField()

class HighScore(models.Model):
    EASY = 'Easy'
    HARD = 'Hard'
    HECK = 'Heck'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (Hard, 'Hard'),
        (Heck, 'Heck'),
    ]

    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="highscore")
    score = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default=EASY)