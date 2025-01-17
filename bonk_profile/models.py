from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class BonkProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bonkprofile")
    profile_pic = CloudinaryField('image', default='Bonk-profile-default_fjze4j')
    total_games = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.username} | {self.total_games} games played"

class HighScore(models.Model):
    EASY = 'Easy'
    HARD = 'Hard'
    HECK = 'Heck'

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (HARD, 'Hard'),
        (HECK, 'Heck'),
    ]

    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="highscore")
    score = models.PositiveIntegerField(default = 0)
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default=EASY)