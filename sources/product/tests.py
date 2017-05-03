from django.test import TestCase
from product.models import Category, Product
from django.test import Client
from django.core.urlresolvers import reverse


class TestProduct(TestCase):
    fixtures = ['data.json']

    def test_category_view(self):
        categories = Category.objects.all()
        client = Client()
        for category in categories:
            response = client.get(reverse('product:category', args={category.slug}))
            self.assertEqual(response.status_code, 200)

    def test_product_view(self):
        products = Product.objects.all()
        client = Client()
        for product in products:
            response = client.get(reverse('product:product_detail', args={product.category.slug, product.slug}))
            self.assertEqual(response.status_code, 200)
