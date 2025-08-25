from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'financeiro'

# Router para ViewSets da API REST
router = DefaultRouter()

urlpatterns = [
    # Views principais
    path('plano-contas/', views.plano_contas_list, name='plano_contas_list'),
    path('centro-custo/', views.centro_custo_list, name='centro_custo_list'),
    path('bancos/', views.bancos_list, name='bancos_list'),
    path('contas-bancarias/', views.contas_bancarias_list, name='contas_bancarias_list'),
    path('contas-receber/', views.contas_receber_list, name='contas_receber_list'),
    path('contas-pagar/', views.contas_pagar_list, name='contas_pagar_list'),
    path('relatorios/', views.relatorios_financeiros, name='relatorios'),
    
    # API REST
    path('api/', include(router.urls)),
]