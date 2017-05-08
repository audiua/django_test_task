from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^products/recent/$', views.RecentListView.as_view(), name='recent_products'),
    url(r'^products/(?P<category_slug>[a-z0-9]+)/(?P<slug>[a-z0-9]+)/$',
        views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^products/(?P<slug>[a-z0-9]+)/$', views.CategoryDetailView.as_view(),
        name='category_detail'),

    url(r'^products/$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^$', views.HomePageView.as_view(), name='home')
]
