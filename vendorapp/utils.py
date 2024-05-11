from vendorapp.models import PurchaseOrder, Vendor
from django.db.models import Count, Avg
from django.db.models.functions import Coalesce
from django.db import models
from datetime import timedelta
from django.utils import timezone

def update_average_response_time(vendor):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    total_acknowledged_pos = acknowledged_pos.count()
    if total_acknowledged_pos > 0:
        total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
        avg_response_time = total_response_time / total_acknowledged_pos
        vendor.average_response_time = avg_response_time
        vendor.save()


def update_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_completed_pos = completed_pos.count()
    if total_completed_pos > 0:
        on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date')).count()
        on_time_delivery_rate = on_time_deliveries / total_completed_pos
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()

def update_quality_rating_average(vendor):
    completed_pos_with_rating = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    total_completed_pos_with_rating = completed_pos_with_rating.count()
    if total_completed_pos_with_rating > 0:
        quality_rating_avg = completed_pos_with_rating.aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        vendor.quality_rating_avg = quality_rating_avg
        vendor.save()

def update_average_response_time(vendor):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    total_acknowledged_pos = acknowledged_pos.count()
    if total_acknowledged_pos > 0:
        avg_response_time = acknowledged_pos.aggregate(avg_time=Avg(Coalesce(models.F('acknowledgment_date') - models.F('issue_date'), timedelta())))['avg_time']
        vendor.average_response_time = avg_response_time.total_seconds() / 3600  # in hours
        vendor.save()

def update_fulfillment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
    if total_pos > 0:
        fulfilled_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        fulfillment_rate = fulfilled_pos / total_pos
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()
