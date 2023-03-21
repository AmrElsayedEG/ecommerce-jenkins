from django.contrib import admin
from users.models import User, Address, City, Country, WishList


admin.site.register(User)
admin.site.register(Address)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(WishList)
