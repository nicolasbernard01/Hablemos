from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.views.generic.edit import UpdateView, DeleteView
from .models import Comentario, Debate, Avatar, User, Mensaje
from .forms import AvatarForm, ComentarioForm, CrearMensajeForm, UserEditForm, UserRegisterForm, DebateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):

    debates = Debate.objects.all()

    ctx = {'debates':debates}

    return render(request, r'hablemosapp/debates.html', ctx)

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

                return redirect('debates')

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

                return redirect('debates')

        else:
            
            messages.error(request,r'Ups! error al iniciar sesion, verifica los datos')

            return redirect('login')
        
    form = AuthenticationForm()

    return render(request, r'hablemosapp/login.html', {'form': form})

@login_required
def logout_request(request):

    logout(request)

    return redirect('debates')

def debates(request):

    user = request.user

    debates = Debate.objects.all()

    if user.is_authenticated:

        mensajes = Mensaje.objects.filter(receptor=user)

        if request.method == 'POST':
        
            search = request.POST['search']

            if search != '':

                    debates = Debate.objects.filter(titulo__icontains = search)

                    ctx = {'debates':debates,'mensajes': mensajes}

                    messages.success(request, r'Resultados de su busqueda')

                    return render(request, r'hablemosapp/debates.html', ctx)

            else:

                return redirect('debates')

        else:

            debates = Debate.objects.all()

            return render(request, r'hablemosapp/debates.html', {'debates':debates, 'mensajes': mensajes})
            
    else:

        debates = Debate.objects.all()

        return render(request, r'hablemosapp/debates.html', {'debates':debates})
                   
def leer_debate(request, debate_id):

    debate = Debate.objects.get(id=debate_id)

    comentarios = Comentario.objects.filter(debate = debate_id)

    if request.method == 'POST':

        form = ComentarioForm(request.POST)
        

        if form.is_valid():

            info = form.cleaned_data

            nuevo_comentario = Comentario(comentario = info['comentario'], autor=request.user, debate=debate)

            nuevo_comentario.save()

            return redirect('debates')

        else:

            return render(request, r'hablemosapp/leer_debate.html', ctx)

    else:

        form = ComentarioForm()

        ctx = {'debate':debate, 'comentarios':comentarios, 'form': form}

        return render(request, r'hablemosapp/leer_debate.html', ctx)

@login_required
def crear_debate(request):

    if request.method == 'POST':

        form = DebateForm(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data

            nuevo_post = Debate(titulo=info['titulo'], subtitulo=info['subtitulo'],cuerpo=info['cuerpo'], imagen=info['imagen'], autor=request.user)

            nuevo_post.save()

            return redirect('debates')

        return render(request, r'hablemosapp/crear_debate.html', {'form': form})

    form = DebateForm()

    return render(request, r'hablemosapp/crear_debate.html', {'form': form})

class DebateUpdate(LoginRequiredMixin, UpdateView):

    model = Debate

    success_url = '/debates/'

    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]

class DebateDelete(LoginRequiredMixin, DeleteView):

    model = Debate

    success_url = '/debates/'

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.email = info['email']

            user.save()

            messages.success(request, r"Perfil actualizado con exito.")

            return redirect('editar_perfil')

        else:

            messages.error(request, r"Error al actualizar su perfil, verifique las contraseñas.")

            form = UserEditForm(initial = {'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email})

            return redirect('editar_perfil')

    else:

        form = UserEditForm(initial = {'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email})   

        return render(request, r'hablemosapp/editar_perfil.html', {'form':form})

@login_required
def user_avatar(request):

    if request.method == 'POST':

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username)

            avatar = Avatar(usuario=user, imagen = form.cleaned_data['imagen'])

            avatar.save()

            return redirect('debates')

    else:

        form = AvatarForm()

    return render(request,r'hablemosapp/user_avatar.html', {'form':form})

@login_required
def enviar_mensaje(request):

    if request.method == 'POST':

        form = CrearMensajeForm(request.POST)
        
        try:

            if form.is_valid():

                info = form.cleaned_data

                nuevo_mensaje = Mensaje(emisor=request.user,receptor=User.objects.get(email=info["receptor"]), mensaje = info["mensaje"])

                nuevo_mensaje.save()

                messages.success(request, r'Mensaje Enviado')

                return redirect('enviar_mensaje')

            else: 

                messages.error(request,r'Ups! algo ha salido mal')

                return redirect('enviar_mensaje')

        except:

            messages.error(request,r'Parece que ese usuario no existe')

            return redirect('enviar_mensaje')

    else:

        form = CrearMensajeForm()

        return render(request, 'hablemosapp/enviar_mensaje.html', {'form':form})

@login_required
def leer_mensajes(request):

    user = request.user

    mensajes = Mensaje.objects.filter(receptor = user)

    ctx = {'mensajes': mensajes}

    return render(request, r'hablemosapp/leer_mensajes.html', ctx)

