from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.casa_home),
  path('registrar_casa/',views.registrar_casa),
  path('listar_casa/',views.listar_casa),
]