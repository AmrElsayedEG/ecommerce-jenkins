from django.dispatch import receiver
from django.db.models.signals import post_migrate
from main.models import Currency
from main.apps import MainConfig

@receiver(post_migrate, sender=MainConfig)
def currency_migrate(sender, **kwargs):
    if not Currency.objects.all().exists():
        init_currency = Currency(currency='EGP', currency_ar='ج.م', symbol='£')
        init_currency.save()