from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router Object
router = DefaultRouter()

# Register all ViewSets 
router.register('category', views.CategoryView, basename='category')
router.register('product', views.ProductView, basename='product')
router.register('supplier', views.SupplierView, basename='supplier')
router.register('customer', views.CustomerView, basename='customer')
router.register('purchase-order', views.PurchaseOrderView, basename='purchase-order')
router.register('purchase-item', views.PurchaseItemView, basename='purchase-item')
router.register('sales-order', views.SalesOrderView, basename='sales-order')
router.register('sales-item', views.SalesItemView, basename='sales-item')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('sales_report/', views.sales_report_view, name='sales_report'),
    path('auth/',include('rest_framework.urls')),
    path('api/sales-report/', views.SalesReportView.as_view(), name='sales-report'),
]
