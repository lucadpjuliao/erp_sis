from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'operacional'

# Router para ViewSets da API REST
router = DefaultRouter()

urlpatterns = [
    # Views principais
    path('pessoas/', views.pessoas_list, name='pessoas_list'),
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('fornecedores/', views.fornecedores_list, name='fornecedores_list'),
    path('funcionarios/', views.funcionarios_list, name='funcionarios_list'),
    path('produtos/', views.produtos_list, name='produtos_list'),
    path('categorias/', views.categorias_list, name='categorias_list'),
    path('estoque/', views.estoque_list, name='estoque_list'),
    
    # API REST
    path('api/', include(router.urls)),
]