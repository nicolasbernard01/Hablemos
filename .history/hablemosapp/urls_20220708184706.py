from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('debate/list', DebateList.as_view(), name="debate_list"),
    path('debate/<pk>', DebateDetail.as_view(), name="debate_detail"),
    path('profesor/nuevo', ProfeCreate.as_view(), name="profe_create"),
    path('profesores/editar/<pk>', ProfeUpdate.as_view(), name="profe_update"),
    path('profesores/eliminar/<pk>', ProfeDelete.as_view(), name="profe_delete"),
]