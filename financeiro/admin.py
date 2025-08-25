from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PlanoContas, CentroCusto, ContasBancarias, FormaPagamento,
    ContasReceber, ContasPagar, MovimentacaoFinanceira
)


@admin.register(PlanoContas)
class PlanoContasAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'tipo', 'nivel', 'aceita_lancamento', 'is_active']
    list_filter = ['tipo', 'nivel', 'aceita_lancamento', 'is_active']
    search_fields = ['codigo', 'nome']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(CentroCusto)
class CentroCustoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'empresa', 'is_active']
    list_filter = ['empresa', 'is_active']
    search_fields = ['codigo', 'nome']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ContasBancarias)
class ContasBancariasAdmin(admin.ModelAdmin):
    list_display = ['banco', 'agencia', 'conta', 'digito', 'tipo', 'saldo_inicial', 'empresa']
    list_filter = ['tipo', 'empresa', 'is_active']
    search_fields = ['banco', 'agencia', 'conta']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'prazo_recebimento', 'taxa', 'is_active']
    list_filter = ['tipo', 'is_active']
    search_fields = ['nome']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ContasReceber)
class ContasReceberAdmin(admin.ModelAdmin):
    list_display = ['numero_documento', 'cliente', 'data_vencimento', 'valor_original', 'situacao', 'empresa']
    list_filter = ['situacao', 'data_vencimento', 'empresa', 'forma_pagamento']
    search_fields = ['numero_documento', 'cliente']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    date_hierarchy = 'data_vencimento'
    
    fieldsets = (
        ('Documento', {
            'fields': ('numero_documento', 'cliente', 'data_emissao', 'data_vencimento')
        }),
        ('Valores', {
            'fields': ('valor_original', 'valor_desconto', 'valor_juros', 'valor_multa')
        }),
        ('Recebimento', {
            'fields': ('valor_recebido', 'data_recebimento', 'situacao')
        }),
        ('Classificação', {
            'fields': ('conta_contabil', 'centro_custo', 'forma_pagamento', 'empresa')
        }),
        ('Auditoria', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(ContasPagar)
class ContasPagarAdmin(admin.ModelAdmin):
    list_display = ['numero_documento', 'fornecedor', 'data_vencimento', 'valor_original', 'situacao', 'empresa']
    list_filter = ['situacao', 'data_vencimento', 'empresa', 'forma_pagamento']
    search_fields = ['numero_documento', 'fornecedor']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    date_hierarchy = 'data_vencimento'
    
    fieldsets = (
        ('Documento', {
            'fields': ('numero_documento', 'fornecedor', 'data_emissao', 'data_vencimento')
        }),
        ('Valores', {
            'fields': ('valor_original', 'valor_desconto', 'valor_juros', 'valor_multa')
        }),
        ('Pagamento', {
            'fields': ('valor_pago', 'data_pagamento', 'situacao')
        }),
        ('Classificação', {
            'fields': ('conta_contabil', 'centro_custo', 'forma_pagamento', 'conta_bancaria', 'empresa')
        }),
        ('Auditoria', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(MovimentacaoFinanceira)
class MovimentacaoFinanceiraAdmin(admin.ModelAdmin):
    list_display = ['data', 'tipo', 'valor_formatado', 'descricao', 'conta_bancaria', 'empresa']
    list_filter = ['tipo', 'data', 'conta_bancaria', 'empresa']
    search_fields = ['descricao']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    date_hierarchy = 'data'
    
    def valor_formatado(self, obj):
        cor = 'green' if obj.tipo == 'entrada' else 'red'
        return format_html(
            '<span style="color: {};">R$ {:.2f}</span>',
            cor,
            obj.valor
        )
    valor_formatado.short_description = 'Valor'
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)