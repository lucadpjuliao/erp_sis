from django.db import models
from decimal import Decimal
from core.models import BaseModel, Empresa


class Pessoa(BaseModel):
    """Modelo base para Pessoas (Clientes, Fornecedores, Funcionários)"""
    nome = models.CharField(max_length=200, verbose_name='Nome')
    tipo_pessoa = models.CharField(max_length=20, choices=[
        ('fisica', 'Pessoa Física'),
        ('juridica', 'Pessoa Jurídica'),
    ], verbose_name='Tipo de Pessoa')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')
    rg_ie = models.CharField(max_length=20, blank=True, verbose_name='RG/IE')
    endereco = models.TextField(blank=True, verbose_name='Endereço')
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    celular = models.CharField(max_length=20, blank=True, verbose_name='Celular')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Cliente(BaseModel):
    """Clientes"""
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    limite_credito = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                       verbose_name='Limite de Crédito')
    prazo_pagamento = models.PositiveIntegerField(default=30, verbose_name='Prazo de Pagamento (dias)')
    vendedor = models.CharField(max_length=200, blank=True, verbose_name='Vendedor')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.pessoa.nome}"


class Fornecedor(BaseModel):
    """Fornecedores"""
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    prazo_entrega = models.PositiveIntegerField(default=0, verbose_name='Prazo de Entrega (dias)')
    condicoes_pagamento = models.TextField(blank=True, verbose_name='Condições de Pagamento')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.pessoa.nome}"


class Funcionario(BaseModel):
    """Funcionários"""
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    setor = models.CharField(max_length=100, verbose_name='Setor')
    salario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Salário')
    data_admissao = models.DateField(verbose_name='Data de Admissão')
    data_demissao = models.DateField(null=True, blank=True, verbose_name='Data de Demissão')
    situacao = models.CharField(max_length=20, choices=[
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('demitido', 'Demitido'),
        ('afastado', 'Afastado'),
    ], default='ativo', verbose_name='Situação')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.pessoa.nome}"


class Categoria(BaseModel):
    """Categorias de Produtos"""
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                           related_name='subcategorias', verbose_name='Categoria Pai')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class UnidadeMedida(BaseModel):
    """Unidades de Medida"""
    nome = models.CharField(max_length=50, verbose_name='Nome')
    sigla = models.CharField(max_length=10, unique=True, verbose_name='Sigla')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'
        ordering = ['nome']

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class Produto(BaseModel):
    """Produtos"""
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoria')
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name='Unidade de Medida')
    peso = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, verbose_name='Peso (kg)')
    dimensoes = models.CharField(max_length=100, blank=True, verbose_name='Dimensões')
    codigo_barras = models.CharField(max_length=50, blank=True, verbose_name='Código de Barras')
    preco_custo = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Preço de Custo')
    preco_venda = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Preço de Venda')
    margem_lucro = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'),
                                     verbose_name='Margem de Lucro (%)')
    estoque_minimo = models.DecimalField(max_digits=15, decimal_places=3, default=Decimal('0.000'),
                                       verbose_name='Estoque Mínimo')
    estoque_maximo = models.DecimalField(max_digits=15, decimal_places=3, default=Decimal('0.000'),
                                       verbose_name='Estoque Máximo')
    controla_estoque = models.BooleanField(default=True, verbose_name='Controla Estoque')
    tipo = models.CharField(max_length=20, choices=[
        ('produto', 'Produto'),
        ('servico', 'Serviço'),
        ('materia_prima', 'Matéria Prima'),
        ('produto_acabado', 'Produto Acabado'),
    ], default='produto', verbose_name='Tipo')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Estoque(BaseModel):
    """Controle de Estoque"""
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.DecimalField(max_digits=15, decimal_places=3, default=Decimal('0.000'),
                                   verbose_name='Quantidade')
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                       verbose_name='Valor Unitário')
    localizacao = models.CharField(max_length=100, blank=True, verbose_name='Localização')
    lote = models.CharField(max_length=50, blank=True, verbose_name='Lote')
    data_validade = models.DateField(null=True, blank=True, verbose_name='Data de Validade')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        ordering = ['produto__codigo']
        unique_together = ['produto', 'empresa', 'lote']

    def __str__(self):
        return f"{self.produto.codigo} - Qtd: {self.quantidade}"

    @property
    def valor_total(self):
        return self.quantidade * self.valor_unitario


class MovimentacaoEstoque(BaseModel):
    """Movimentações de Estoque"""
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    tipo = models.CharField(max_length=20, choices=[
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('ajuste', 'Ajuste'),
        ('transferencia', 'Transferência'),
    ], verbose_name='Tipo')
    quantidade = models.DecimalField(max_digits=15, decimal_places=3, verbose_name='Quantidade')
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor Unitário')
    motivo = models.CharField(max_length=200, verbose_name='Motivo')
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    data_movimentacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Movimentação')
    numero_documento = models.CharField(max_length=50, blank=True, verbose_name='Número do Documento')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'
        ordering = ['-data_movimentacao']

    def __str__(self):
        return f"{self.produto.codigo} - {self.tipo} - {self.quantidade}"

    @property
    def valor_total(self):
        return self.quantidade * self.valor_unitario