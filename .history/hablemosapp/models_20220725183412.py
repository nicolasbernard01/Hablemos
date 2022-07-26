from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Debate(models.Model):

    titulo = models.CharField('titulo', max_length=60)
    subtitulo = models.CharField('subtitulo', max_length=150)
    cuerpo = models.TextField('cuerpo')
    imagen = models.ImageField('imagen',upload_to = 'PostImagen/',blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comentario(models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comentario_autor', null=True)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, null=True)
    comentario = models.TextField('comentario')
    creado = models.TimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comentario_likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='comentario_dislike')

    def __str__(self):
        
        return self.comentario


class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatar/', blank=True, null=True)


class Mensaje(models.Model):

    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    mensaje = models.TextField(max_length=150, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now=True)
    leido = models.BooleanField(default=False)
    

    def __str__(self):
        
        return self.mensaje


class About_us(models.Model):

    creador = models.CharField(max_length=200)
    