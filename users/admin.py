from django.contrib import admin
from .models import AccountModel

#admin dashboard pe password readolny ho na k editable
from django.contrib.auth.admin import UserAdmin

AccountModel
# Register your models here.

@admin.register(AccountModel)
class AccountModelAdmin(UserAdmin):
   list_display = ('first_name', 'last_name',
                    'username', 'email', 'phone_number','date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')
   list_display_links =('email', 'first_name', 'last_name')
   
   readonly_fields = ('last_login', 'date_joined')
   #show record in descending order
   ordering = ('-date_joined',)
   
   filter_horizontal = ()
   list_filter = ()
   fieldsets=()
   
   search_fields = ['first_name', 'last_name',
                     'username', 'email', 'phone_number']
   list_per_page = 10
 
