from django.db import connection
from django.http import HttpResponse
from django.core.management import call_command
import os


def executar_migrate(request):
    try:
        call_command("makemigrations")
        call_command("migrate")
        return HttpResponse("Migrations executadas com sucesso!")
    except Exception as e:
        return HttpResponse(f"Erro ao executar migrations: {str(e)}")


def ajustar_nome_nullable(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER TABLE planningcontabilidade_cliente
                ALTER COLUMN nome DROP NOT NULL;
            """)
        return HttpResponse("Campo 'nome' agora permite NULL!")
    except Exception as e:
        return HttpResponse(f"Erro ao alterar campo: {str(e)}")


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

        with connection.cursor() as cursor:
            for comando in comandos:
                comando = comando.strip()
                if comando:
                    cursor.execute(comando)

        return HttpResponse("Importação executada com sucesso!")

    except Exception as e:
        return HttpResponse(f"Erro ao executar importação: {str(e)}")

