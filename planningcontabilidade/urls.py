from planningcontabilidade.views import executar_importacao

urlpatterns = [
    # suas rotas...
    path('executar-importacao/', executar_importacao),
]
