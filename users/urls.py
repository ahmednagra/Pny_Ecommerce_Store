from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth

##### user related path##########################
urlpatterns = [

    path('', user_view.Login, name='loginpage'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout1'),
    path('register/', user_view.register, name='register'),

]