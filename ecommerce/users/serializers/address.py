from rest_framework import serializers
from users.models import Address, City, Country
from main.models import ShippingFee
from main.serializers import ShippingFeeSerializer

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    error_msg = {
        'dublicate' : {
            'error' : 'This address is already registered',
            'error_ar' : 'هذا العنوان مسجل بالفعل'
        }
    }
    class Meta:
        model = Address
        fields = '__all__'
    
    def validate(self, attrs):
        print(self.context['request'].user)
        if Address.objects.filter(**attrs, user_id=self.context['request'].user.id).exists():
            raise serializers.ValidationError(self.error_msg['dublicate'])
        return attrs

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['country'] = CountrySerializer(instance.country).data
        result['city'] = CitySerializer(instance.city).data
        if self.context['request'].method == 'GET':
            result['shipping_fees'] = ShippingFeeSerializer(ShippingFee.objects.filter(city__id=instance.city.id).last()).data
        return result