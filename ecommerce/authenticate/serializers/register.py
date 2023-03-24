from rest_framework import serializers
from users.models import User
import logging
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)

class RegisterSerializer(serializers.ModelSerializer):
    
    error_msg = {
        'exists' : {
            'error' : _('A user with this email already exists'),
        }
    }
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'password', 'location',)
        extra_kwargs = {'password' : {'write_only':False}, 'email' : {'validators' : []}, 'phone' : {'validators' : []}}

    def validate(self, attrs):
        if User.objects.filter(email = attrs.get('email')).exists():
            raise serializers.ValidationError(self.error_msg['exists'])
        return attrs

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data['username'] = validated_data.get('email')
        validated_data['is_active'] = True

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        return user
