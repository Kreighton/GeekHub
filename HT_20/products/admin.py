from django.contrib import admin

from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'product_price', 'status')
    list_filter = ('product_category',)
    search_fields = ('product_name',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory, ProductCategoryAdmin)

