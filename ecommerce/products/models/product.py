from django.db import models
from products.models.category import Category
from products.models.sub_category import SubCategory
from main.models.currency import Currency
from utils import ProductWeightChoices


def product_image(instance, filename):
    return f"products/{instance.title}/{filename}"

class Product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=10000)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    # images
    main_image = models.ImageField(upload_to=product_image)
    image_1 = models.ImageField(upload_to=product_image, blank=True, null=True)
    image_2 = models.ImageField(upload_to=product_image, blank=True, null=True)
    image_3 = models.ImageField(upload_to=product_image, blank=True, null=True)

    small_available = models.BooleanField("Customers can buy small unit?", default=False)
    # big unit
    big_unit = models.CharField("Big unit name", max_length=100, blank=True, null=True)
    big_unit_price = models.FloatField("Big unit price", default=0)
    big_unit_price_discount = models.FloatField("Discount price for big unit", blank=True, null=True)
    big_unit_discount_max_quantity = models.PositiveBigIntegerField("Max quantity user have to buy if there is a discount on Big unit", blank=True, null=True)
    # small unit
    small_unit =models.CharField("Unit name", max_length=100)
    small_unit_price = models.FloatField("Unit price", default=0)
    small_unit_price_discount = models.FloatField("Discount price for the unit", blank=True, null=True)
    small_unit_discount_max_quantity = models.PositiveBigIntegerField("Max quantity user have to buy if there is a discount on the Unit", blank=True, null=True)

    in_big_items = models.PositiveIntegerField("Items in each big unit", blank=True, null=True)
    item_weight = models.IntegerField()
    weight_type = models.CharField(max_length=50, choices=ProductWeightChoices.choices, default=ProductWeightChoices.GRAM)
    live = models.BooleanField(default=True)
    in_stock_items = models.PositiveIntegerField(default=0)
    ordered_times = models.PositiveBigIntegerField(default=0)
    product_order = models.PositiveBigIntegerField(default=100)
    big_unit_max_quantity =  models.PositiveBigIntegerField("Max quantity if there is no discount for big unit", blank=True, null=True)
    small_unit_max_quantity =  models.PositiveBigIntegerField("Max quantity if there is no discount for small unit", blank=True, null=True)

    def __str__(self) -> str:
        return self.title