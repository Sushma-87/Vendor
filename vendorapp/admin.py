from django.contrib import admin
from .models import Vendor, PurchaseOrder,Performance

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ('name', 'vendor_code')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('po_number', 'vendor__name')
    date_hierarchy = 'order_date'

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    list_filter = ('date',)
    search_fields = ('vendor__name',)
    date_hierarchy = 'date'
