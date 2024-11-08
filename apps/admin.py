from django.contrib import admin
from django.core.exceptions import ValidationError

from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        # 'slug', "number", 'image',
        'name', 'slug', 'url','times'
        # 'url', 'date', 'duration', 'times', 'event_date'
    )
    search_fields = ('data__size', 'data__color',)

    # list_filter = ('is_available',)
    # search_fields = ('name',)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid')