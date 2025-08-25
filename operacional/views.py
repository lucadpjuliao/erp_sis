from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pessoa, Cliente, Fornecedor, Funcionario, Produto, Categoria, UnidadeMedida, Estoque


@login_required
def pessoas_list(request):
    """Lista de Pessoas"""
    pessoas = Pessoa.objects.filter(is_active=True).order_by('nome')[:50]
    return render(request, 'operacional/pessoas_list.html', {'pessoas': pessoas})


@login_required
def clientes_list(request):
    """Lista de Clientes"""
    clientes = Cliente.objects.filter(is_active=True).order_by('codigo')[:50]
    return render(request, 'operacional/clientes_list.html', {'clientes': clientes})


@login_required
def fornecedores_list(request):
    """Lista de Fornecedores"""
    fornecedores = Fornecedor.objects.filter(is_active=True).order_by('codigo')[:50]
    return render(request, 'operacional/fornecedores_list.html', {'fornecedores': fornecedores})


@login_required
def funcionarios_list(request):
    """Lista de Funcionários"""
    funcionarios = Funcionario.objects.filter(is_active=True).order_by('codigo')[:50]
    return render(request, 'operacional/funcionarios_list.html', {'funcionarios': funcionarios})


@login_required
def produtos_list(request):
    """Lista de Produtos"""
    produtos = Produto.objects.filter(is_active=True).order_by('codigo')[:50]
    return render(request, 'operacional/produtos_list.html', {'produtos': produtos})


@login_required
def categorias_list(request):
    """Lista de Categorias"""
    categorias = Categoria.objects.filter(is_active=True).order_by('nome')
    return render(request, 'operacional/categorias_list.html', {'categorias': categorias})


@login_required
def estoque_list(request):
    """Lista de Estoque"""
    estoques = Estoque.objects.filter(is_active=True).order_by('produto__codigo')[:50]
    return render(request, 'operacional/estoque_list.html', {'estoques': estoques})
