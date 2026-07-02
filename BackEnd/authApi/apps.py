# from django.apps import AppConfig


# class AuthapiConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'authApi'



from django.apps import AppConfig


class AuthapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authApi'

    def ready(self):
        import authApi.signals