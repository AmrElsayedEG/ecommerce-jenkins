from django.contrib import admin
from main.models import Banners, Coupon, ShippingFee, AppVersion, Currency

admin.site.register(Banners)
admin.site.register(Coupon)
admin.site.register(ShippingFee)
admin.site.register(AppVersion)
admin.site.register(Currency)