from django import forms

from product_list.models import Product_Category


class Category_Form(forms.ModelForm):
    class Meta:
        model = Product_Category
        fields = [
            'name',
            'description'
            ]
