from django.urls import path
from .views import home, executar_importacao

urlpatterns = [
    path('', home),
    path('executar-importacao/', executar_importacao),
]
