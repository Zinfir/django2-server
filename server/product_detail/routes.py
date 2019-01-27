from django.urls import path

from .views import product_json_list


app_name = 'rest_product_detail'

urlpatterns = [
    path('', product_json_list, name='list'),
]
