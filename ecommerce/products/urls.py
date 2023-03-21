from django.urls import path
from products.views import *

app_name = "products"

urlpatterns = [
    path('category/list/', ListCategoriesView.as_view(), name='list-category'),
    path('category/<int:pk>/', GetCategoryView.as_view(), name='get-one-category'),
    path('list/', ListProductsView.as_view(), name='list-products'),
    path('<int:pk>/', GetProductView.as_view(), name='get-product'),
    path('discount/', ListDiscountProductsView.as_view(), name='discount-products'),
    path('best/all/', BestSellersView.as_view(), name='best-of-all-time'),
]
