from django.shortcuts import render
from orders.models import Order, OrderItem
from utils import  reports_admin_user
from datetime import date
from reports.generators import registered_users_per_month
from products.models import Product

@reports_admin_user
def products_statistics(request):
    today = date.today()
    top_products_chart = Product.objects.all().order_by('-ordered_times')[:10]
    top_products_chart_data = {'product_name' : list(top_products_chart.values_list('title', flat=True)), 'ordered_times' : list(top_products_chart.values_list('ordered_times', flat=True))}
    all_products = Product.objects.all().count()
    active_products = Product.objects.filter(live=True).count()
    products_out_of_stock = Product.objects.filter(in_stock_items__lte=10).count()
    ordered_products_today = len(OrderItem.objects.filter(order__created__date=today).values('product__id').distinct())

    context = {
        'chart' : top_products_chart_data,
        'all_products' : all_products,
        'active_products' : active_products,
        'products_out_of_stock' : products_out_of_stock,
        'ordered_products_today' : ordered_products_today
    }
    return render(request, 'products_stat.html', context)


@reports_admin_user
def products_running_out(request):
    products = Product.objects.filter(in_stock_items__lte=100).order_by('-in_stock_items').select_related('category')
    context = {
        'products' : products
    }
    return render(request, 'products_running_out.html', context)