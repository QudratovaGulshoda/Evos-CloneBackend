from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from datetime import datetime
from utils.models import BaseModel


# Create your models here.
class SubCategory(BaseModel):
    title = models.CharField(max_length=255,verbose_name="SubCategory name")

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'SubCategories'
        verbose_name = "SubCategory "
        verbose_name_plural = "SubCategories "


class Category(BaseModel):
    title = models.CharField(max_length=255,verbose_name="Category name")
    image = models.ImageField(upload_to="category-image",verbose_name="Category Image",
                              help_text="Upload Categories' Image",null=True,blank=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def Last_Updated(self):
        time = self.updated_at
        times = time.strftime("%m/%d/%Y, %H:%M:%S")
        return times

    @property
    def Category_Picture(self):
        if self.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))

    @property
    def Products_Count(self):
        items = self.products.all()
        return len(items)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Categories'
        verbose_name = "Category "
        verbose_name_plural = "Categories "


class Product(BaseModel):
    title = models.CharField(max_length=255,verbose_name="Product Name",help_text="Enter product name")
    description = models.TextField(verbose_name="About Product",help_text="Field for Product's description",null=True,blank=True)
    price = models.IntegerField(default=0,verbose_name="Product's Price",help_text="Enter product's price")
    discount = models.IntegerField(default=0,verbose_name="Product's discount price",help_text="Enter product's discount price")
    image = models.ImageField(upload_to="product-image", verbose_name="Product Image",
                              help_text="Upload Product's Image",null=True,blank=True)

    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,verbose_name="Product's Subcategory",
                                    help_text="Choose Subcategory",related_name='products',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,verbose_name="Product's Category",
                                 help_text="Choose Category",related_name='products')



    @property
    def Last_Updated(self):
        time = self.updated_at
        times = time.strftime("%m/%d/%Y, %H:%M:%S")
        return times

    @property
    def Product_Picture(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))

    @property
    def user(self):
        return self.category.user

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Products'
        verbose_name = "Product "
        verbose_name_plural = "Products "
