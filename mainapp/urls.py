from django.urls import path
from django.contrib import admin
from mainapp.views import index, products, product_page

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    # path('<int:pk>/products/', products, name='products'),
    path('products/', products, name='products'),
    path('<int:pk>/product_page/', product_page, name='product_page'),
]