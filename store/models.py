from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/products/images/")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
#    subcategory = models.ForeignKey(SubCategory,  on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product_name + '  ' + str(self.price)+''

    @staticmethod
    def get_all__products(self):
        return Product.objects.all()

    @staticmethod
    def get_all__products__id(id):
        return Product.objects.filter(category=id)
    
    # self mean Product k anr category ki field jo foreignky se category model se clug ko fetch
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
