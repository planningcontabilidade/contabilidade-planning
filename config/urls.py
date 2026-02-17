from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Sistema Contabilidade Online 🚀")

urlpatterns = [
    path('', home),
]
