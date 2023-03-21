from django.shortcuts import render, redirect
from utils import ProductsExcel, OrdersExcel, CustomersExcel, UserTypeChoices
from products.models import Product
from orders.models import Order
import datetime
from users.models import User

def sheets(request):
    return render(request, 'sheets.html')

def export_sheet(request, type):
    today = datetime.date.today()
    if type == 'all-products':
        return ProductsExcel.export_as_csv(queryset=Product.objects.all())
    elif type == 'all-orders':
        return OrdersExcel.export_as_csv(queryset=Order.objects.all().select_related('customer'))
    elif type == 'current-month-orders':
        return OrdersExcel.export_as_csv(queryset=Order.objects.filter(created__year=today.year, created__month=today.month).select_related('customer'))
    elif type == 'last-month-orders':
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        return OrdersExcel.export_as_csv(queryset=Order.objects.filter(created__year=last_month.year, created__month=last_month.month).select_related('customer'))
    elif type == 'current-year-orders':
        return OrdersExcel.export_as_csv(queryset=Order.objects.filter(created__year=today.year).select_related('customer'))
    elif type == 'last-year-orders':
        return OrdersExcel.export_as_csv(queryset=Order.objects.filter(created__year=today.year - 1).select_related('customer'))
    elif type == 'all-customers':
        return CustomersExcel.export_as_csv(queryset=User.objects.filter(type=UserTypeChoices.CUSTOMER))
    else:
        return redirect('reports:unauthorized')