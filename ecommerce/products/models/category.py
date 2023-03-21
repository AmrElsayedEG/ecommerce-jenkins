from django.db import models

def company_image(instance, filename):
    return f"categories/{instance.title}/{filename}"

class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=company_image)
    catregory_order = models.PositiveBigIntegerField(default=10)
    live = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.title