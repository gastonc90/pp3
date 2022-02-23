from django.apps import AppConfig


class RecruiterappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RecruiterApp'

    def ready(self):
        import RecruiterApp.signals
