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


class VariationManager(models.Model):
    def all(self):
        return super(VariationManager, self).filter(active=True)
    
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

# color and size k liya 
variation_category_choice = (
    ('color' , 'color'),
    ('size', 'size'),
)


class VariationModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category= models.CharField(max_length=200, choices=variation_category_choice, default='size')
    variation_value = models.CharField(max_length=200)
    is_active= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #ab model ko btana hai k oper wala model tery liya bnaya hai
    objects = VariationManager()

   # def __str__(self):
    #    return str(self.product)
    
    def __unicode__(self):
        return self.product