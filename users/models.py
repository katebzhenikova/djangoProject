from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    # token = models.CharField(max_length=20, verbose_name='токен пользователя')
    # is_active = models.BooleanField(default=True, verbose_name='активирован')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

