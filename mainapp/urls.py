from django.urls import path
from django.contrib import admin
from mainapp.views import index

urlpatterns = [
    path('', index)
]