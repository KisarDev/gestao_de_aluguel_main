from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestaoAluguel.urls')),
    path('casa/', include('gestaoAluguel.casa_urls')),
    path('inquilino/', include('gestaoAluguel.inquilino_urls')),
    path('user/', include('users.urls')),
    path('despesas/', include('despesas.urls')),
]
