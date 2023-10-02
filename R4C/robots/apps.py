from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import robots.signals