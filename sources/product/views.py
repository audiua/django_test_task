from datetime import datetime, timedelta
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import EmptyPage, Paginator
from .models import Category, Product

from django.views.generic import ListView, DetailView, TemplateView


class RecentListView(ListView):
    model = Category

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecentListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        recent_date = datetime.today() - timedelta(days=1)
        return Category.objects.filter(created_at__gte=recent_date)


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    """Category detail view"""
    model = Category


class ProductDetailView(DetailView):
    """Product detail view"""
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])


class HomePageView(TemplateView):
    """Home page"""
    template_name = 'product/base.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context