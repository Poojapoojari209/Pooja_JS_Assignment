from django.urls import path
from .views import show_time

urlpatterns = [
     path('', show_time), 
     path('time/', show_time),
]
