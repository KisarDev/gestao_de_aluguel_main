from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('registrar_inquilinos/', views.registrar_inquilino,
         name="registrar_inquilinos"),
    path('listar_inquilinos/', views.listar_inquilinos,
         name="listar_inquilinos"),
    path('atualizar_inquilino/<int:id>', views.atualizar_inquilino,
         name="atualizar_inquilino"),
    path('deletar_inquilino/<int:id>', views.deletar_inquilino,
         name="deletar_inquilino"),
]
