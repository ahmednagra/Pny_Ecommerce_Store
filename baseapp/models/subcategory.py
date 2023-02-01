from django.db import models
from category.models import Category

class SubCategory(models.Model):
    SubCategory = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.SubCategory
    
    