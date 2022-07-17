from django import forms
from .models import Avatar, Debate, Comentario, Mensaje
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
    
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    email = forms.EmailField(label='Email')
    password1: forms.Field(label='Contraseña', widget= forms.PasswordInput,required=False)
    password2: forms.Field(label='Repetir Contraseña', widget=forms.PasswordInput,required= False)

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_text = {k: '' for k in fields}


class AvatarForm(forms.Form):

    imagen = forms.ImageField(label='Imagen', required=False)

    class Meta:

        model = Avatar
        fields = ['imagen']


class CrearMensajeForm(forms.Form):

    receptor = forms.EmailField(label='para')
    mensaje = forms.CharField(label='mensaje', required=True, widget=forms.Textarea)

    class Meta:

        model = Mensaje
        fields = ['destinatario', 'mensaje']