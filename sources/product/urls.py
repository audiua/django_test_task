from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^products/recent/$', views.recent_products, name='recent_products'),
    url(r'^products/(?P<category_slug>[a-z0-9]+)/(?P<product_slug>[a-z0-9]+)/$',
        views.product_detail, name='product_detail'),
    url(r'^products/(?P<category_slug>[a-z0-9]+)/$', views.category_detail,
        name='category_detail'),
    url(r'^products/$', views.category_list, name='category_list'),
    url(r'^$', views.home, name='home')
]
