from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

# Router para ViewSets da API REST
router = DefaultRouter()

urlpatterns = [
    # Views principais do sistema
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('empresas/', views.empresas_list, name='empresas_list'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('usuarios/', views.usuarios, name='usuarios'),
    
    # API REST
    path('api/', include(router.urls)),
]