from django.db import models
from .user import User

class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country.country} - {self.city}"

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_addresses')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    primary = models.BooleanField(default=False)
    location = models.JSONField()