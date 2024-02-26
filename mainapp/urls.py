from django.urls import path
from django.contrib import admin
from mainapp.views import ProductListView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    # path('', index, name='index'),
    # path('<int:pk>/products/', products, name='products'),
    path('', ProductListView.as_view(), name='products'),
    path('<int:pk>/product_page/', ProductDetailView.as_view(), name='product_page'),
    path('', ProductDetailView.as_view(), name='product_page'),
    path('blog_form_create/', BlogCreateView.as_view(), name='blog_form_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/blog_detail/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/blog_form/', BlogUpdateView.as_view(), name='blog_form'),
    path('<int:pk>/blog_confirm_delete/', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]