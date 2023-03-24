from rest_framework import serializers
from main.models import Banners
from utils import TranslateBannerMixin

class BannersSerializer(TranslateBannerMixin, serializers.ModelSerializer):
    class Meta:
        model = Banners
        exclude = ('title_en', 'image_en',)