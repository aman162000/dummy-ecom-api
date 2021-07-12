from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=False)
    category_id = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_id = self.category_name.lower()
        super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    product_name = models.CharField(blank=False, max_length=100, null=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_desc = models.TextField(blank=False, null=False)
    product_price = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    product_img_sm = models.ImageField(upload_to='images-150',blank=True)
    product_img_md = models.ImageField(upload_to='images-300',blank=True)
    product_img_lg = models.ImageField(upload_to='images-600',blank=True)
    product_rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    product_quantity = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    product_sales = models.DecimalField(decimal_places=0,max_digits=1000,default=0)

    def __str__(self):
        return self.product_name
