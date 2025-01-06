from django.shortcuts import render,redirect , get_object_or_404 
from .models import product,laptop , CartItem , PlaceOrder  , smartTv ,UserInfo
from django.contrib.auth.models import User,auth
from django. contrib import messages
from django.contrib.contenttypes.models import ContentType
from .forms import PlaceOrderForm






# Create your views here.

def home(request):
    items = product.objects.all()
    lap = laptop.objects.all()
    smarttv = smartTv.objects.all()

    return render(request, 'home.html',{ 'stock':items, 'lap' : lap, 'samartTv' : smarttv  })




def login(request):
    if request.method == 'POST':
        usrname = request.POST['usrname']
        password = request.POST['password']
        user = auth.authenticate(username = usrname , password = password )
        if user is not None:
            auth.login (request, user)
            return redirect('/')
        else :
            messages.info(request, ' Invalid username & password')
            return redirect('login')
    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        fname = request.POST['name']
        usrname = request.POST['usrname']
        email = request.POST['email']
        pswrd = request.POST['password']
        cnfrmpswd = request.POST['confirmpassowrd']
        if pswrd != cnfrmpswd:
            messages.info(request, 'Passwords are not matching')
            return redirect('reg')
        elif User.objects.filter(username = usrname).exists():
            messages.info(request,'User name already exists')
            return redirect('reg')
        elif User.objects.filter(email = email).exists():
            messages.info(request, ' email already exists')
            return redirect('reg')
        else :
            user = User.objects.create_user(first_name = fname, username = usrname, email = email, password=cnfrmpswd )
            user.save();
     
            return redirect('/')
    
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def cart(request):

     if not request.user.is_authenticated:
        return redirect('login')
     
    
     cart_items = CartItem.objects.filter(user=request.user)
     cart_total = sum(item.total_price for item in cart_items)


     return render(request , 'Cart.html' , {
         'cart_items': cart_items,
        'cart_total': cart_total,
     })




def add_to_cart(request, item_id, model_type):
    if model_type == 'product':
        item = get_object_or_404(product, id=item_id)
        content_type = ContentType.objects.get_for_model(product)
    elif model_type == 'laptop':
        item = get_object_or_404(laptop, id=item_id)
        content_type = ContentType.objects.get_for_model(laptop)
    elif model_type == 'smartTv':
        item = get_object_or_404(smartTv, id=item_id)
        content_type = ContentType.objects.get_for_model(smartTv) 
    
    

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=item.id
    )
   


    if not created:
        cart_item.quantity += 1
        cart_item.save()
   



    
        
    return redirect('cart')


def orderpage(request):
    
    return render (request , 'orders.html' )



def update_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

        if request.POST.get('action') == 'increase':
            cart_item.quantity += 1
        elif request.POST.get('action') == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        
        cart_item.save()
    
    return redirect('cart')


def remove_from_cart(request, item_id):
    if request.method == 'POST':
       
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
       
        cart_item.delete()
    
    return redirect('cart')



def placeorder(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.total_price for item in cart_items)
    if request.method == 'POST':
      
        name = request.POST.get('name')
        address = request.POST.get('address')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        country = request.POST.get('country')
        contact = request.POST.get('contact')
        cart_total = request.session.get('cart_total', 0)  

        if not all([name, address, district, pincode, country, contact]):
            messages.error(request, "All fields are required.")
            return render(request, 'PlaceOrder.html', {
                'cart_items': cart_items,
                'cart_total': cart_total,
            })

        
        PlaceOrder.objects.create(
            user=request.user, 
            name=name,
            address=address,
            district=district,
            pincode=pincode,
            country=country,
            contact=contact,
            total_price=cart_total  
        )

        return redirect('confirmOrder')

    return render(request, 'PlaceOrder.html', {
        
         'cart_items': cart_items,
        'cart_total': cart_total,
     }
    )


def confirmOrder(request,):
    
    cart_items = CartItem.objects.filter(user=request.user)
    
    cart_total = sum(item.total_price * 100 for item in cart_items)

    if request.method == 'POST':
        

        client = razorpay.Client(auth=('#', '#'))
        payment = client.order.create({
            'amount': '50000', 
            'currency': 'INR',
            'payment_capture': '1'
        })

       
    return render (request , 'completeOrder.html' ,{ 'cart_items': cart_items,
        'cart_total': cart_total} )
    


def itempage(request,):
   
    return render (request,'itempage.html' )







    
    

  
    
    

    































    # if request.method == 'POST':
    #     form = PlaceOrderForm(request.POST)
    #     if form.is_valid():
    #         # Create a new order and save it
    #         order = PlaceOrderForm()  # Replace 'Order' with the name of your order model
    #         order.user = request.user  # Link the order to the current user
    #         order.name = form.cleaned_data['name']  # Assuming your form has this field
    #         order.address = form.cleaned_data['address']
    #         order.district = form.cleaned_data['district']
    #         order.pincode = form.cleaned_data['pincode']
    #         order.country = form.cleaned_data['country']
    #         order.contact = form.cleaned_data['contact']
    #         order.total_price = sum(item.total_price for item in CartItem.objects.filter(user=request.user))  # Calculate total price

    #         order.save()  # Save the order to get the ID

    #         # Get the cart items and associate them with the order
    #         cart_items = CartItem.objects.filter(user=request.user)
    #         for item in cart_items:
    #             order.items.add(item)  # Assuming you have a ManyToMany relationship in your Order model
    #             item.delete()  # Optionally, remove the item from the cart after ordering

    #         # Redirect to a success page
    #         return redirect('order_success')  # Update with your success page URL
    # else:
    #     form = PlaceOrderForm()

    # cart_total = sum(item.total_price for item in CartItem.objects.filter(user=request.user))  # Example of getting cart total
    # return render(request, 'PlaceOrder.html', {'form': form, 'cart_total': cart_total})
    
    
    
   


    # if not request.user.is_authenticated:
    #     return redirect('login')
     
    
    # cart_items = CartItem.objects.filter(user=request.user)
    # cart_total = sum(item.total_price for item in cart_items)
    # return render(request, 'placeOrder.html',{
         
    #      'cart_items': cart_items,
    #     'cart_total': cart_total,
    #  })
    

