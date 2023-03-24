from rest_framework import serializers
from products.models import SubCategory
from utils import TranslateTitleMixin

class SubCategorySerializer(TranslateTitleMixin, serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ('category', 'title_en',)