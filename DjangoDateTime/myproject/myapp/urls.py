from django.urls import path
from .views import show_time, name_form

urlpatterns = [
     path('', show_time), 
     path('time/', show_time),
     path('name/', name_form),
]
