from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModel(models.Model):
    """Modelo base com campos comuns para todos os modelos"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, 
                                 related_name='%(class)s_created', verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='%(class)s_updated', verbose_name='Atualizado por')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        abstract = True


class Empresa(BaseModel):
    """Modelo para representar a empresa/filiais"""
    nome = models.CharField(max_length=200, verbose_name='Nome da Empresa')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=200, verbose_name='Razão Social')
    inscricao_estadual = models.CharField(max_length=20, blank=True, verbose_name='Inscrição Estadual')
    inscricao_municipal = models.CharField(max_length=20, blank=True, verbose_name='Inscrição Municipal')
    endereco = models.TextField(verbose_name='Endereço')
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    site = models.URLField(blank=True, verbose_name='Site')
    matriz = models.BooleanField(default=False, verbose_name='É Matriz')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Configuracao(BaseModel):
    """Configurações gerais do sistema"""
    chave = models.CharField(max_length=100, unique=True, verbose_name='Chave')
    valor = models.TextField(verbose_name='Valor')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    tipo = models.CharField(max_length=20, choices=[
        ('string', 'Texto'),
        ('integer', 'Número Inteiro'),
        ('float', 'Número Decimal'),
        ('boolean', 'Verdadeiro/Falso'),
        ('json', 'JSON'),
    ], default='string', verbose_name='Tipo')

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'
        ordering = ['chave']

    def __str__(self):
        return f"{self.chave}: {self.valor}"