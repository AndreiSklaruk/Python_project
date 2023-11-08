from django.contrib import admin
from . import models
from products.models import *





admin.site.register(ProductCategory)
admin.site.register(Product)
