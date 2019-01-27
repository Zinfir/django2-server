from django.urls import path

from main import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('test/', views.test, name='test'),
    path('history/', views.index, name='history'),
    path('showroom/', views.index, name='showroom'),
]