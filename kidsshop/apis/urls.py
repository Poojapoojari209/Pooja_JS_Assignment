from django.urls import path
from .views import *

urlpatterns = [
    path('', get_information, name='get_infomation'),
     path('products/', products, name='products')
]