from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from carts.models import CartItem, CartModel
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#this function is for geting id from session
# by usin "  _  " before name make it private function 
def _cart_id(request):
    cart = request.session.session_key
    if not cart:        # agr phly se session na ho ho session bna lay gay
        cart = request.session.create()
    return cart    
        
        #add item in cart withoutlogin from session key
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) #get product by id
    
    try:
        # yaha id session se li gai hai
        # private function _cart_id ko request k sath is liya diya k us wqt k session kii id aa jain
        cart = CartModel.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session 
        
    except CartModel.DoesNotExist:
        cart = CartModel.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()    
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        #after add item cart increament 1
        cart_item.quantity +=1 
        cart_item.save()
    # when card item not exist
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            # now add some vsalues
            product = product,
            quantity=1,
            cart = cart,            
            
            )
        cart_item.save()
    #ye function display item in cart 
    #return HttpResponse(cart_item.product)
    #exit()
    return redirect('cart')     
            

def remove_cart(request, product_id):
    #get cart
    cart = CartModel.objects.get(cart_id=_cart_id(request))
    # get product idfrom Product Model
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
   # if quantitiy greater then 1 then increment otherwise decrement 
    if cart_item.quantity>1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')        

                
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax =0 
        grand_total = 0
        # cart object by cart id
        cart = CartModel.objects.get(cart_id=_cart_id(request))
        # cart items looping to get total and quantity
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax= (2 * total)/100
        grand_total = total + tax     
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)
