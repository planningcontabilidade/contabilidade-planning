from django.db import connection
from django.http import HttpResponse
import os


def executar_importacao(request):
    caminho = os.path.join(os.path.dirname(os.path.dirname(__file__)), "import_clientes.sql")

    with open(caminho, "r", encoding="utf-8") as f:
        sql_script = f.read()

    with connection.cursor() as cursor:
        cursor.executescript(sql_script)

    return HttpResponse("Importação executada com sucesso!")
