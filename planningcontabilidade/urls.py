from django.urls import path
from .views import home, executar_importacao, lista_clientes

urlpatterns = [
    path('', home, name='home'),
    path('executar-importacao/', executar_importacao, name='executar_importacao'),
    path('clientes/', lista_clientes, name='lista_clientes'),
]
