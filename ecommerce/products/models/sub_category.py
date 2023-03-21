from django.db import models
from products.models.category import Category

def sub_image(instance, filename):
    return f"categories/sub/{instance.title}/{filename}"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subs')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=sub_image)
    order = models.IntegerField(default=10)

    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'

    def __str__(self) -> str:
        return self.title