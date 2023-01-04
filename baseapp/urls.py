from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= 'homepage'),
    path('login/', login, name='loginpage'),
    path('register/', register, name='register'),
]
