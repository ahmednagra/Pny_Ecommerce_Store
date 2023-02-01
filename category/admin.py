from .models import Category
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug', 'description',
                    'cat_image', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('category_name',)}
    ordering = ('-id',)