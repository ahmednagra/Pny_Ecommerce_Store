from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    category = None
    products=None
    
    if category_slug !=None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:        
        products= Product.objects.all().filter(is_available=True)
        product_count = products.count()
        category = Category.objects.all()
    context = {
        'products': products,
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
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
        
    return render(request, 'store/product_detail.html', context)
