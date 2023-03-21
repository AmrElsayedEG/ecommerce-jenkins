from rest_framework import serializers
from main.models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ('id', 'default',)