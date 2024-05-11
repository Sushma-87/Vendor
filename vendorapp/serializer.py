from rest_framework import serializers
from vendorapp.models import Vendor,PurchaseOrder,Performance

class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','vendor_name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class PurchaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledment_date']

class PerformaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id','vendor','date','on_time_delivery_rate ',' quality_rating_avg','average_response_time','fulfillment_rate']