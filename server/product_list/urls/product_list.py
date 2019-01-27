from django.urls import path

from product_list.views import (
    category_detail,
    category_create, category_update,
    category_delete, category_list, CategoryDetailView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    CategoryListView,
    )
from product_detail.views import ProductListView, product_list
from django.views.decorators.cache import cache_page

app_name = 'product_list'


urlpatterns = [
    path(
        '<int:pk>',
        cache_page(3600)(product_list),
        name='product_category'
    ),
    path('detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]