from django import forms
from .models import PurchaseItem


class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = [
            'product',
            'value',
        ]
        