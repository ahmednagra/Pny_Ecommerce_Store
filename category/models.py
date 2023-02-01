from django.db import models
import datetime
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(
        upload_to='media/category/images', blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
# is function mein get_url liya aur reverse mein products_by_category path url aur then field value slug attache ki aur fun use kiya store/topbat.html m=file mein
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
            
        
    def __str__(self):
        return self.category_name
