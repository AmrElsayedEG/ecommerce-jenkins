from django.db import models
from utils import CouponTypesChoices

class Coupon(models.Model):
    code = models.CharField(max_length=10)
    discount_type = models.CharField(choices=CouponTypesChoices.choices, default=CouponTypesChoices.PERCENTAGE, max_length=20)
    discount = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    total_must_be = models.FloatField("Total must be equal or above", null=True, blank=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'coupon'
        verbose_name_plural = 'coupons'