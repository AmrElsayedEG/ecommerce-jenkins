from django.db import models
from utils import BannersChoices

def banner_image(instance, filename):
    return f"banners/{instance.title}/{filename}"

class Banners(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=banner_image)
    type = models.CharField(max_length=50, choices=BannersChoices.choices, default=BannersChoices.STATIC)
    key = models.CharField(max_length=100, blank=True, null=True)
    live = models.BooleanField(default=True)
    order = models.PositiveBigIntegerField(default=10)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self) -> str:
        return self.title