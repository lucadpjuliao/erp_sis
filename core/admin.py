from django.contrib import admin
from .models import Empresa, Configuracao


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'razao_social', 'matriz', 'is_active', 'created_at']
    list_filter = ['matriz', 'is_active', 'created_at']
    search_fields = ['nome', 'cnpj', 'razao_social']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'razao_social', 'cnpj', 'matriz')
        }),
        ('Documentos', {
            'fields': ('inscricao_estadual', 'inscricao_municipal')
        }),
        ('Contato', {
            'fields': ('endereco', 'telefone', 'email', 'site')
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


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ['chave', 'valor', 'tipo', 'is_active']
    list_filter = ['tipo', 'is_active']
    search_fields = ['chave', 'descricao']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    
    fieldsets = (
        ('Configuração', {
            'fields': ('chave', 'valor', 'tipo', 'descricao')
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