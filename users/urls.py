from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('registrar_usuario/', views.register,
         name="registrar_usuario"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
