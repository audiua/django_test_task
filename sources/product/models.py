from django.db import models
from django.core.urlresolvers import reverse

class BaseModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class Category(BaseModel):
    """Category model"""
    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('product:category_detail', args=[self.slug])

    def __str__(self):
        return self.name

class Product(BaseModel):
    """Product model"""
    category = models.ForeignKey(Category, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "products"

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name