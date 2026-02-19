from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
import os

from .models import Cliente


# ==============================
# Dashboard Executivo
# ==============================
def home(request):
    total_clientes = Cliente.objects.count()

    clientes_por_uf = (
        Cliente.objects
        .values("uf")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    top_ufs = clientes_por_uf[:5]

    context = {
        "total_clientes": total_clientes,
        "top_ufs": top_ufs,
    }

    return render(request, "index.html", context)


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

                        <a href="/" class="btn btn-secondary mt-3">Voltar para Dashboard</a>
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
    busca = request.GET.get("q")

    clientes = Cliente.objects.all().order_by("id")

    if busca:
        clientes = clientes.filter(nome__icontains=busca)

    return render(request, "lista_clientes.html", {
        "clientes": clientes,
        "busca": busca
    })
