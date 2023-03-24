from rest_framework import serializers
from products.models import Category
from products.serializers.sub_category import SubCategorySerializer
from utils import TranslateTitleMixin

class CategorySerializer(TranslateTitleMixin, serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('live', 'catregory_order', 'title_en',)

class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('live', 'catregory_order', 'title_en',)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['sub_categories'] = SubCategorySerializer(instance.subs.all().order_by('order'), many=True, context={'request':self.context['request']}).data
        if self.context['request'].LANGUAGE_CODE == 'en':
            result['title'] = instance.title_en
        return result