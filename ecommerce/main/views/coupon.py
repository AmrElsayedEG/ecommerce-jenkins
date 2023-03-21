from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from main.serializers import CheckCouponSerializer, CouponSerializer
from main.models import Coupon
from django.utils.timezone import now

class ListActiveCouponsView(ListAPIView):
    queryset = Coupon
    serializer_class = CouponSerializer
    pagination_class = None

    def get_queryset(self):
        return Coupon.objects.filter(end_date__gt=now(), public=True)

class CheckCouponView(CreateAPIView):
    serializer_class = CheckCouponSerializer

    def post(self, request, *args, **kwargs):
        coupon = self.serializer_class(data=self.request.data, context = {'request' : self.request})
        coupon.is_valid(raise_exception=True)
        return Response(CouponSerializer(coupon.validated_data.get('instance')).data, status=200)