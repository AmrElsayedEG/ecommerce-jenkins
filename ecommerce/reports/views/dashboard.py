from django.shortcuts import render, redirect
from orders.models import Order
from users.models import User
from utils import UserTypeChoices, reports_admin_user
from datetime import date, timedelta
from main.models import AppVersion
from reports.generators import orders_statistics_per_month_order
from main.models import Currency

@reports_admin_user
def dashboard(request):
    currency = Currency.objects.filter(default=True).last()
    orders_chart = orders_statistics_per_month_order()
    app_status = AppVersion.objects.last()
    if request.method == 'POST' and request.POST.get('app_status'):
        status = request.POST.get('app_status')
        app_status.active = True if status == 'active' else False
        app_status.save()
        return redirect('/')

    today = date.today()
    all_users = User.objects.filter(type=UserTypeChoices.CUSTOMER).count()
    today_orders = Order.objects.filter(created__date=today).count()
    yesterday_orders = Order.objects.filter(created__date=today - timedelta(1)).count()
    orders_per = (((today_orders - yesterday_orders) * 100) / yesterday_orders) if yesterday_orders != 0 else 100
    today_users = User.objects.filter(last_login__date=today, type=UserTypeChoices.CUSTOMER).count()
    today_sales = sum(i.total_cost for i in Order.objects.filter(created__date=today))
    context = {
        'all_users' : all_users,
        'today_orders' : today_orders,
        'today_users' : today_users,
        'today_sales' : today_sales,
        'today' : today,
        'yesterday_orders' : yesterday_orders,
        'orders_per' : orders_per,
        'app_status' : app_status.active,
        'orders_chart' : orders_chart,
        'currency' : currency,
    }
    return render(request, 'index.html', context)