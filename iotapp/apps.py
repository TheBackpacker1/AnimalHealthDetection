from django.apps import AppConfig


class IotappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iotapp'
    def ready(self):
        from . import mqtt_client
