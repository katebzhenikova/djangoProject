from django.urls import path
from django.contrib import admin
from mainapp.views import ProductListView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, toggle_activity, ProductCreateView, ProductUpdateView, ProductDeleteView

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [

    path('', ProductListView.as_view(), name='products'),
    path('product_form_create/', ProductCreateView.as_view(), name='product_form_create'),
    path('<int:pk>/product_form/', ProductUpdateView.as_view(), name='product_form'),
    path('<int:pk>/product_page/', ProductDetailView.as_view(), name='product_page'),
    path('<int:pk>/product_confirm_delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),

    path('blog_form_create/', BlogCreateView.as_view(), name='blog_form_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/blog_detail/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/blog_form/', BlogUpdateView.as_view(), name='blog_form'),
    path('<int:pk>/blog_confirm_delete/', BlogDeleteView.as_view(), name='blog_confirm_delete'),
    path('<int:pk>/activity/', toggle_activity, name='toggle_activity'),

]