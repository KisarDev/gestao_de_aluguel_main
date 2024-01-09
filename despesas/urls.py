from django.urls import path, include

from despesas import views

urlpatterns = [
    path('registrar_despesas/', views.registrar_despesas,
         name='registrar_despesas'),
    path('listar_despesas/', views.listar_despesas,
         name='listar_despesas'),
    path('adicionar_casa/', views.adicionar_casa,
         name='adicionar_casa'),
]
