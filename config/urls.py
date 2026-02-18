from django.contrib import admin
from django.urls import path
from planningcontabilidade.views import executar_importacao, executar_migrate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('executar-migrate/', executar_migrate),
    path('executar-importacao/', executar_importacao),
]
