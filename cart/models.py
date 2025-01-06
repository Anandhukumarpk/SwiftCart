from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings




# Create your models here.
class product(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class laptop(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

# CartItem Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    


# PlaceOrder Model
class PlaceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_items = models.ManyToManyField('CartItem', related_name='orders')  # Link to CartItem

    def cart_items_names(self):
        # Fetch the cart items for this order's user
        cart_items = CartItem.objects.filter(user=self.user)
        # Return the names of the products in the cart
        return ', '.join([item.product.name for item in cart_items])

    cart_items_names.short_description = "Cart Item Names"

    def __str__(self):
        return f"Order by {self.user.username} - {self.total_price}"


    




class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_item = models.ForeignKey('cart.CartItem', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.cart_item.id}"
    

class smartTv(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    price = models.IntegerField()