from rest_framework import serializers
from products.models import Product
from .category import CategorySerializer
from .sub_category import SubCategorySerializer
from main.serializers import CurrencySerializer
from users.models import WishList
import random
from django.db.models import Q

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'main_image', 'small_unit', 'small_unit_price', 'small_unit_price_discount', 'category', 'sub_category', 'currency')

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['currency'] = CurrencySerializer(instance.currency).data
        return result

class DetailsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('ordered_times', 'product_order', 'big_unit', 'big_unit_price', 'big_unit_price_discount', 'big_unit_discount_max_quantity',)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['category'] = CategorySerializer(instance.category).data
        result['sub_category'] = SubCategorySerializer(instance.sub_category).data
        result['wishlist'] = WishList.objects.filter(user=self.context['request'].user, product=instance).exists()
        result['currency'] = CurrencySerializer(instance.currency).data
        reco_products = Product.objects.filter(~Q(id=instance.id), category__id=instance.category.id)
        reco_result = random.sample(list(reco_products), 3 if reco_products.count() >= 3 else reco_products.count())
        result['recommendations'] = ProductSerializer(reco_result, many=True).data
        return result

class WishListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'main_image')