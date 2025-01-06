from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('reg',views.reg, name='reg'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/<str:model_type>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('placeorder',views.placeorder, name='placeorder'),
    path('item',views.itempage, name='itempage'),
     path('confirmOrder/', views.confirmOrder , name='confirmOrder'),
    

    
]