from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Модель пользователя """

    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='имя', blank=True)
    last_name = models.CharField(max_length=150, verbose_name='фамилия', null=True)
    username = models.CharField(max_length=20, verbose_name='логин', unique=True)
    password = models.CharField(max_length=200, verbose_name='пароль')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
