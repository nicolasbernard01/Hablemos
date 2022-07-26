from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar_avatar/', editar_avatar, name='editar_avatar'),
    path('user_avatar/', user_avatar, name='user_avatar'),
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('leer_mensajes/', leer_mensajes, name='leer_mensajes'),
    path('debates/', debates, name="debates"),
    path('debates/', debates, name="debates"),
    path('crear_debate/', crear_debate, name="crear_debate"),
    path('leer_debate/<debate_id>', leer_debate, name='leer_debate'),
    path('debate/editar/<pk>', DebateUpdate.as_view(), name="debate_update"),
    path('debate/eliminar/<pk>', DebateDelete.as_view(), name="debate_delete"),    
    
]