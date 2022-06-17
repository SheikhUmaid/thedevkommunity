from django.apps import AppConfig


class DevusersConfig(AppConfig):

    name = 'devusers'
    
    def ready(self):
        import devusers.signals
