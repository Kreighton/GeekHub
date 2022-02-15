from django.db import models
from django.urls import reverse
from django.contrib.auth import settings


class ProductCategory(models.Model):
    category_name = models.CharField(default='', max_length=200)
    slug = models.CharField(max_length=200, default='')
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=False)

    product_name = models.CharField(max_length=200, default='')
    product_image = models.ImageField(upload_to='product_imgs/', default='')
    slug = models.CharField(max_length=200, default='')
    product_price = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    product_description = models.TextField(default='')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return f'/product/{self.pk}'


class Order(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    order_items_ids = models.CharField(default='', max_length=200)
    total_cost = models.DecimalField(default=0, decimal_places=2, max_digits=10000)
