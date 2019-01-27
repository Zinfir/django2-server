from django.contrib import admin
import datetime
from product_detail.models import Product
from django.template.loader import render_to_string


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'picture', 'name', 'product_category',
        'price', 'modified', 'created', 'is_new', 'is_active'
    ]

    list_filter = [
        'product_category', 'image',
        'created', 'modified', 'is_active', 'special_offer',
    ]

    search_fields = [
        'name', 'description', 'price',
    ]

    fieldsets = (
        (
            None, {
                'fields': ('name', 'product_category', 'special_offer', 'is_active')
            }
        ),
        (
            'Content', {
                'fields': ('image', 'description', 'price')
            }
        )
    )

    def picture(self, obj):
        return render_to_string(
            'product_detail/components/picture.html',
            {'image': obj.image.url}
        )


    def is_new(self, obj):
        today = datetime.datetime.now()
        return obj.created.date() >= today.date()
