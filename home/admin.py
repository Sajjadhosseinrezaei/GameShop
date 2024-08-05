from django.contrib import admin
from .models import Product, Category

# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ['category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
