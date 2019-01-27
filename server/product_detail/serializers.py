from rest_framework import serializers

from product_list.models import Product_Category
from product_detail.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    product_category = serializers.SerializerMethodField()
    my_absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'url',
            'product_category',
            'name',
            'image',
            'short_desc',
            'description',
            'special_offer',
            'price',
            'quantity',
            'my_absolute_url',
            ]

    def get_image(self, obj):
        return obj.image.url

    def get_product_category(self, obj):
        return obj.product_category.name

    def get_my_absolute_url(self, obj):
        return obj.get_absolute_url()
