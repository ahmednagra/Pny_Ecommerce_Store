from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyAccountManger(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User Email address is Mandatory')
        if not username:
            raise ValueError(' User NAme is MAndatory')
        #normalize_email mean when we write in captitol letter convert it to small letter
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    #create Super User and their permissions
    
    def create_superuser(self, first_name, last_name, username, email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password= password,
            first_name=first_name,
            last_name=last_name,
        )
        #now gave the permissins 
        user.is_admin= True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
        
        
class AccountModel(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    #required fields
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    
    #login with email not username
    USERNAME_FIELD= 'email'
    #Required Fields
    REQUIRED_FIELDS =['username', 'first_name', 'last_name'] 
    
    
    #now we tell the account we are using myaccount manger for all operations
    objects = MyAccountManger()
    
    
    def __str__(self):
        return f'({self.first_name}, {self.last_name})'
    
    
    #mandatory Methods agr admin ho to timam permissions ho ge
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    #specify Function
    def has_module_perms(self, add_label ):
        return True
    