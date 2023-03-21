from rest_framework.generics import ListAPIView
from main.models import Banners
from main.serializers import BannersSerializer
from utils import IsAuthenticated, SearchFilter, DjangoFilterBackend

class ListBannersView(ListAPIView):
    queryset = Banners.objects.filter(live=True).order_by('-order')
    serializer_class = BannersSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ['position']
    pagination_class = None