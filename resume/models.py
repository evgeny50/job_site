# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from user.models import CustomUser


class Resume(models.Model):
    """Fields for creating a resume"""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='resume'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='First name'
    )
    second_name = models.CharField(
        max_length=255,
        verbose_name='Second name'
    )
    salary = models.IntegerField(
        verbose_name='Salary',
        blank=True,
        null=True
    )
    education = models.TextField(
        verbose_name='Education',
        blank=True,
        null=True
    )
    experience = models.TextField(
        verbose_name='Experience'
    )
    portfolio = models.CharField(
        max_length=350,
        verbose_name='Portfolio'
    )
    specialty = models.ForeignKey(
        'Specialty',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Specialty'
    )
    grade = models.ForeignKey(
        'Grade',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Grade'
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Status'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list_resume', kwargs={'pk': self.pk})


class Grade(models.Model):
    """User grade"""
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )

    def __str__(self):
        return self.title


class Status(models.Model):
    """Resume statuses"""
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )

    def __str__(self):
        return self.title


class Specialty(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )

    def __str__(self):
        return self.title
