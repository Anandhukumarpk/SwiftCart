from django.shortcuts import render , redirect , get_object_or_404
from .models import  Order, OrderItem ,Contactus
from django.contrib.contenttypes.models import ContentType

from cart.models import CartItem 
from .forms import ContactForm










def orderplace(request):

    cart_items = CartItem.objects.filter(user=request.user)
    

    new_order = Order.objects.create(user=request.user)


    for cart_item in cart_items:
        OrderItem.objects.create(
            order=new_order,
            content_type=cart_item.content_type,
            object_id=cart_item.object_id,
            quantity=cart_item.quantity,
            price=cart_item.product.price  
        )
    

    total = sum(item.total_price for item in new_order.items.all())
    new_order.total_price = total
    new_order.save()

   
    return redirect( 'placeorder')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('contact')  
    else:
        form = ContactForm() 
   
    return render (request, 'contactus.html', {'form': form})

def orderpage(request):

    
    
    return render (request , 'orders.html' )
    
 


    




def cart(request):

     if not request.user.is_authenticated:
        return redirect('login')
     
    
     cart_items = CartItem.objects.filter(user=request.user)
     cart_total = sum(item.total_price for item in cart_items)


     return render(request , 'Cart.html' , {
         'cart_items': cart_items,
        'cart_total': cart_total,
     })


def faq(request):
    return render(request, 'faq.html')

