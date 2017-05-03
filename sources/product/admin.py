from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'category', 'created_at', 'modified_at']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)