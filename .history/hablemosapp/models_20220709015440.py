from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Debate(models.Model):

    titulo = models.CharField('titulo', max_length=30)
    subtitulo = models.CharField('subtitulo', max_length=150)
    cuerpo = models.TextField('cuerpo')
    imagen = models.ImageField('imagen', blank = True)
    creado = models.TimeField(default=datetime.date)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')


class Comentario(models.Model):

    comentario = models.TextField('comentario')
    creado = models.TimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comentario_likes')
    dislike = models.ManyToManyField(User, blank=True, related_name='comentario_dislike')



