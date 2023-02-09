from .models import Product, VariationModel
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name', 'slug', 'category', 'description', 'price','image', 'stock', 'is_available', 'created_at', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ('-id',)


@admin.register(VariationModel)
class VariationModelAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'variation_category', 'variation_value', 'is_active', 'created_at')
    ordering = ('-id',)
    #ab jis b field ko editable krna ho ye tuple hai to comma b add kry
    list_editable= ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')