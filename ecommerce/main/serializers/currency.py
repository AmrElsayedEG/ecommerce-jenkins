from rest_framework import serializers
from main.models import Currency
from utils import TranslateTitleMixin

class CurrencySerializer(TranslateTitleMixin, serializers.ModelSerializer):
    class Meta:
        model = Currency
        exclude = ('id', 'default', 'title_en',)