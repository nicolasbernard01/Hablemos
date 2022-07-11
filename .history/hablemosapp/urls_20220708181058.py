from django.urls import path
from .views import *



print(' asdasdasda'),


urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
]