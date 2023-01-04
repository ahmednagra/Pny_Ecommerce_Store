from django.contrib import admin
from .models.category import Category
from .models.Products import Products
from .models.subcategory import SubCategory
# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SubCategory)
