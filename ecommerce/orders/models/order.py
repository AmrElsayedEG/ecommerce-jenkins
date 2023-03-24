from django.db import models
from users.models import User, Address
from main.models import Coupon, ShippingFee, Currency
from utils import OrderStatusChoices, CouponTypesChoices, OrderPaymentOptionChoices
from utils import send_email

class Order(models.Model):
    order_no = models.IntegerField(unique=True, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_order')
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey(Coupon, blank=True, null=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True,null=True)
    payment_option = models.PositiveIntegerField(choices=OrderPaymentOptionChoices.choices, default= OrderPaymentOptionChoices.ON_DELIVERY)
    shipping_fees = models.ForeignKey(ShippingFee, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(choices=OrderStatusChoices.choices, default=OrderStatusChoices.PENDING)
    last_action_date = models.DateTimeField(auto_now=True)

    @property
    def total_cost(self):
        total = sum(item.get_cost() for item in self.ordered_items.all())

        # Coupons
        if self.coupon:
            if self.coupon.discount_type == CouponTypesChoices.PERCENTAGE:
                total = total - ((total * self.coupon.discount) / 100)
            else:
                total -= self.coupon.discount

        # Shipping Fees
        if self.shipping_fees:
            total += self.shipping_fees.amount
            
        return total

    def order_submit_email(self):
        send_email(
                subject="Order Details",
                template_name="order_info.html",
                context={
                    "name" : self.customer.first_name,
                    "order" : self,
                    "items" : self.ordered_items.all(),
                    "total" : self.total_cost
                },
                to=[self.customer.email]
            )
        return