from rest_framework import serializers
from main.models import Banners

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'