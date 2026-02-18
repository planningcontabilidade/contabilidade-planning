from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import render
import os

from .models import Cliente


# ==============================
# Página Inicial
# ==============================
def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Araújo Gonçalves Contadores Associados</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">

        <div class="container text-center mt-5">
            <div class="card shadow p-5">
                <h1 class="mb-3">Araújo Gonçalves Contadores Associados</h1>
                <p class="mb-4">Sistema de Gestão de Clientes</p>

                <a href="/executar-importacao/" class="btn btn-primary m-2">
                    Importar Clientes
                </a>

                <a href="/clientes/" class="btn btn-dark m-2">
                    Ver Clientes
                </a>
            </div>
        </div>

        </body>
        </html>
    """)


# ==============================
# Importação Segura
# ==============================
def executar_importacao(request):
    try:
        caminho = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "import_clientes.sql"
        )

        if not os.path.exists(caminho):
            return HttpResponse("Arquivo import_clientes.sql não encontrado.")

        with open(caminho, "r", encoding="utf-8") as f:
            sql_script = f.read()

        comandos = sql_script.split(";")

        inseridos = 0
        ignorados = 0

        with transaction.atomic():
            with connection.cursor() as cursor:
                for comando in comandos:
                    comando = comando.strip()

                    if comando.upper().startswith("INSERT"):
                        try:
                            cursor.execute(comando)
                            inseridos += 1
                        except Exception:
                            ignorados += 1

        return HttpResponse(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Importação Finalizada</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body class="bg-light">
                <div class="container mt-5 text-center">
                    <div class="card shadow p-4">
                        <h2 class="mb-3">Importação Finalizada</h2>
                        <p class="text-success">✔ Inseridos: {inseridos}</p>
                        <p class="text-warning">⚠ Ignorados: {ignorados}</p>

                        <a href="/" class="btn btn-secondary mt-3">Voltar para Home</a>
                    </div>
                </div>
            </body>
            </html>
        """)

    except Exception as e:
        return HttpResponse(f"Erro ao executar importação: {str(e)}")


# ==============================
# Lista de Clientes
# ==============================
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by("id")

    return render(request, "lista_clientes.html", {
        "clientes": clientes
    })
