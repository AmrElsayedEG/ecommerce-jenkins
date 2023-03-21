from rest_framework import serializers
from orders.models import OrderItem
from products.serializers import ProductSerializer
from utils import OrderItemTypeChoices

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ('order','price',)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['product'] = ProductSerializer(instance.product).data
        return result

    def validate(self, attrs):
        # if attrs.get('type') == OrderItemTypeChoices.BIG_UNIT:
        #     max_boxs = int(attrs.get('product').in_stock_items / attrs.get('product').box_items)
        #     if attrs.get('quantity') > max_boxs:
        #         raise serializers.ValidationError(
        #             {
        #                 "item" : f"{attrs.get('product').title}",
        #             }
        #         )
        # Remove the next line in large systems
        attrs['type'] = OrderItemTypeChoices.SMALL_UNIT
        if attrs.get('type') == OrderItemTypeChoices.SMALL_UNIT:
            if attrs.get('quantity') > attrs.get('product').in_stock_items:
                raise serializers.ValidationError(
                    {
                        "item" : f"{attrs.get('product').title}",
                    }
                )

        return attrs