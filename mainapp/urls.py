from django.urls import path
from django.contrib import admin
from mainapp.views import index, products
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]