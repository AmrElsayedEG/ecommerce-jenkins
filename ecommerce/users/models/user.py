from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.contrib.auth.models import UserManager
from utils import UserTypeChoices


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and -/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(max_length=150,
                                  help_text="should be alpha only with max length 50")

    last_name = models.CharField(max_length=150,
                                  help_text="should be alpha only with max length 50")

    email = models.EmailField(_('email address'), validators=[EmailValidator], unique=True)

    phone = models.CharField(max_length=20, unique=True)

    type = models.SmallIntegerField(choices=UserTypeChoices.choices, default=UserTypeChoices.CUSTOMER)

    location = models.JSONField(blank=True, null=True)

    user_token = models.CharField(blank=True, null=True, max_length=500)

    last_order = models.DateTimeField(blank=True, null=True)

    requested_token = models.CharField(blank=True, null=True, max_length=500)

    registered = models.DateTimeField(auto_now_add=True)
    

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True
        db_table = 'users'

    def __str__(self) -> str:
        return str(self.email)

class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'