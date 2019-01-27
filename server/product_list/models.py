from django.db import models
from django.urls import reverse_lazy


class Product_Category(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product_list:product_category', kwargs={'pk': self.pk})
