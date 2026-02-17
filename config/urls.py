from django.contrib import admin
from django.urls import path
from planningcontabilidade.views import executar_importacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('executar-importacao/', executar_importacao),
]
