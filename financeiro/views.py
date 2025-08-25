from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PlanoContas, CentroCusto, Banco, ContasBancarias, ContasReceber, ContasPagar


@login_required
def plano_contas_list(request):
    """Lista do Plano de Contas"""
    contas = PlanoContas.objects.filter(is_active=True).order_by('codigo')
    return render(request, 'financeiro/plano_contas_list.html', {'contas': contas})


@login_required
def centro_custo_list(request):
    """Lista de Centros de Custo"""
    centros = CentroCusto.objects.filter(is_active=True).order_by('codigo')
    return render(request, 'financeiro/centro_custo_list.html', {'centros': centros})


@login_required
def bancos_list(request):
    """Lista de Bancos"""
    bancos = Banco.objects.filter(is_active=True).order_by('codigo')
    return render(request, 'financeiro/bancos_list.html', {'bancos': bancos})


@login_required
def contas_bancarias_list(request):
    """Lista de Contas Bancárias"""
    contas = ContasBancarias.objects.filter(is_active=True).order_by('banco__nome', 'agencia')
    return render(request, 'financeiro/contas_bancarias_list.html', {'contas': contas})


@login_required
def contas_receber_list(request):
    """Lista de Contas a Receber"""
    contas = ContasReceber.objects.filter(is_active=True).order_by('-data_vencimento')[:50]
    return render(request, 'financeiro/contas_receber_list.html', {'contas': contas})


@login_required
def contas_pagar_list(request):
    """Lista de Contas a Pagar"""
    contas = ContasPagar.objects.filter(is_active=True).order_by('-data_vencimento')[:50]
    return render(request, 'financeiro/contas_pagar_list.html', {'contas': contas})


@login_required
def relatorios_financeiros(request):
    """Relatórios Financeiros"""
    return render(request, 'financeiro/relatorios.html')
