import unidecode

# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from user.models import CustomUser


class Company(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Url',
        null=False
    )
    city = models.CharField(
        max_length=255,
        verbose_name='Город'
    )
    logo = models.ImageField(
        upload_to='company/%Y/%m/%d/',
        verbose_name='Логотип',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Информация о компании'
    )
    employee_count = models.IntegerField(
        default=0,
        verbose_name='Количество сотрудников'
    )
    owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = unidecode.unidecode(self.name).lower()
        self.slug = slugify(value, allow_unicode=False)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('company', kwargs={'company': self.slug})

    class Meta:
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'
