from django.db import models

from vacancy.models import Vacancy


class User(models.Model):
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Пароль')


class Manger(models.Model):
    pass
