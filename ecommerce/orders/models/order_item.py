from django.db import models
from products.models import Product
from orders.models.order import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def get_cost(self):
        return self.price * self.quantity
