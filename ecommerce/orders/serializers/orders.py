from rest_framework import serializers
from orders.models import Order, OrderItem
from .order_items import OrderItemsSerializer
import random
from main.serializers import ShippingFeeSerializer, CouponSerializer
from utils import OrderStatusChoices
import logging
from django.utils.timezone import now
from datetime import timedelta
from users.serializers import AddressSerializer
from main.models import Currency
from main.serializers import CurrencySerializer
logger = logging.getLogger(__name__)

class OrderSerializer(serializers.ModelSerializer):
    error_msgs = {
        'error' : {
            'error' : 'A coupon you are using is invalid or expired',
            'error_ar' : 'الكوبون المستخدم ربما منتهي الصلاحية أو لم تستوفي الشروط'
        }
    }
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'order_no' : {'validators' : []},
            'customer' :  {'required' : False},
            'address' : {'required' : True},
            'shipping_fees' : {'required' : True}
        }

    def validate(self, attrs):
        if not attrs.get('customer'):
            attrs['customer'] = self.context.get('request').user
        if attrs.get('coupon'):
            if attrs.get('coupon').end_date < now() or Order.objects.filter(customer=attrs['customer'], coupon=attrs['coupon']).exists():
                raise serializers.ValidationError(self.error_msgs['error'])
        while True:
            order_no = random.randint(100000, 999999)
            if not Order.objects.filter(order_no=order_no).exists():
                attrs['order_no'] = order_no
                break
        attrs['currency'] = Currency.objects.filter(default=True).last()
        return attrs

class CreateOrderSerializer(serializers.Serializer):
    error_msgs = {
        'error' : {
            'error' : 'There is no items in your order',
            'error_ar' : 'لا توجد منتجات فى الطلب'
        }
    }
    order = OrderSerializer()
    items = OrderItemsSerializer(many=True)

    def validate(self, attrs):
        if len(attrs.get('items')) == 0:
            raise serializers.ValidationError(self.error_msgs['error'])
        return attrs

    def create(self, validated_data):
        order = validated_data.get('order')
        items = validated_data.get('items')

        order_instance = Order.objects.create(**order)

        items_list = []

        for item in items:
            item['product'].in_stock_items -= item['quantity']
            item['product'].save()
            item['price'] = item['product'].small_unit_price
            # if item['type'] == item['product'].small_unit:
            #     item['product'].in_stock_items -= item['quantity']
            #     item['product'].save()
            #     item['price'] = item['product'].small_unit_price
            # else:
            #     item['product'].in_stock_items -= int(item['quantity'] * item['product'].in_big_items)
            #     item['product'].ordered_times += 1
            #     item['product'].save()
            #     item['price'] = item['product'].big_unit_price
            items_list.append(OrderItem(**item, order=order_instance))

        items_objects = OrderItem.objects.bulk_create(items_list)

        order_instance.order_submit_email()

        return order_instance

class OrderDetailsSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemsSerializer(many=True)
    address = AddressSerializer()
    shipping_fees = ShippingFeeSerializer()
    coupon = CouponSerializer()
    currency = CurrencySerializer()

    class Meta:
        model = Order
        fields = ('order_no', 'notes', 'phone', 'created', 'status', 'ordered_items', 'total_cost', 'address', 'shipping_fees', 'coupon', 'currency')

class CancelOrderSerializer(serializers.ModelSerializer):
    error_msg = {
        'reject' : {
            'error' : 'This order can\'t be edited, Please contact the support',
            'error_ar' : 'هذا الطلب لايمكن تعديله، برجاء مراجعة الدعم الفني'
        }
    }
    class Meta:
        model = Order
        fields = ('status',)

    def update(self, instance, validated_data):
        if instance.status != OrderStatusChoices.PENDING:
            raise serializers.ValidationError(self.error_msg['reject'])
        hours = timedelta(hours=1)
        if instance.created + hours < now():
            raise serializers.ValidationError(self.error_msg['reject'])
        return super().update(instance, validated_data)