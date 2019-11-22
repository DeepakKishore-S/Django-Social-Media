from django.apps import AppConfig


class SdkConfig(AppConfig):
    name = 'sdk'


    def ready(self):
        import sdk.signals
