from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('registrar_casa/',views.registrar_casa)
]