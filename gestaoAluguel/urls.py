from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('spider/', views.spider, name="spider"),
]
