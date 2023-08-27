from django.urls import path
from App_Shop import views

app_name="App_Shop"

urlpatterns=[
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('shipping',views.shipping,name='shipping'),
    path('shipping-process',views.shipping_process,name='shipping_process'),
    
    
]