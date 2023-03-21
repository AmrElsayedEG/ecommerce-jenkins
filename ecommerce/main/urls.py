from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from main.views import *

app_name = "main"

urlpatterns = [
    path('openapi/', get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url':'main:openapi-schema'}
    ), name='swagger-ui'),
    path('banners/', ListBannersView.as_view(), name='list-banners'),
    path('coupon/list/', ListActiveCouponsView.as_view(), name='list-coupons'),
    path('coupon/check/', CheckCouponView.as_view(), name='check-coupun'),
    path('version/', GetAppVersionView.as_view(), name='app-version'),

    # App home page data
    path('home/', AppHomeView.as_view(), name='home-data'),
]
