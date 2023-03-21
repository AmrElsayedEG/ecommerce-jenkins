from rest_framework import serializers
from users.models import User
from utils import send_email, UpdatePasswordMixin
from django.db.models import Q
import logging
from django.utils.crypto import get_random_string

logger = logging.getLogger(__name__)

class ForgetPasswordRequestSerializer(serializers.Serializer):
    error_msg = {
        "email": {
            "error" : "A user with that email or phone not found",
            "error_ar" : "لا يوجد مستخدم مسجل بهذا البريد الإلكترونى أو رقم الهاتف"
        },
        "send_error" : {
            "error" : "An error occured while sending email, Please contact support",
            "error_ar" : "حدث خطأ، برجاء مراجعة الدعم الفني"
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
            "error" : "Invalid token",
            "error_ar" : "خطأ في الكود"
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
            "error" : "Invalid token",
            "error_ar" : "خطأ في الكود"
        },
        "doesnt_match" : {
            "error" : "Passwords doesn\'t match",
            "error_ar" : "كلمتي المرور ليستا متطابقتين"
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