from django.urls import path
from products.views import *
from orders.views import *


app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),

   ]
