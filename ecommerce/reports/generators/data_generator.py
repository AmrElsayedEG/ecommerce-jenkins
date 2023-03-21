from datetime import date
from orders.models import Order
from users.models import User
from utils import UserTypeChoices
import datetime

def orders_statistics_per_month_order():
    months = ["01", "02","03","04","05","06","07","08","09","10","11","12"]
    today = date.today()
    data = []
    for i in months:
        data.append(Order.objects.filter(created__month=i, created__year=today.year).count())
    return {"data" : data, "date" : months}

def registered_users_per_month():
    months = ["01", "02","03","04","05","06","07","08","09","10","11","12"]
    today = date.today()
    data = []
    for i in months:
        data.append(User.objects.filter(type=UserTypeChoices.CUSTOMER, registered__month=i, registered__year=today.year).count())
    return {"data" : data, "date" : months}

def statistics_filter_order(timeframe):
    if timeframe == 'Lweek':
        timeframe = 7
    elif timeframe == 'Lmonth':
        timeframe = 30
    timeframe = int(timeframe)
    today = date.today()
    end = today + datetime.timedelta(days=-timeframe)
    dates = []
    delta = today - end
    for i in range(delta.days + 1):
        dates.append(end + datetime.timedelta(days=i))

    data = []
    for i in dates:
        data.append(Order.objects.filter(created__date=i).count())

    dates = []
    for i in range(delta.days + 1):
        x = end + datetime.timedelta(days=i)
        dates.append(x.strftime('%m/%d/%Y'))

    return {"date" : dates, "data" : data}