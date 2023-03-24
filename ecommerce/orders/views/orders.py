from orders.serializers import CreateOrderSerializer, OrderDetailsSerializer, CancelOrderSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from utils import IsAuthenticated
from rest_framework.response import Response
from django.db.transaction import atomic
from orders.models import Order
from datetime import datetime
from django.utils.translation import gettext_lazy as _

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
                        'error' : [_('One or more items above the in stock number')]
                    }
                else:
                    error = order.errors
                return Response(error, status=400)
            order.save()
            # save lsat order date
            self.request.user.last_order = datetime.now()
            self.request.user.save()
            return Response({
                    'success': [_("Order created successfully")]
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