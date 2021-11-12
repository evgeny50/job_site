from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(
        _('phone number'),
        unique=True,
        blank=True,
        null=True,
    )
    is_moderator = models.BooleanField(
        default=False)
    is_employer = models.BooleanField(
        default=False
    )
    is_aspirant = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username

