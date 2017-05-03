from django import template
from product.models import Category
register = template.Library()


@register.inclusion_tag('product/product_menu.html', name='product_menu', takes_context=True)
def gdz_menu(context):
    items = Category.objects.all()
    return {'items': items}