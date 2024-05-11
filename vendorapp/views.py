from rest_framework.decorators import api_view
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from vendorapp.models import Vendor, PurchaseOrder,Performance
from vendorapp.serializer import VendorSerializers
from vendorapp.forms import VendorForm,PerformanceForm,PurchaseForm
from vendorapp.utils import update_average_response_time,timezone
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage

@csrf_exempt
def vendorapi(request,id=0):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        vendors_serializers = VendorSerializers(vendors,many = True)
        return JsonResponse(vendors_serializers.data,safe=False)
    elif request.method == 'POST':
        vendors = JSONParser().parse(request)
        vendor_serializer =VendorSerializers(data=vendors)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse("data added successfully",safe=False)
        return JsonResponse("not added")
    elif request.method == 'PUT':
        vendorid = JSONParser().parse(request)
        vendordata = Vendor.objects.get(id=vendorid['id'])
        vendorserializer = VendorSerializers(vendordata,data=vendorid)
        if vendorserializer.is_valid():
            vendorserializer.save()
            return JsonResponse("data updated successfully",safe=False)
        return JsonResponse("not upddates")
    elif request.method == 'DELETE':
        # trainsid = JSONParser().parse(request)
        vendordata = Vendor.objects.get(id=id)
        # if traindata:
        vendordata.delete()
        return JsonResponse("data deleted successfully",safe=False)
    return JsonResponse("not deleted")

@csrf_exempt
def SaveFile(request):
    file_data = request.FILES['file']
    file_name = default_storage.save(file_data.vendor_name,file_data)
    return JsonResponse(file_name,safe=False)

def purchaseapi(request,id=0):
    if request.method == 'GET':
        purchases = PurchaseOrder.objects.all()
        purchases_serializers = VendorSerializers(purchases,many = True)
        return JsonResponse(purchases_serializers.data,safe=False)
    elif request.method == 'POST':
        purchases = JSONParser().parse(request)
        purchase_serializer =VendorSerializers(data=purchases)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse("data added successfully",safe=False)
        return JsonResponse("not added")
    elif request.method == 'PUT':
        po_id = JSONParser().parse(request)
        purchasedata = Vendor.objects.get(id=po_id['id'])
        purchaseserializer = VendorSerializers(purchasedata,data=po_id)
        if purchaseserializer.is_valid():
            purchaseserializer.save()
            return JsonResponse("data updated successfully",safe=False)
        return JsonResponse("not upddates")
    elif request.method == 'DELETE':
        # trainsid = JSONParser().parse(request)
        purchasedata = PurchaseOrder.objects.get(id=id)
        # if traindata:
        purchasedata.delete()
        return JsonResponse("data deleted successfully",safe=False)
    return JsonResponse("not deleted")

@csrf_exempt
def SaveFile1(request):
    file_data = request.FILES['file']
    file_name = default_storage.save(file_data.vendor_name,file_data)
    return JsonResponse(file_name,safe=False)

def performanceapi(request,id=0):
    if request.method == 'GET':
        purchases = PurchaseOrder.objects.all()
        purchases_serializers = VendorSerializers(purchases,many = True)
        return JsonResponse(purchases_serializers.data,safe=False)
    else:
        return JsonResponse("data deleted successfully",safe=False)
    
def index(request):
    vendors = Vendor.objects.all()
    if request.method == 'POST':
        form = VendorForm(request.POST)
        form.is_valid()
        form.save()
        return redirect(index)
    form = VendorForm()
    return render(request, 'index.html', {'vendors': vendors,'form':form})

def po_details(request,pk):
    purchase_order = PurchaseOrder.objects.get(po_id=pk)
    if request.method == 'POST':
        form1 = PurchaseForm(request.POST,instance=purchase_order)
        form1.is_valid()
        form1.save()
        return redirect(index)
    form1 = PurchaseForm(instance=purchase_order)
    return render(request, 'po_detail.html', {'purchase_order': purchase_order,'form1':form1})

def performance(request, vendor_id):
    perform = Performance.objects.get(pk=vendor_id)
    return render(request, 'performance.html', {'perform': perform})