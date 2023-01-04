from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models.category import Category
from baseapp.models.Products import Products
from baseapp.models.subcategory import SubCategory
# Create your views here.
def index(request):
    id=request.GET.get("id")
    if id:
        prod = Products.get_all__products__id(id)
    else:
        prod = Products.get_all__products(request)
    #method 1 data load
    ctrs=Category.objects.all()
    subcat = SubCategory.objects.all()
#method 2 with static method
#ye data staticmethod se laykr aay hai aur static method product mldel mein define kiya hai
    
    print(prod)
    context = {
        "subcat":subcat,
        "category": ctrs,
        "products": prod
    }
    return render(request, 'baseapp/index.html', context)


def login(request):
    return render(request, 'baseapp/login.html')


def register(request):
    return render(request, 'baseapp/signup.html')
