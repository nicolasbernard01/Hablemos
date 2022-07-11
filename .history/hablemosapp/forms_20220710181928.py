from logging import PlaceHolder
from django import forms
from .models import Debate, Comentario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label='Email')
    password1: forms.Field(label='Contraseña', widget= forms.PasswordInput)
    password2: forms.Field(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k: '' for k in fields}



class UserEditForm(UserCreationForm):
    
    nombre = forms.CharField(label='Nombre', max_length=30, required=False)
    apellido = forms.CharField(label='Apellido', max_length=30, required=False)
    email = forms.EmailField(label='Email')
    password1: forms.Field(label='Contraseña', widget= forms.PasswordInput,required=False)
    password2: forms.Field(label='Repetir Contraseña', widget=forms.PasswordInput,required= False)

    class Meta:

        model = User
        fields = ['Nombre']
