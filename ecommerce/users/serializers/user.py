from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','phone')

class UserEmailSerializer(serializers.ModelSerializer):
    error_msg = {
        'dublicate' : {
            'error' : 'An account with that email exists',
            'error_ar' : 'يوجد حساب مسجل بهذا البريد'
        }
    }
    class Meta:
        model = User
        fields = ('email',)
        extra_kwargs = {'email' : {'validators' : []}}
    
    def validate(self, attrs):
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError(self.error_msg['dublicate'])
        return attrs

class EmailTokenSerializer(serializers.Serializer):
    error_msg = {
        "token" : {
            "error" : "Invalid token",
            "error_ar" : "خطأ في الكود"
        },
        'dublicate' : {
            'error' : 'An account with that email exists',
            'error_ar' : 'يوجد حساب مسجل بهذا البريد'
        }
    }
    email = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate(self, attrs):

        user = self.context['request'].user
        
        if not user or user.requested_token != attrs.get('token'):
            raise serializers.ValidationError(self.error_msg['token'])

        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError(self.error_msg['dublicate'])

        return attrs