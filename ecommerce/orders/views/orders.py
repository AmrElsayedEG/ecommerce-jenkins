from orders.serializers import CreateOrderSerializer, OrderDetailsSerializer, CancelOrderSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from utils import IsAuthenticated
from rest_framework.response import Response
from django.db.transaction import atomic
from orders.models import Order
from datetime import datetime

class CreateOrderView(CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated,]

    @atomic
    def post(self, request, *args, **kwargs):
            order = self.serializer_class(data=request.data, context={'request' : self.request})
            if not order.is_valid():
                if order.errors.get('order'):
                    error = order.errors.get('order')
                elif order.errors.get('items'):
                    error = []
                    for item in order.errors['items']:
                        if item.get('item'):
                            error.append(item['item'][0].title())
                    error = {
                        'error' : [f'These items above the in stock number, {error}'],
                        'error_ar' : [f'{error} ,الكمية المطلوبة من هذه المنتجات أكبر من الكمية المتاحة']
                    }
                else:
                    error = order.errors
                return Response(error, status=400)
            order.save()
            # save lsat order date
            self.request.user.last_order = datetime.now()
            self.request.user.save()
            return Response({
                    'success': "Order created successfully",
                    'success_ar': "تم إنشاء الطلب بنجاح",
            })

class MyOrdersView(ListAPIView):
    queryset = Order
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = None

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created')

class CancelOrderView(UpdateAPIView):
    queryset = Order
    serializer_class = CancelOrderSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'order_no'