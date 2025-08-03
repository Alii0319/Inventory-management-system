from django.contrib import admin
from .models import Category,Product,Supplier,Customer,PurchaseOrder,PurchaseItem,SalesOrder,SalesItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'quantity', 'price', 'low_stock_alert']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_number', 'address']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'email']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'date']

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'purchase_order', 'product', 'quantity', 'unit_price']

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date']

@admin.register(SalesItem)
class SalesItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'sales_order', 'product', 'quantity', 'unit_price']
