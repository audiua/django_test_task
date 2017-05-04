from django.test import TestCase

from product.models import Category, Product

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='car', slug='car')

    def test_name_label(self):
        self.assertEquals(self.category.name, 'car')

    def test_first_name_max_length(self):
        max_length = self.category._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(category.get_absolute_url(),'/products/car/')

class ProductModelTest(TestCase):

    def setUp(self):
        #Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name='car', slug='car')
        self.product = Product.objects.create(name='audi', slug='audi', price=20.22, category=self.category)

    def test_name(self):
        self.assertEquals(self.product.name,'audi')

    def test_first_name_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_get_absolute_url(self):
        #This will also fail if the urlconf is not defined.
        self.assertEquals(self.product.get_absolute_url(),'/products/car/audi/')