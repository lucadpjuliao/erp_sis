from django.db import models
from decimal import Decimal
from core.models import BaseModel, Empresa


class PlanoContas(BaseModel):
    """Plano de Contas"""
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                           related_name='filhos', verbose_name='Conta Pai')
    tipo = models.CharField(max_length=20, choices=[
        ('ativo', 'Ativo'),
        ('passivo', 'Passivo'),
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
        ('patrimonio', 'Patrimônio Líquido'),
    ], verbose_name='Tipo')
    nivel = models.PositiveIntegerField(default=1, verbose_name='Nível')
    aceita_lancamento = models.BooleanField(default=True, verbose_name='Aceita Lançamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Plano de Contas'
        verbose_name_plural = 'Planos de Contas'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class CentroCusto(BaseModel):
    """Centro de Custo"""
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                           related_name='filhos', verbose_name='Centro Pai')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Centro de Custo'
        verbose_name_plural = 'Centros de Custo'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Banco(BaseModel):
    """Bancos"""
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    
    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class ContasBancarias(BaseModel):
    """Contas Bancárias"""
    banco = models.ForeignKey(Banco, on_delete=models.PROTECT, verbose_name='Banco')
    agencia = models.CharField(max_length=10, verbose_name='Agência')
    conta = models.CharField(max_length=20, verbose_name='Conta')
    digito = models.CharField(max_length=2, verbose_name='Dígito')
    tipo = models.CharField(max_length=20, choices=[
        ('corrente', 'Conta Corrente'),
        ('poupanca', 'Poupança'),
        ('aplicacao', 'Aplicação'),
    ], verbose_name='Tipo')
    saldo_inicial = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                      verbose_name='Saldo Inicial')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'
        ordering = ['banco__nome', 'agencia', 'conta']

    def __str__(self):
        return f"{self.banco.nome} - {self.agencia}/{self.conta}-{self.digito}"


class FormaPagamento(BaseModel):
    """Formas de Pagamento"""
    nome = models.CharField(max_length=100, verbose_name='Nome')
    tipo = models.CharField(max_length=20, choices=[
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('transferencia', 'Transferência'),
        ('cheque', 'Cheque'),
        ('pix', 'PIX'),
        ('boleto', 'Boleto'),
    ], verbose_name='Tipo')
    prazo_recebimento = models.PositiveIntegerField(default=0, verbose_name='Prazo Recebimento (dias)')
    taxa = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'),
                              verbose_name='Taxa (%)')

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class ContasReceber(BaseModel):
    """Contas a Receber"""
    numero_documento = models.CharField(max_length=50, verbose_name='Número do Documento')
    cliente = models.ForeignKey('operacional.Cliente', on_delete=models.PROTECT, verbose_name='Cliente')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    data_emissao = models.DateField(verbose_name='Data de Emissão')
    valor_original = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor Original')
    valor_desconto = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                       verbose_name='Valor Desconto')
    valor_juros = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Valor Juros')
    valor_multa = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Valor Multa')
    valor_recebido = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                       verbose_name='Valor Recebido')
    data_recebimento = models.DateField(null=True, blank=True, verbose_name='Data de Recebimento')
    situacao = models.CharField(max_length=20, choices=[
        ('aberto', 'Aberto'),
        ('recebido', 'Recebido'),
        ('cancelado', 'Cancelado'),
    ], default='aberto', verbose_name='Situação')
    conta_contabil = models.ForeignKey(PlanoContas, on_delete=models.PROTECT, verbose_name='Conta Contábil')
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.PROTECT, verbose_name='Centro de Custo')
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT, verbose_name='Forma de Pagamento')
    conta_bancaria = models.ForeignKey(ContasBancarias, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Conta Bancária')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Conta a Receber'
        verbose_name_plural = 'Contas a Receber'
        ordering = ['-data_vencimento']

    def __str__(self):
        return f"{self.numero_documento} - {self.cliente.pessoa.nome}"

    @property
    def valor_total(self):
        return self.valor_original + self.valor_juros + self.valor_multa - self.valor_desconto


class ContasPagar(BaseModel):
    """Contas a Pagar"""
    numero_documento = models.CharField(max_length=50, verbose_name='Número do Documento')
    fornecedor = models.ForeignKey('operacional.Fornecedor', on_delete=models.PROTECT, verbose_name='Fornecedor')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    data_emissao = models.DateField(verbose_name='Data de Emissão')
    valor_original = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor Original')
    valor_desconto = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                       verbose_name='Valor Desconto')
    valor_juros = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Valor Juros')
    valor_multa = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                    verbose_name='Valor Multa')
    valor_pago = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'),
                                   verbose_name='Valor Pago')
    data_pagamento = models.DateField(null=True, blank=True, verbose_name='Data de Pagamento')
    situacao = models.CharField(max_length=20, choices=[
        ('aberto', 'Aberto'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ], default='aberto', verbose_name='Situação')
    conta_contabil = models.ForeignKey(PlanoContas, on_delete=models.PROTECT, verbose_name='Conta Contábil')
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.PROTECT, verbose_name='Centro de Custo')
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT, verbose_name='Forma de Pagamento')
    conta_bancaria = models.ForeignKey(ContasBancarias, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Conta Bancária')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Conta a Pagar'
        verbose_name_plural = 'Contas a Pagar'
        ordering = ['-data_vencimento']

    def __str__(self):
        return f"{self.numero_documento} - {self.fornecedor.pessoa.nome}"

    @property
    def valor_total(self):
        return self.valor_original + self.valor_juros + self.valor_multa - self.valor_desconto


class MovimentacaoFinanceira(BaseModel):
    """Movimentações Financeiras"""
    data = models.DateField(verbose_name='Data')
    tipo = models.CharField(max_length=20, choices=[
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ], verbose_name='Tipo')
    valor = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor')
    descricao = models.TextField(verbose_name='Descrição')
    conta_contabil = models.ForeignKey(PlanoContas, on_delete=models.PROTECT, verbose_name='Conta Contábil')
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.PROTECT, verbose_name='Centro de Custo')
    conta_bancaria = models.ForeignKey(ContasBancarias, on_delete=models.PROTECT, verbose_name='Conta Bancária')
    conta_receber = models.ForeignKey(ContasReceber, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Conta a Receber')
    conta_pagar = models.ForeignKey(ContasPagar, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Conta a Pagar')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Movimentação Financeira'
        verbose_name_plural = 'Movimentações Financeiras'
        ordering = ['-data']

    def __str__(self):
        return f"{self.data} - {self.tipo} - R$ {self.valor}"