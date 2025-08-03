from rest_framework import viewsets,status
from .models import Category, Product, Supplier, Customer,PurchaseOrder, PurchaseItem, SalesOrder, SalesItem
from .serializers import CategorySerializer, ProductSerializer, SupplierSerializer, CustomerSerializer,PurchaseOrderSerializer, PurchaseItemSerializer, SalesOrderSerializer, SalesItemSerializer
from django.db.models import F,Sum
from rest_framework.response import Response
from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from datetime import datetime,timedelta
from django.shortcuts import render
from django.utils import timezone

#       Create views here



def sales_report_view(request):
    return render(request,'inventory/sales_report.html')

class SalesReportView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        sales_items = SalesItem.objects.all()

        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            start_date = timezone.make_aware(start_date)  # Fix warning
            sales_items = sales_items.filter(created_at__gte=start_date)

        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
            end_date = timezone.make_aware(end_date)  # Fix warning
            sales_items = sales_items.filter(created_at__lt=end_date)

        # Aggregate total quantity and total revenue
        total_quantity = sales_items.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0
        total_revenue = sales_items.aggregate(
            total_rev=Sum(F('quantity') * F('unit_price'))
        )['total_rev'] or 0

        # Group by product
        product_sales = sales_items.values(
            product_name=F('product__name')
        ).annotate(
            quantity_sold=Sum('quantity'),
            total_earned=Sum(F('quantity') * F('unit_price'))
        )

        return Response({
            'total_quantity': total_quantity,
            'total_revenue': total_revenue,
            'product_sales': list(product_sales)
        }, status=status.HTTP_200_OK)
    

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PurchaseOrderView(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseItemView(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance=self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
        return Response(self.get_serializer(instance).data,status=status.HTTP_201_CREATED,headers=headers)

    def perform_create(self, serializer):
        product=serializer.validated_data['product']
        quantity=serializer.validated_data['quantity']

        with transaction.atomic():
            instance=serializer.save()
            Product.objects.filter(pk=product.pk).update(quantity=F('quantity')+quantity)
        
        return instance


class SalesOrderView(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

class SalesItemView(viewsets.ModelViewSet):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance=self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)

        return Response(self.get_serializer(instance).data,status=status.HTTP_201_CREATED,headers=headers)
    
    def perform_create(self, serializer):
        product=serializer.validated_data['product']
        quantity=serializer.validated_data['quantity']

        with transaction.atomic():
            product_obj=Product.objects.select_for_update().get(pk=product.pk)
            if product_obj.quantity < quantity:
                raise ValidationError('Not enough quantity in store')
            instance=serializer.save()
            Product.objects.filter(pk=product.pk).update(quantity=F('quantity')-quantity)
        return instance