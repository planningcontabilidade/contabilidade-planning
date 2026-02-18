from django.contrib import admin
from django.urls import path
from planningcontabilidade.views import home, executar_importacao

urlpatterns = [
    path('', home),  # Página inicial
    path('executar-importacao/', executar_importacao),
    path('admin/', admin.site.urls),
]
