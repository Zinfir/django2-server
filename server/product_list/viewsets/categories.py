from rest_framework.viewsets import ModelViewSet

from product_list.serializers import CategorySerializer
from product_list.models import Product_Category


class CategoryViewSet(ModelViewSet):
    queryset = Product_Category.objects.all()
    serializer_class = CategorySerializer