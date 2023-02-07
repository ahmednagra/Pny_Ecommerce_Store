from .models import CartModel, CartItem
from .views import _cart_id

#ye function hai cart icon ko auto update krny k liya 
def counter(request):
    cart_count = 0
    if 'admin'in request.path:
        return {}
    else:
        try:
            cart = CartModel.objects.filter(cart_id= _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except CartModel.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)                



# ab is c0ntext_processor ko settings.py mein b register krna hai 
