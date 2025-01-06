from django.contrib import admin
from . models import Order,OrderItem, Contactus


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'Order', 'product_name', 'quantity', 'price')  # Display these fields
    

# Register your models here.



admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(Contactus)


