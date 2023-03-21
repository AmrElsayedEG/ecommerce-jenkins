from rest_framework.permissions import BasePermission, IsAuthenticated
from utils import UserTypeChoices
import functools
from django.shortcuts import redirect

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.user_type == UserTypeChoices.ADMIN)

def reports_admin_user(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == UserTypeChoices.ADMIN:
                return view_func(request,*args, **kwargs)
            return redirect("reports:unauthorized")
        return redirect("reports:login")
    return wrapper