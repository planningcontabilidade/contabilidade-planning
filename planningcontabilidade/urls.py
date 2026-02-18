from django.urls import path
from planningcontabilidade.views import home, executar_importacao

urlpatterns = [
    path('', home),
    path('executar-importacao/', executar_importacao),
]
