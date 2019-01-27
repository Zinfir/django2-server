from rest_framework import serializers

from product_list.models import Product_Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    my_absolute_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product_Category
        fields = [
            'url',
            'name',
            'description',
            'modified',
            'created',
            'my_absolute_url',
            ]   

    def get_my_absolute_url(self, obj):
        return obj.get_absolute_url()