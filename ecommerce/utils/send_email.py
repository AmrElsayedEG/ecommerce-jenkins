from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(subject, template_name, context, to):
    body = render_to_string(template_name, context)
    msg = EmailMultiAlternatives(subject, settings.WEBSITE_NAME, to=to)
    msg.attach_alternative(body, "text/html")
    msg.send()