from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    name = models.CharField(max_length=100)
    
    
    number = models.CharField(max_length=15)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
    ]

    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return f"Order {self.id} by {self.user.username}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Save the price at the time of order


    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"OrderItem {self.id} for Order {self.order.id}"
    

    def __str__(self):
        product_name = self.product.name if hasattr(self.product, 'name') else 'Unknown Product'
        return f"OrderItem {self.id} for Order {self.order.id}: {product_name} (x{self.quantity})"
    







    

class Contactus(models.Model):  # Use PascalCase for class names
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Message = models.TextField(blank=True)

    def __str__(self):
        return self.Name