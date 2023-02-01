from django.contrib import admin
from .models.subcategory import SubCategory
# Register your models here.


#admin.site.register(Category)

admin.site.register(SubCategory)


"""
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'category','description', 'price', 'image', 'stock', 'is_available', 'created_at', 'modified_date')
    prepopulated_fields = {'slug':('product_name',)}
"""