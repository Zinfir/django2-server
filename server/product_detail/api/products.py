from product_detail.models import Product
from rest_framework.viewsets import ModelViewSet
from product_detail.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(special_offer='Trending')
    serializer_class = ProductSerializer


class ProductListLeftViewSet(ModelViewSet):
    queryset = Product.objects.filter(pk=16)
    serializer_class = ProductSerializer

class ProductListRightViewSet(ModelViewSet):
    queryset = Product.objects.filter(pk=15)
    serializer_class = ProductSerializer