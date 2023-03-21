from rest_framework import serializers
from users.models import WishList
from products.serializers import WishListProductSerializer

class WishListSerializer(serializers.ModelSerializer):
    product = WishListProductSerializer()
    class Meta:
        model = WishList
        fields = ('id', 'product',)


class CreateWishListSerializer(serializers.ModelSerializer):
    error_msg = {
        'dublicate' : {
            'error' : 'This product is already in your wishlist',
            'error_ar' : 'هذا المنتج موجود بالقائمة بالفعل'
        }
    }
    class Meta:
        model = WishList
        fields = ('id', 'product')
    
    def validate(self, attrs):
        if WishList.objects.filter(user=self.context['request'].user, product=attrs.get('product')).exists():
            raise serializers.ValidationError(self.error_msg['dublicate'])
        attrs['user'] = self.context['request'].user
        return attrs