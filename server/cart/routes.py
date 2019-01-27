from django.urls import path

from .views import PurchaseCreateView


app_name = 'cart_api'

urlpatterns = [
    path('create/', PurchaseCreateView.as_view(), name='create'),
]
