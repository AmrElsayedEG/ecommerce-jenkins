from rest_framework.generics import RetrieveAPIView
from main.serializers import AppVersionSerializer
from main.models import AppVersion

class GetAppVersionView(RetrieveAPIView):
    queryset = AppVersion
    serializer_class = AppVersionSerializer

    def get_object(self):
        return self.queryset.objects.last()