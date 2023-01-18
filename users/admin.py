from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
   list_display = ['firstname', 'lastname','username', 'email', 'password', 'created_at']
   search_fields = ['firstname', 'lastname','username', 'email', 'password', 'created_at']
   list_per_page = 10
    
