from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles(models.TextChoices):
    USER = 'user', _('Пользователь')
    ADMIN = 'admin', _('Администратор')


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('Имя пользователя'))
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name=_('Фамилия пользователя'))
    phone = PhoneNumberField(null=False, blank=False, verbose_name=_('Телефон для связи'))
    email = models.EmailField(max_length=254, unique=True, verbose_name=_('Электронная почта'))
    role = models.CharField(max_length=5, choices=UserRoles.choices, default='user', verbose_name=_('Роль'))
    image = models.ImageField(upload_to='post_images/', null=True, blank=True, verbose_name=_('Аватарка'))
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'phone')

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email
