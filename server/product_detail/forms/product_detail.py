from django import forms

from product_detail.models import Product


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_category',
            'name',
            'image',
            'short_desc',
            'description',
            'special_offer',
            'price',
            'quantity',
            ]
