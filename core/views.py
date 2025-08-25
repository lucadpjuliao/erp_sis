from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Empresa
from financeiro.models import ContasReceber, ContasPagar, MovimentacaoFinanceira
from operacional.models import Cliente, Fornecedor, Produto


@login_required
def dashboard(request):
    """Dashboard principal do sistema"""
    hoje = timezone.now().date()
    inicio_mes = hoje.replace(day=1)
    
    # Estatísticas gerais
    total_clientes = Cliente.objects.filter(is_active=True).count()
    total_fornecedores = Fornecedor.objects.filter(is_active=True).count()
    total_produtos = Produto.objects.filter(is_active=True).count()
    
    # Contas a receber - vencendo nos próximos 30 dias
    contas_receber_mes = ContasReceber.objects.filter(
        situacao='aberto',
        data_vencimento__gte=hoje,
        data_vencimento__lte=hoje + timedelta(days=30)
    ).aggregate(total=Sum('valor_original'))['total'] or 0
    
    # Contas a pagar - vencendo nos próximos 30 dias
    contas_pagar_mes = ContasPagar.objects.filter(
        situacao='aberto',
        data_vencimento__gte=hoje,
        data_vencimento__lte=hoje + timedelta(days=30)
    ).aggregate(total=Sum('valor_original'))['total'] or 0
    
    # Movimentações financeiras do mês
    receitas_mes = MovimentacaoFinanceira.objects.filter(
        tipo='entrada',
        data__gte=inicio_mes,
        data__lte=hoje
    ).aggregate(total=Sum('valor'))['total'] or 0
    
    despesas_mes = MovimentacaoFinanceira.objects.filter(
        tipo='saida',
        data__gte=inicio_mes,
        data__lte=hoje
    ).aggregate(total=Sum('valor'))['total'] or 0
    
    # Contas em atraso
    contas_receber_atraso = ContasReceber.objects.filter(
        situacao='aberto',
        data_vencimento__lt=hoje
    ).count()
    
    contas_pagar_atraso = ContasPagar.objects.filter(
        situacao='aberto',
        data_vencimento__lt=hoje
    ).count()
    
    context = {
        'total_clientes': total_clientes,
        'total_fornecedores': total_fornecedores,
        'total_produtos': total_produtos,
        'contas_receber_mes': contas_receber_mes,
        'contas_pagar_mes': contas_pagar_mes,
        'receitas_mes': receitas_mes,
        'despesas_mes': despesas_mes,
        'saldo_mes': receitas_mes - despesas_mes,
        'contas_receber_atraso': contas_receber_atraso,
        'contas_pagar_atraso': contas_pagar_atraso,
    }
    
    return render(request, 'core/dashboard.html', context)


@login_required
def empresas_list(request):
    """Lista de empresas"""
    empresas = Empresa.objects.filter(is_active=True)
    return render(request, 'core/empresas_list.html', {'empresas': empresas})


@login_required
def configuracoes(request):
    """Página de configurações"""
    return render(request, 'core/configuracoes.html')


@login_required
def usuarios(request):
    """Página de usuários"""
    return render(request, 'core/usuarios.html')
