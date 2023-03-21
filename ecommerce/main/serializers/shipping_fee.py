from rest_framework import serializers
from main.models import ShippingFee

class ShippingFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingFee
        fields = ('id', 'amount',)