
from utils import send_email
from celery import shared_task
from orders.models import Order

@shared_task
def order_submit_email(name, email):
    # order = Order.objects.get(id=order_id)
    send_email(
            subject="Order Details",
            template_name="order_info.html",
            context={
                    "name" : name,
                    # "order" : order,
                    # "items" : order.ordered_items.all(),
                    # "total" : order.total_cost
            },
            to=[email]
        )
    return