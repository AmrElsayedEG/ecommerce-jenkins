from rest_framework import serializers
from users.models import User
import logging
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)

class LoginSerializer(serializers.ModelSerializer):

    error_msg = {
        "login" : {
            "error" : _("Invalid email or Password"),
        },
        "not_active" : {
            "error" : _("This account is not activated, Please contact the manager."),
        },
    }

    username = serializers.CharField(help_text="Enter email or phone here")
    password = serializers.CharField(help_text="Enter password here")

    class Meta:
        model = User
        fields = ('username', 'password',)

    def validate(self, attrs):
        user = User.objects.filter(Q(email=attrs['username']) | Q(phone=attrs['username'])).last()

        if not user:
            raise serializers.ValidationError(self.error_msg['login'])

        if not user.check_password(attrs['password']):
            logger.warn(f'Failed Login attempt: {attrs["username"]}')
            raise serializers.ValidationError(self.error_msg['login'])

        if not user.is_active:
            raise serializers.ValidationError(self.error_msg['not_active'])

        attrs['user'] = user

        return attrs