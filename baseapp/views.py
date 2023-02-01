from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from store.models import Product
from baseapp.models.subcategory import SubCategory
# Create your views here.
def index(request):
    id=request.GET.get("id")
    if id:
        prod = Product.get_all__products__id(id)
    else:
        prod = Product.get_all__products(request).filter(is_available=True)
    #method 1 data load
    ctrs=Category.objects.all()
    #subcat = SubCategory.objects.all()
    
    print(prod)
    context = {
        #"subcat":subcat,
        "category": ctrs,
        "products": prod,
    }
    return render(request, 'baseapp/index.html', context)


def login(request):
    return render(request, 'baseapp/login.html')


def register(request):
    return render(request, 'baseapp/signup.html')
