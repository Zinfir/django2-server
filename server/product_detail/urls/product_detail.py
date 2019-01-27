from django.urls import path

from product_detail.views.product_detail import (
    product_list, ProductListView,
    ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView,
    )



app_name = 'product_detail'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
]