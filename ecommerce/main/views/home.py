from rest_framework.views import APIView
from utils import IsAuthenticated, BannersChoices
from main.models import Banners
from django.db.models import Q
from main.serializers import BannersSerializer
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product
from rest_framework.response import Response

class AppHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        top_banners = Banners.objects.filter(live=True, type=BannersChoices.STATIC).order_by('order')
        offer_banners = Banners.objects.filter(Q(type=BannersChoices.SPECIAL_OFFERS) | Q(type=BannersChoices.PRODUCT), live=True).order_by('order')
        alL_categories = Category.objects.filter(live=True).order_by('catregory_order')
        most_sex_products = Product.objects.all().order_by('-ordered_times')[:1 ]

        return Response({
                'top_banners' : BannersSerializer(top_banners, many=True).data,
                'offer_banners' : BannersSerializer(offer_banners, many=True).data,
                'all_categories' : CategorySerializer(alL_categories, many=True).data,
                'most_sex_products' : ProductSerializer(most_sex_products, many=True).data
        }, status=200)