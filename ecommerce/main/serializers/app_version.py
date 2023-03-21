from rest_framework import serializers
from main.models import AppVersion

class AppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = ('version', 'active',)