from django.db import models

class Currency(models.Model):
    currency = models.CharField(max_length=20)
    currency_ar = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    default = models.BooleanField(default=True)

    def __str__(self):
        return self.currency

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'