from django.shortcuts import render, redirect
from orders.models import Order
from utils import  reports_admin_user, OrderStatusChoices
from datetime import date
from reports.generators import orders_statistics_per_month_order, statistics_filter_order
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string
from main.models import Currency

@reports_admin_user
def orders_statistics(request):
    currency = Currency.objects.filter(default=True).last()
    today = date.today()
    year_chart = orders_statistics_per_month_order()
    month_chart = statistics_filter_order('Lmonth')
    week_chart = statistics_filter_order('Lweek')
    all_orders = Order.objects.all()
    pie_chart = (Order.objects.values('status').annotate(count=Count('status')).order_by())
    today_orders = Order.objects.filter(created__date=today).count()
    today_sales = sum(i.total_cost for i in Order.objects.filter(created__date=today, status=OrderStatusChoices.DELIVERED))
    overall_sales = sum(i.total_cost for i in Order.objects.filter(status=OrderStatusChoices.DELIVERED))
    context = {
        'year_chart' : year_chart,
        'month_chart' : month_chart,
        'week_chart' : week_chart,
        'all_orders' : all_orders.count(),
        'today_orders' : today_orders,
        'pie_chart' : pie_chart,
        'today_sales' : today_sales,
        'overall_sales' : overall_sales,
        'currency' : currency
    }
    return render(request, 'orders_stat.html', context)

@reports_admin_user
def all_orders(request):
    orders = Order.objects.all().select_related('customer', 'currency').order_by('-created')
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    if page_number and not page_number.isdigit():
        return redirect('reports:unauthorized')
    page_obj = paginator.get_page(page_number)

    # Pagination Bar
    if page_number is not None and page_number not in ['1', '2'] and page_obj.paginator.num_pages > 5:
        previous = int(page_number) - 2
        next = int(page_number) + 3
        if int(page_number) == page_obj.paginator.num_pages:
            previous = int(page_number) - 4
        elif int(page_number)+1 >= page_obj.paginator.num_pages:
            previous = int(page_number) - 3
        if next > page_obj.paginator.num_pages:
            next = page_obj.paginator.num_pages + 1
        pagin_range = range(previous, next)
    else:
        previous = 1
        next = 6
        if next > page_obj.paginator.num_pages:
            next = page_obj.paginator.num_pages + 1
        pagin_range = range(previous, next)
    context = {
        'orders' : page_obj,
        'pagin_range' : pagin_range,
        'page_number' : int(page_number) if page_number else page_number,
    }
    return render(request, 'all_orders.html', context)

@reports_admin_user
def one_order(request, order_no):
    if request.method == 'POST' and request.POST.get('status'):
        order = Order.objects.filter(order_no=order_no).update(status=request.POST.get('status'))
    order = Order.objects.filter(order_no=order_no).select_related('customer', 'coupon', 'shipping_fees', 'address', 'address__country', 'address__city', 'currency').last()
    if not order:
        return redirect('reports:unauthorized')
    items = order.ordered_items.all().select_related('product', 'product__category').values('product__title', 'product__category__title', 'type', 'quantity', 'price')
    context = {
        'order' : order,
        'items' : items
    }
    return render(request, 'one_order.html', context)

@reports_admin_user
def order_pdf(request, id):
    order = Order.objects.select_related('customer', 'currency').filter(id=id).last()
    if not order:
        return redirect('reports:unauthorized')
    template = render_to_string("order-pdf.html", {'pagesize':'A3', 'order' : order, 'items' : order.ordered_items.all().select_related('product')})
    html = HTML(string=template, base_url=request.build_absolute_uri())
    result = html.write_pdf()
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = f'attachment; filename=order-{order.order_no}.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response