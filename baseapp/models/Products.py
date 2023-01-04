from django.db import models
from .category import Category
from .subcategory import SubCategory

class Products(models.Model):
    title= models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products/images/")
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,  on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title+ '  ' +str(self.price)+''
    
    @staticmethod
    def get_all__products(self):
        return Products.objects.all()
    
    @staticmethod
    def get_all__products__id(id):
        return Products.objects.filter(category=id)
    
