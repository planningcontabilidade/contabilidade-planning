from django.db import connection, transaction
from django.shortcuts import render, redirect
from django.contrib import messages
import os

from .models import Cliente


# ==============================
# Página Inicial (HOME)
# ==============================
def home(request):
    return render(request, "index.html")


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
            messages.error(request, "Arquivo import_clientes.sql não encontrado.")
            return redirect("home")

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

        messages.success(request, f"✔ Inseridos: {inseridos}")
        messages.warning(request, f"⚠ Ignorados: {ignorados}")

        return redirect("lista_clientes")

    except Exception as e:
        messages.error(request, f"Erro ao executar importação: {str(e)}")
        return redirect("home")


# ==============================
# Lista de Clientes + Busca
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
