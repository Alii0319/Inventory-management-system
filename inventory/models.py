from django.db import models

# Create your models here.

#   Category model
class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.name
    
#   Product model
class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_alert = models.PositiveIntegerField(default=10)  # e.g., alert if quantity < 10

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



#   Supplier model
class Supplier(models.Model):
    name=models.CharField(max_length=30)
    contact_number=models.CharField(max_length=11)
    address=models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

#   Customer model
class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name


#   PurchaseOrder model
class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Purchase #{self.id} - {self.supplier.name}"

#   PurchaseItem model
class PurchaseItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

#   SalesOrder model
class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Sale #{self.id} - {self.customer.name}"

#    SalesItem model
class SalesItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
