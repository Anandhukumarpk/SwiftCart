from django.contrib import admin
from .models import product, laptop , CartItem , PlaceOrder ,UserInfo , smartTv
from django.utils.html import format_html
from django.urls import reverse


class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',  'cart_items_names')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'object_id', 'quantity', 'price', 'view_on_site')

    def view_on_site(self, obj):
        url = reverse('order_item_detail', args=[obj.id])
        return format_html('<a href="{}">View</a>', url)


# Register your models here.
admin.site.register(product)
admin.site.register(laptop)
admin.site.register(CartItem)
admin.site.register(PlaceOrder, PlaceOrderAdmin)

admin.site.register(smartTv)
admin.site.register(UserInfo)










