from django.contrib import admin
from django.core.exceptions import ValidationError

from apps.models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        # 'slug', "number", 'image',
        'name', 'slug', 'url',
        # 'url', 'date', 'duration', 'times', 'event_date'
    )
    search_fields = ('data__size', 'data__color',)

    # list_filter = ('is_available',)
    # search_fields = ('name',)
