from rest_framework import serializers
from .models import Category,Product,Supplier,Customer,PurchaseOrder,PurchaseItem,SalesOrder,SalesItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields='__all__'

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseItem
        fields='__all__'

class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesOrder
        fields='__all__'

class SalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=SalesItem
        fields='__all__'