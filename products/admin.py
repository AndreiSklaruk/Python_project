from django.contrib import admin
from . import models
from products.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')
    list_filter = ('category',)
    ordering = ('name', 'price')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')
