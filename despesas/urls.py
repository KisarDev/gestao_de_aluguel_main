from django.urls import path, include

from despesas import views

urlpatterns = [
    path('registrar_despesas/', views.registrar_despesas,
         name='registrar_despesas'),
]
