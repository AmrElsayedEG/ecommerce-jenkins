from .login import LoginView
from .register import RegisterView
from .password import ForgetPasswordRequestView, CheckForgetPasswordTokenView, SetForgetPasswordView, ChangePasswordView
from .profile import ProfileView
# from .logout import LogoutView

__all__ = [
    'LoginView',
    'RegisterView',
    'ForgetPasswordRequestView',
    'CheckForgetPasswordTokenView',
    'SetForgetPasswordView',
    'ProfileView',
    # 'LogoutView',
    'ChangePasswordView',
]