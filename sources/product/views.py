from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    return render(request, 'product/base.html')

def category_list(request):
    """list all categories"""
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {'categories': categories})

def category_detail(request, category_slug):
    """list all products of category"""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category_detail.html', {'category': category,
                                                         'products': products})

def product_detail(request, category_slug, product_slug):
    """Detail product view"""
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product/product_detail.html', {'category': category,
                                                         'product': product})
@login_required(login_url='/login/')
def recent_products(request):
    """recent products for 24 hours"""
    recent_date = datetime.today() - timedelta(days=24)
    products = Product.objects.filter(created_at__gte=recent_date)
    return render(request, 'product/recent_products.html', {'products': products})