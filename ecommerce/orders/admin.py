from django.contrib import admin
from orders.models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no','customer','status', 'created', 'last_action_date', 'total_cost',)
    readonly_fields = ('total_cost',)
    list_filter = ('status',)
    search_fields = ['customer__name', 'customer__phone', 'order_no',]
    inlines = [OrderItemAdmin,]

admin.site.register(Order, OrderAdmin)