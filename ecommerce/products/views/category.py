from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Category
from products.serializers import CategorySerializer, DetailCategorySerializer
from utils import IsAuthenticated

class ListCategoriesView(ListAPIView):
    queryset = Category.objects.filter(live=True).order_by('catregory_order')
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

class GetCategoryView(RetrieveAPIView):
    queryset = Category
    serializer_class = DetailCategorySerializer
    permission_classes = (IsAuthenticated,)