from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BonkProfile

@receiver(post_save, sender=User)
def create_bonk_profile(sender, instance, created, **kwargs):
    if created:
        BonkProfile.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_bonk_profile(sender, instance, **kwargs):
    instance.bonkprofile.save()