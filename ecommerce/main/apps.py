from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):

        # add default data
        from django.db.models.signals import post_migrate
        from .signals.currency import currency_migrate

        # add default currency
        post_migrate.connect(currency_migrate, sender=self)
