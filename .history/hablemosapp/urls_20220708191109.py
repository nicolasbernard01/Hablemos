from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio)    
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
  
]