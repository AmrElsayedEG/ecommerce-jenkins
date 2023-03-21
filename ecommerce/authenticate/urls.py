from django.urls import path
from authenticate.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "authenticate"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

    # forget password
    path("forget/password/", ForgetPasswordRequestView.as_view(), name="forget-password"),
    path("forget/check/", CheckForgetPasswordTokenView.as_view(), name="check-token"),
    path("forget/set/", SetForgetPasswordView.as_view(), name="set-password"),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/logout/', LogoutView.as_view(), name="logout"),

    # profile
    path("me/", ProfileView.as_view(), name="profile"),

    # change password
    path("change/password/", ChangePasswordView.as_view(), name='change-password'),
]
