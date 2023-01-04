from importlib.resources import path
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register, name='register'),
    # path('login/',views.login, name='login'),
    # path('logout/',views.logout, name='logout'),
    # another way access html without define defination
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',views.profile, name='profile'),
           
] 


"""

path("users/", include("django.contrib.auth.urls")), 

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

"""