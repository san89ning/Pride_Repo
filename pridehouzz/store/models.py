from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from io import BytesIO
from PIL import Image
from userprofile.models import Userprofile

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Brands'
    
    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sizes'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = {
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    }

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(Size, related_name='products', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class SearchTerm(models.Model):
    query = models.TextField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, related_name='searchTerm', on_delete=models.CASCADE)
    no_of_searches = models.IntegerField(default=0)

    def __str__(self):
        return self.query

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    amount = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'OrderItems'
    
    def __str__(self):
        return self.product.title
