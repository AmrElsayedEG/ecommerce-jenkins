from rest_framework import serializers
from users.models import User
from utils import send_email, UpdatePasswordMixin
from django.db.models import Q
import logging
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)

class ForgetPasswordRequestSerializer(serializers.Serializer):
    error_msg = {
        "email": {
            "error" : _("A user with that email or phone not found"),
        },
        "send_error" : {
            "error" : _("An error occured while sending email, Please contact support"),
        }
    }
    email = serializers.CharField(help_text="Enter email here", required=True)

    def validate(self, attrs):
        user = User.objects.filter(Q(email=attrs.get('email')) | Q(phone=attrs.get('phone'))).last()
        if not user:
            raise serializers.ValidationError(self.error_msg['email'])
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.get('user')
        try:
            token = get_random_string(5, '0123456789')
            send_email(
                subject="إستعادة كلمة المرور",
                template_name="forget_password_body.html",
                context={
                    "token" : token,
                    "name" : user.first_name
                },
                to=[user.email]
            )
            user.requested_token = token
            user.save()
        except:
            logger.error(f"[Reset Password Token Email] Error while sending email for user {user.email}")
            raise serializers.ValidationError(self.error_msg['send_error'])
        return user

class CheckForgetPasswordTokenSerializer(serializers.Serializer):
    error_msg = {
        "token" : {
            "error" : _("Invalid token"),
        }
    }
    token = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    def validate(self, attrs):
        user = User.objects.filter(Q(email=attrs.get('email')) | Q(phone=attrs.get('phone'))).last()
        if not user or user.requested_token != attrs.get('token'):
            raise serializers.ValidationError(self.error_msg['token'])
        return attrs
    
class SetForgetPasswordSerializer(UpdatePasswordMixin, serializers.Serializer):
    error_msg = {
        "token" : {
            "error" : _("Invalid token"),
        },
        "doesnt_match" : {
            "error" : _("Passwords doesn\'t match"),
        },
    }
    token = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)

    def validate(self, attrs):

        user = User.objects.filter(Q(email=attrs.get('email')) | Q(phone=attrs.get('phone'))).last()

        if not user or user.requested_token != attrs.get('token'):
            raise serializers.ValidationError(self.error_msg['token'])

        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError(self.error_msg['doesnt_match'])

        attrs['user'] = user

        return attrs

class ChangePasswordSerializer(UpdatePasswordMixin, serializers.Serializer):
    password = serializers.CharField()

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs