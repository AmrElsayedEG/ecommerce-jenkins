from django.shortcuts import render, redirect
from users.models import User
from utils import UserTypeChoices, reports_admin_user
from datetime import date
from reports.generators import registered_users_per_month

@reports_admin_user
def customers_statistics(request):
    today = date.today()
    chart = registered_users_per_month()
    all_users = User.objects.filter(type=UserTypeChoices.CUSTOMER).count()
    active_users = User.objects.filter(type=UserTypeChoices.CUSTOMER, last_login__date=today).count()
    ordered_today = User.objects.filter(type=UserTypeChoices.CUSTOMER, last_order__date=today).count()
    new_users_month = User.objects.filter(type=UserTypeChoices.CUSTOMER, registered__month=today.month, registered__year=today.year).count()

    context = {
        'chart' : chart,
        'all_users' : all_users,
        'active_users' : active_users,
        'ordered_today' : ordered_today,
        'new_users_month' : new_users_month
    }
    return render(request, 'customers_stat.html', context)