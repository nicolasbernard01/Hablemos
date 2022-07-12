from django.urls import path
from .views import *

urlpatterns = [

    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('editar_perfil/<>')
    path('debate/list', DebateList.as_view(), name="debate_list"),
    path('leer_debate/<debate_id>', leer_debate, name='leer_debate'),
    path('debate/', DebateCreate.as_view(), name="debate_create"),
    path('debate/editar/<pk>', DebateUpdate.as_view(), name="debate_update"),
    path('debate/eliminar/<pk>', DebateDelete.as_view(), name="debate_delete"),
 
]