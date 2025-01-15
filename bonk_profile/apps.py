from django.apps import AppConfig


class BonkProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bonk_profile'

    def ready(self):
        import bonk_profile.signals
