from django.db import models
from users.models import City

class ShippingFee(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, related_name='shipping_fees')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.city)