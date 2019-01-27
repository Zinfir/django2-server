from django.db import models
from datetime import datetime
from django.utils.functional import cached_property


class Image(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True
    )
    value = models.ImageField(
        upload_to='images/'
    )
    @property
    def url(self):
        return self.value.url

    @cached_property
    def get_new_products(self):
        return self.product_set.filter(
            created__lte=datetime.now()
        )[:6]


    def __str__(self):
        return self.name
