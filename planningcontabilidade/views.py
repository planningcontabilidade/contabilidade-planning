from django.db import connection, transaction
from django.http import HttpResponse
from django.core.management import call_command
import os


# ==============================
# Página Inicial
# ==============================
def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Planning Contabilidade</title>
                <style>
                    body {
                        font-family: Arial;
                        text-align: center;
                        margin-top: 100px;
                        background-color: #f4f6f9;
                    }
                    h1 { color: #2c3e50; }
                    a {
                        display: inline-block;
                        margin: 10px;
                        padding: 12px 25px;
                        background-color: #3498db;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                    }
                    a:hover { background-color: #2980b9; }
                </style>
            </head>
            <body>
                <h1>Planning Contabilidade</h1>
                <p>Sistema de Gestão de Clientes</p>
                <a href="/executar-importacao/">Importar Clientes</a>
            </body>
        </html>
    """)


# ==============================
# Executar Migrations
# ==============================
def executar_migrate(request):
    try:
        call_command("makemigrations")
        call_command("migrate")
        return HttpResponse("Migrations executadas com sucesso!")
    except Exception as e:
        return HttpResponse(f"Erro ao executar migrations: {str(e)}")


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

                    # Executa apenas INSERT
                    if comando.upper().startswith("INSERT"):
                        try:
                            cursor.execute(comando)
                            inseridos += 1
                        except Exception:
                            ignorados += 1

        return HttpResponse(
            f"""
            <h2>Importação Finalizada</h2>
            <p>✔ Inseridos: {inseridos}</p>
            <p>⚠ Ignorados: {ignorados}</p>
            <a href="/">Voltar para Home</a>
            """
        )

    except Exception as e:
        return HttpResponse(f"Erro ao executar importação: {str(e)}")
