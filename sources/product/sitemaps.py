from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from .models import Product, Category

class HomeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ['product:home']

    def location(self, obj):
        return reverse(obj)

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.modified_at

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.modified_at