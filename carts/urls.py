from django.urls import path
from .views import *

urlpatterns = [
    
path('', cart, name='cart' ),
path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
# cart quantity decrement k liya url 
path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'),

]
