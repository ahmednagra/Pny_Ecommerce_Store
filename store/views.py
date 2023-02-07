from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product
from category.models import Category
from carts.models import CartItem
#import _cart_id function
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.


def store(request, category_slug=None):
    category = None
    products=None
    
    if category_slug !=None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('id')
        # Create a Paginator with the queryset
        paginator = Paginator(products, 6)
        # Get the page number from the request
        page_number = request.GET.get('page')
        # Get the requested page from the paginator
        page_product = paginator.get_page(page_number)

        product_count = products.count()
    else:        
        products= Product.objects.all().filter(is_available=True).order_by('id')
        # Create a Paginator with the queryset
        paginator = Paginator(products, 6)
        # Get the page number from the request
        page_number = request.GET.get('page')
        # Get the requested page from the paginator
        page_product = paginator.get_page(page_number)
    
        product_count = products.count()
        category = Category.objects.all()
    context = {
        'products': page_product,
        'product_count': product_count,
        'category ': category,
        
    }
    return render(request, 'store/store.html', context)


def storedetail(request):
    products = Product.objects.all().filter(is_available=True)
    # display product count
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
            # category__slug is syntax to get slug field of the category
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        #if this particular product exist or not in cart 
        # here cart__  is the foreignkey of CartItem Model for CartModel
        #first access cart field in CartItem then with fori=eign key get cartid from Cart model
        in_cart= CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()       
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart' : in_cart,
    }
        
    return render(request, 'store/product_detail.html', context)


def search(request):
    #agr keyword get request meinho to us ko variable mein save kr liya
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
    if keyword:
        products = Product.objects.order_by(
            '-created_at').filter(Q(description__contains=keyword) | Q(product_name__contains=keyword))
        product_count = products.count()
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
