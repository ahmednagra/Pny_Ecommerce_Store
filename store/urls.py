from django.urls import path
from .views import *


urlpatterns = [
    path('', store, name='store_homepage'),
    path('<slug:category_slug>/', store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         product_detail, name='product_detail'),

    path('storedetail', storedetail, name='store_detailpage'),
    # path('login/', login, name='loginpage'),
    # path('register/', register, name='register'),
]
