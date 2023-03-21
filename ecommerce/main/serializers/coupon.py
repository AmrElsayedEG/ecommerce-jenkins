from rest_framework import serializers
from main.models import Coupon
from orders.models import Order
from django.utils.timezone import now

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class CheckCouponSerializer(serializers.Serializer):
    error_msgs = {
        'error' : {
            'error' : 'A coupon you are using is invalid or expired',
            'error_ar' : 'الكوبون المستخدم ربما منتهي الصلاحية أو لم تستوفي الشروط'
        }
    }
    code = serializers.CharField(required=True)
    total = serializers.FloatField(required=True)

    def validate(self, attrs):
        coupon = Coupon.objects.filter(code=attrs.get('code'))

        if not coupon.exists():
            raise serializers.ValidationError(self.error_msgs['error'])

        coupon = coupon.last()

        if coupon.end_date < now():
            raise serializers.ValidationError(self.error_msgs['error'])

        if coupon.total_must_be and attrs.get('total') < coupon.total_must_be:
            raise serializers.ValidationError(self.error_msgs['error'])

        if coupon.total_must_be is None and Order.objects.filter(customer=self.context['request'].user, coupon=coupon).exists():
            raise serializers.ValidationError(self.error_msgs['error'])

        attrs['instance'] = coupon
        return attrs