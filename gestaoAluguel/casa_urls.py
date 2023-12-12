from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.casa_home, name="casa_home"),
    path('registrar_casa/', views.registrar_casa, name="registrar_casa"),
    path('atualizar_casa/<int:id>', views.atualizar_casa, name="atualizar_casa"),
    path('deletar_casa/<int:id>', views.deletar_casa, name="deletar_casa"),
    path('listar_casa/', views.listar_casa, name="listar_casa"),
    path('renda_mensal/', views.rendimento_estimado, name="renda_mensal"),
]
