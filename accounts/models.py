from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100 , verbose_name='نام کامل')
    email = models.EmailField(max_length=100, unique=True, verbose_name="آدرس ایمیل")
    is_admin = models.BooleanField(default=False, verbose_name='ادمین است؟')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.is_admin