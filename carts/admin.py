from django.contrib import admin
from .models import CartItem, CartModel
# Register your models here.


@admin.register(CartModel)
class CartModeldmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'date_added')
    ordering = ('-id',)
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity', 'is_active')
    ordering = ('-id',)
