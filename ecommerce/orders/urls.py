from django.urls import path
from orders.views import *

app_name = "orders"
urlpatterns = [
    path('', MyOrdersView.as_view(), name='list-my-orders'),
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('cancel/<int:order_no>/', CancelOrderView.as_view(), name='cancel-order'),
]
