from django.urls import path
from .views.pessoa_views import *


urlpatterns = [
    path('listar_pessoa', listar_pessoas, name='listar_pessoas'),
    path('cadastrar_pessoa', cadastrar_pessoa, name='cadastrar_pessoa'),
    path('listar_pessoa', cadastrar_pessoa, name='cadastrar_pessoa'),
    path('listar_pessoa/<int:id>', listar_pessoa_id, name='listar_pessoa_id'),
    path('editar_pessoa/<int:id_pessoa>', editar_pessoa, name='editar_pessoa'),
    path('home', home, name='home'),
    path('index', home, name='home'),
]