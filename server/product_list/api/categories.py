from product_list.models import Product_Category
from rest_framework.viewsets import ModelViewSet
from product_list.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Product_Category.objects.all()
    serializer_class = CategorySerializer
