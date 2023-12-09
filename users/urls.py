from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('registrar_usuario/', views.registrar_usuario, name="registrar_usuario")


]
