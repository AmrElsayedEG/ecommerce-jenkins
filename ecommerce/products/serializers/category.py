from rest_framework import serializers
from products.models import Category, SubCategory
from products.serializers.sub_category import SubCategorySerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('live', 'catregory_order',)

class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('live', 'catregory_order',)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['sub_categories'] = SubCategorySerializer(instance.subs.all().order_by('order'), many=True).data
        return result