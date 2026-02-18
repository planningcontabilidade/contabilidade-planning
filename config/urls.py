from django.contrib import admin
from django.urls import path
from planningcontabilidade.views import (
    executar_importacao,
    executar_migrate,
    ajustar_nome_nullable,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('executar-migrate/', executar_migrate),
    path('ajustar-nome-null/', ajustar_nome_nullable),
    path('executar-importacao/', executar_importacao),
]
