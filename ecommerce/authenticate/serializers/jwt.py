from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": {
            "error" : [_("Invalid email or Password")],
            "error_ar" : ["خطأ في البريد الإلكترونى أو كلمة السر"]
        }
    }
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        return data