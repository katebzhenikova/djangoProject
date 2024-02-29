from django.contrib import admin

from mainapp.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_category', 'is_active',)
    list_filter = ('product_category', 'product_name', 'description',)
    search_fields = ('product_name', 'description', 'is_active',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'vers_is_active',)
    list_filter = ('version_name',)
