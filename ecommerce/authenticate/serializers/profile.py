from rest_framework import serializers
from users.models import User
from users.serializers import AddressSerializer

class ProfileSerializer(serializers.ModelSerializer):
    addresses = serializers.SerializerMethodField()

    def get_addresses(self, obj):
        return AddressSerializer(obj.user_addresses.all(), context={'request':self.context['request']}, many=True).data
        
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'addresses')

# class ResetPasswordSerializer(serializers.Serializer):

#     error_msg = {
#         "token" : {
#             "error" : "Invalid token",
#             "error_ar" : "خطأ في البيانات"
#         },
#         "doesnt_match" : {
#             "error" : "Passwords doesn\'t match",
#             "error_ar" : "كلمتي المرور ليستا متطابقتين"
#         }
#     }

#     password = serializers.CharField()
#     password1 = serializers.CharField()
#     token = serializers.CharField()

#     def validate(self, attrs):
        
#         if attrs.get('password') != attrs.get('password1'):
#             raise serializers.ValidationError(self.error_msg['doesnt_match'])
        
#         token = Token.objects.get(key=attrs.get('token'))

#         if not token or not token.user.is_active:
#             raise serializers.ValidationError(self.error_msg['token'])

#         attrs['user'] = token.user

#         return attrs

#     def update(self, validated_data):
#         instance = validated_data.get('user')
#         instance.set_password(validated_data.get('password'))
#         instance.save()
#         return instance