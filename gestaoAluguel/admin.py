from django.contrib import admin
from gestaoAluguel.models import Casa, Inquilino, MesRendimento
# Register your models here.

admin.site.register(Casa),
admin.site.register(Inquilino)
admin.site.register(MesRendimento)