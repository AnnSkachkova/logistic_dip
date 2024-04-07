from django.contrib import admin
from .models import Delivery, DeliveryProduct


class DeliveryProductInline(admin.TabularInline):
    model = DeliveryProduct
    extra = 1
    

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'status', 'expected_arrival', 'actual_arrival']
    list_filter = ['status', 'supplier']
    search_fields = ['supplier__name', 'status']
    inlines = [DeliveryProductInline]