import pandas as pd
from django.core.management.base import BaseCommand
from planningcontabilidade.models import Cliente


class Command(BaseCommand):
    help = 'Importa clientes da planilha Excel'

    def handle(self, *args, **kwargs):
        caminho_arquivo = "LC CONTROLE - CLIENTES.xlsx"

        df = pd.read_excel(caminho_arquivo)

        # Ajusta cabeçalho real (segunda linha)
        df.columns = df.iloc[0]
        df = df[1:]

        for _, row in df.iterrows():
            Cliente.objects.create(
                ordem=row.get("ORD"),
                nome=row.get("NOME"),
                proprietario=row.get("PROPRIETÁRIO"),
                cnpj=row.get("CNPJ"),
                uf=row.get("UF"),
                inscricao_estadual=row.get("INSC ESTADUAL"),
                cpf_responsavel=row.get("CPF RESPONSÁVEL"),
                senha_sefaz=row.get("SENHA SEFAZ"),
                inscricao_municipal=row.get("INSC MUNICIPAL"),
                login_prefeitura=row.get("LOGIN PREFEITURA"),
                senha_prefeitura=row.get("SENHA PREFEITURA"),
                codigo_acesso=row.get("CODIGO ACESSO"),
                senha_ecac=row.get("SENHA ECAC"),
                observacao=row.get("OBSERVAÇÃO"),
            )

        self.stdout.write(self.style.SUCCESS("Clientes importados com sucesso!"))
