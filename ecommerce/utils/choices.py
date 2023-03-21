from django.db import models


# user type choices
class UserTypeChoices(models.IntegerChoices):
    ADMIN = 1, "Admin"
    CUSTOMER = 2, "Customer"
    WORKER = 3, "Worker"

class ProductWeightChoices(models.TextChoices):
    GRAM = 'جرام', 'جرام'
    Kilo = 'كيلوجرام', 'كيلوجرام'
    ML = 'مل', 'مل'
    LETER = 'لتر', 'لتر'

class BannersChoices(models.TextChoices):
    STATIC = 'Static', 'Static'
    PRODUCT = 'Product', 'Product'
    SPECIAL_OFFERS = 'special_offers', 'Special Offers'

class CouponTypesChoices(models.TextChoices):
    PERCENTAGE = "PER", "Percentage"
    MONEY = "Mon", "Money"

class OrderStatusChoices(models.IntegerChoices):
    PENDING = 1, "Pending"
    DELIVERING = 2, "Delivering"
    DELIVERED = 3, "Delivered"
    CANCELLED = 4, "Cancelled"
    
class OrderItemTypeChoices(models.IntegerChoices):
    SMALL_UNIT = 1, "Single"
    BIG_UNIT = 2, "Box"

class OrderPaymentOptionChoices(models.IntegerChoices):
    ON_DELIVERY = 1, "On Delivery"