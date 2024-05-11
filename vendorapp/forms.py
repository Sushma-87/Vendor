from django import forms
from vendorapp.models import Vendor,PurchaseOrder,Performance


class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields = ['vendor_name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model=PurchaseOrder
        fields = "__all__"

class PerformanceForm(forms.ModelForm):
    class Meta:
        model=Performance
        fields = "__all__"