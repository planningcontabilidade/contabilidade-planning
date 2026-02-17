from django.db import models

class Cliente(models.Model):
    ordem = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=255)
    proprietario = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=20, null=True, blank=True)
    uf = models.CharField(max_length=5, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=50, null=True, blank=True)
    cpf_responsavel = models.CharField(max_length=20, null=True, blank=True)
    senha_sefaz = models.CharField(max_length=100, null=True, blank=True)
    inscricao_municipal = models.CharField(max_length=50, null=True, blank=True)
    login_prefeitura = models.CharField(max_length=100, null=True, blank=True)
    senha_prefeitura = models.CharField(max_length=100, null=True, blank=True)
    codigo_acesso = models.CharField(max_length=100, null=True, blank=True)
    senha_ecac = models.CharField(max_length=100, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome
