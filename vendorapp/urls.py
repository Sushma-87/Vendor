from django.urls import path
from vendorapp import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('vendor/<int:vendor_id>/', views.vendor_details, name='vendor_details'),
    # path('vendor/<int:vendor_id>/', views.vendor_performance, name='vendor_details'),
    path('po/<int:pk>',views.po_details,name='po'),
    path('<int:vendor_id>',views.performance,name='performance'),
    path('<int:id>',views.vendorapi),
    path('savefile',views.SaveFile),
    path('<int:id>',views.purchaseapi),
    path('<int:id>',views.performanceapi),
    path('savefile',views.SaveFile1),
    # path('<int:vendor_id>',views.vendor_performance,name='vendor_performance')

]
