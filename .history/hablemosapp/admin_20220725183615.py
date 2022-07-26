import site
from django.contrib import admin
from .models import Avatar, Debate, Comentario, Mensaje

#debate

class DebateAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'subtitulo', 'cuerpo', 'imagen','autor')
    search_fields = ('titulo', 'subtitulo','autor')

admin.site.register(Debate, DebateAdmin)

#comentario

class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('comentario', 'creado')
    
admin.site.register(Comentario, ComentarioAdmin)

#avatar

admin.site.register(Avatar)

#mensajes

admin.site.register(Mensaje)

admin