from django.contrib.auth.models import AbstractUser
from django.db import models
import random

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    user_phone = models.CharField(max_length=11, verbose_name='телефон', **NULLABLE)
    user_avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    user_country = models.CharField(max_length=11, verbose_name='Страна', **NULLABLE)
    verify_code = models.CharField(max_length=4, default=code, verbose_name='Код вeрификации')
    is_verified = models.BooleanField(default=False, verbose_name='Верификация')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
