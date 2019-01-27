from django.urls import path
from cart.views import (
    PurchaseListView,
    PurchaseCreateView,
    PurchaseDetailView,
    PurchaseUpdateView,
    cart_view,
    )

app_name = 'cart'


urlpatterns = [
    path('', cart_view, name='cart'),
    path('list/', PurchaseListView.as_view(), name='list'),
    path('create/', PurchaseCreateView.as_view(), name='create'),
    path('<pk>/', PurchaseDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PurchaseUpdateView.as_view(), name='update'),
]