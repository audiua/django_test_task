import datetime

from django.test import TestCase
from django.utils import timezone
from django.test.client import Client
from product.models import Category, Product
from django.core.urlresolvers import reverse


def create_product(name, category, days, price=20.20):
    time = timezone.now() + datetime.timedelta(days=days)
    return Product.objects.create(name=name, slug=name.replace(' ', '').lower(), price=price,
                                   created_at=time, category=category)

class TestApp(TestCase):

    def setUp(self):
        from django.test.utils import setup_test_environment
        setup_test_environment()

        self.category = Category.objects.create(name='Category 1', slug='category1')

    def test_recent_login_required(self):
        create_product(name='Product 1', price=20.20, category=self.category, days=0)
        response = self.client.get(reverse('product:recent_products'), follow=True)
        self.assertEquals(response.status_code, 200)

    def test_category_list(self):
        """test """
        Category.objects.create(name='Category 2', slug='category2')

        response = self.client.get(reverse('product:category_list'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<Category: Category 1>', '<Category: Category 2>']
        )

    def test_category_detail(self):
        """test """
        create_product(name='Product 1', price=20.20, category=self.category, days=0)
        create_product(name='Product 2', price=30.20, category=self.category, days=0)

        response = self.client.get(reverse('product:category_detail', args=[self.category.slug]))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['products'],
            ['<Product: Product 1>', '<Product: Product 2>']
        )

    def test_product_detail(self):
        """test """
        product = create_product(name='Product 1', price=20.20, category=self.category, days=1)

        response = self.client.get(product.get_absolute_url())
        self.assertEquals(response.status_code, 200)
        self.assertEqual(
            response.context['product'].name,
            'Product 1'
        )