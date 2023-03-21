from django.urls import path
from reports.views import *

app_name = 'reports'

urlpatterns = [
    path('login/', login_process, name='login'),
    path('logout/', logout_process, name='logout'),
    path('', dashboard, name='dashboard'),

    # customers
    path('customers/statistics/', customers_statistics, name='customer-statistics'),

    # products
    path('products/statistics/', products_statistics, name='product-statistics'),
    path('products/stock/', products_running_out, name='products-running-out'),

    # orders
    path('orders/statistics/', orders_statistics, name='order-statistics'),
    path('orders/all/', all_orders, name='all-orders'),
    path('orders/<int:order_no>/', one_order, name='one-order'),
    path('orders/pdf/<int:id>/', order_pdf, name='order-pdf'),

    # reports
    path('reports/sheets/', sheets, name='sheets'),
    path('reports/export/<str:type>/', export_sheet, name='export-sheets'),

    # errors
    path('error/', unauthorized, name='unauthorized')
]
