from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product
from products.serializers import ProductSerializer, DetailsProductSerializer
from utils import IsAuthenticated, SearchFilter, DjangoFilterBackend, CategoryProductsPagination
from django.db.models import Q
import random

class ListProductsView(ListAPIView):
    queryset = Product.objects.filter(live=True).order_by('product_order')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = {
        'category' : ["exact"],
        'id' : ["in"],
        'sub_category' : ["exact"]
    }
    search_fields=["title",]
    pagination_class = CategoryProductsPagination

class GetProductView(RetrieveAPIView):
    queryset = Product
    serializer_class = DetailsProductSerializer
    permission_classes = (IsAuthenticated,)

class ListDiscountProductsView(ListAPIView):
    queryset = Product.objects.filter(Q(live=True, big_unit_price_discount__isnull=False) | Q(live=True, small_unit_price_discount__isnull=False)).order_by('product_order')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ['category']
    search_fields=["title"]

class BestSellersView(ListAPIView):
    queryset = Product.objects.all().order_by('-ordered_times')[:10]
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None