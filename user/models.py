from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(
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
        return f'{self.first_name}'
