from django.urls import path
from .views import simple_form

urlpatterns = [
    path('form/', simple_form),
]
