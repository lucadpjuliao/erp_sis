from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Pessoa, Cliente, Fornecedor, Funcionario, Categoria, UnidadeMedida,
    Produto, Estoque, MovimentacaoEstoque
)


class ClienteInline(admin.StackedInline):
    model = Cliente
    extra = 0


class FornecedorInline(admin.StackedInline):
    model = Fornecedor
    extra = 0


class FuncionarioInline(admin.StackedInline):
    model = Funcionario
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_pessoa', 'cpf_cnpj', 'telefone', 'email', 'empresa']
    list_filter = ['tipo_pessoa', 'empresa', 'is_active']
    search_fields = ['nome', 'cpf_cnpj', 'email']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    inlines = [ClienteInline, FornecedorInline, FuncionarioInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo_pessoa', 'cpf_cnpj', 'rg_ie')
        }),
        ('Contato', {
            'fields': ('endereco', 'telefone', 'celular', 'email')
        }),
        ('Dados Pessoais', {
            'fields': ('data_nascimento', 'observacoes')
        }),
        ('Empresa', {
            'fields': ('empresa',)
        }),
        ('Status', {
            'fields': ('is_active',)
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


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'pessoa', 'limite_credito', 'prazo_pagamento', 'data_cadastro']
    list_filter = ['data_cadastro', 'is_active']
    search_fields = ['codigo', 'pessoa__nome', 'pessoa__cpf_cnpj']
    readonly_fields = ['data_cadastro', 'created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'pessoa', 'prazo_entrega', 'data_cadastro']
    list_filter = ['data_cadastro', 'is_active']
    search_fields = ['codigo', 'pessoa__nome', 'pessoa__cpf_cnpj']
    readonly_fields = ['data_cadastro', 'created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'pessoa', 'cargo', 'setor', 'salario', 'situacao']
    list_filter = ['situacao', 'cargo', 'setor', 'data_admissao']
    search_fields = ['codigo', 'pessoa__nome', 'cargo', 'setor']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    date_hierarchy = 'data_admissao'
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'pai', 'is_active']
    list_filter = ['pai', 'is_active']
    search_fields = ['nome', 'descricao']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(UnidadeMedida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nome', 'sigla']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'categoria', 'preco_venda', 'tipo', 'controla_estoque']
    list_filter = ['categoria', 'tipo', 'controla_estoque', 'is_active']
    search_fields = ['codigo', 'nome', 'codigo_barras']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'nome', 'descricao', 'categoria', 'tipo')
        }),
        ('Características', {
            'fields': ('unidade_medida', 'peso', 'dimensoes', 'codigo_barras')
        }),
        ('Preços', {
            'fields': ('preco_custo', 'preco_venda', 'margem_lucro')
        }),
        ('Estoque', {
            'fields': ('controla_estoque', 'estoque_minimo', 'estoque_maximo')
        }),
        ('Status', {
            'fields': ('is_active',)
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


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'valor_unitario', 'valor_total_display', 'localizacao', 'empresa']
    list_filter = ['empresa', 'data_validade', 'is_active']
    search_fields = ['produto__codigo', 'produto__nome', 'lote', 'localizacao']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    def valor_total_display(self, obj):
        return format_html(
            '<span style="color: blue;">R$ {:.2f}</span>',
            obj.valor_total
        )
    valor_total_display.short_description = 'Valor Total'
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ['produto', 'tipo', 'quantidade', 'valor_unitario', 'data_movimentacao', 'empresa']
    list_filter = ['tipo', 'data_movimentacao', 'empresa']
    search_fields = ['produto__codigo', 'produto__nome', 'motivo', 'numero_documento']
    readonly_fields = ['data_movimentacao', 'created_at', 'updated_at', 'created_by', 'updated_by']
    date_hierarchy = 'data_movimentacao'
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)