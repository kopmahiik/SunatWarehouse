from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'is_deleted')
    list_display_links = ('id', 'name')
