from django.urls import path
from .views import *

urlpatterns = [

    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('debate/list', DebateList.as_view(), name="debate_list"),
    path('logout/', logout_request, name='logout'),
    #path('debate/<pk>', DebateDetail.as_view(), name="debate_detail"), #cambiar a debate_id el pk
    path('debate/', DebateCreate.as_view(), name="debate_create"),
    path('debate/editar/<pk>', DebateUpdate.as_view(), name="debate_update"),
    path('debate/eliminar/<pk>', DebateDelete.as_view(), name="debate_delete"),
 
]