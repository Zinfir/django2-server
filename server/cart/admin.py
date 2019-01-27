from django.contrib import admin
from .models import Purchase, PurchaseItem


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem


class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'created',
        'is_active',
    ]

    inlines = [
        PurchaseItemInline
    ]


admin.site.register(Purchase, PurchaseModelAdmin)
admin.site.register(PurchaseItem)
