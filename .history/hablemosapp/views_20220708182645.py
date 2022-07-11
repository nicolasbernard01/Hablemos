from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *

def inicio

def register_request(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                login(request,user)
                return redirect('base')

            else:

                return redirect('register')

        return render(request,'hablemosapp/register.html',{'form':form})

    form = UserRegisterForm()

    return render(request, 'hablemosapp/register.html', {'form': form})

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:

                login(request, user)
                return redirect('base')

            else: 

                return redirect('login')

        else:

            return redirect('login')
        
    form = AuthenticationForm()

    return render(request, r'hablemosapp/login.html', {'form': form})

def logout_request(request):

    logout(request)

    return redirect('register_login')

