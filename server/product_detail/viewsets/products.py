from functools import reduce
from django.db.models import Q
from django.shortcuts import get_list_or_404
from rest_framework.viewsets import ModelViewSet

from product_detail.serializers import ProductSerializer
from product_detail.models import Product


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query_params = (
            (key, list(map(int, value.split(','))) if key.endswith('_in') else value)
            for key, value in self.request.GET.items()
        )

        return Product.objects.filter(
            reduce(
                lambda store, itm: store | Q(**{itm[0]: itm[1]}),
                query_params,
                Q()
            )
        )