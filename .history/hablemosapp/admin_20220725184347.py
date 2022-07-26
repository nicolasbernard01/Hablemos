from atexit import register
import site
from django.contrib import admin
from .models import AboutUs, Avatar, Debate, Comentario, Mensaje

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

#aboutus

class AboutusAdmin(admin.ModelAdmin):

    list_dispplay = ('marca', 'creador', 'descripcion')

    class Meta:

        

admin.site.register(AboutUs, AboutusAdmin)