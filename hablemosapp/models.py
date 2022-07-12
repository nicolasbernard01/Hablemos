from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Debate(models.Model):

    titulo = models.CharField('titulo', max_length=60)
    subtitulo = models.CharField('subtitulo', max_length=150)
    cuerpo = models.TextField('cuerpo')
    imagen = models.ImageField('imagen', blank = True)
    creado = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comentario(models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, null=True)
    comentario = models.TextField('comentario')
    creado = models.TimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comentario_likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='comentario_dislike')


class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatar/', blank=True, null=True)

    


