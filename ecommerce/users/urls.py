from django.urls import path
from users.views import *

app_name = "user"
urlpatterns = [
    # address
    path('address/list/', ListCountriesAndCities.as_view(), name='list-all'),
    path('address/add/', AddUserAddress.as_view(), name='add-address'),
    path('address/remove/<int:pk>/', RemoveUserAddress.as_view(), name='remove-address'),
    path('address/shipping/', AddressShippingFees.as_view(), name='address-shipping-fees'),

    # wishlist
    path('wishlist/list/', ListWishListView.as_view(), name='list-wishlist'),
    path('wishlist/add/', AddWishListView.as_view(), name='add-wishlist'),
    path('wishlist/remove/<int:pk>/', RemoveWishListView.as_view(), name='remove-wishlist'),

    # Users
    path('change/info/', UpdateUserInfoView.as_view(), name='change-info'),
    path('change/email/token/', UpdateUserEmailTokenView.as_view(), name='get-token-email'),
    path('change/email/set/', UpdateUserEmailView.as_view(), name='change-email'),
]
