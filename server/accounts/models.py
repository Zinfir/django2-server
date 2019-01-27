from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from images.models import Image

class Account(AbstractUser):
    avatar = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def __str__(self):
        return self.username

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else :
            return True


class GoogleProfile(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )

    age = models.PositiveIntegerField(verbose_name = 'возраст', default = 18)

    def __str__(self):
        return self.age


class VkProfile(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )

    age = models.PositiveIntegerField(verbose_name = 'возраст', default = 18)

    def __str__(self):
        return self.age
