from .models import Product
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name', 'slug', 'category', 'description', 'price','image', 'stock', 'is_available', 'created_at', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ('-id',)
