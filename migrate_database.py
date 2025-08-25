#!/usr/bin/env python3
"""
Script específico para executar migrações do Django de forma segura
"""

import os
import sys
import django
from django.core.management import execute_from_command_line
from django.conf import settings

def setup_django():
    """Configura o Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_system.settings')
    django.setup()

def run_migrations():
    """Executa as migrações do Django de forma segura"""
    try:
        print("🔧 CONFIGURANDO DJANGO...")
        setup_django()
        
        print("\n📋 Verificando estado das migrações...")
        
        # 1. Verificar se há migrações pendentes
        try:
            print("🔍 Verificando migrações pendentes...")
            execute_from_command_line(['manage.py', 'showmigrations'])
        except Exception as e:
            print(f"⚠️  Aviso ao verificar migrações: {e}")
        
        # 2. Executar migrações principais do Django primeiro
        print("\n🚀 Aplicando migrações do Django...")
        core_apps = [
            'contenttypes',
            'auth', 
            'sessions',
            'admin',
            'messages'
        ]
        
        for app in core_apps:
            try:
                print(f"   📦 Migrando {app}...")
                execute_from_command_line(['manage.py', 'migrate', app])
            except Exception as e:
                print(f"   ⚠️  Erro em {app}: {e}")
        
        # 3. Executar migrações dos apps customizados
        print("\n🔧 Aplicando migrações dos módulos customizados...")
        custom_apps = ['core', 'financeiro', 'operacional']
        
        for app in custom_apps:
            try:
                print(f"   📦 Migrando {app}...")
                execute_from_command_line(['manage.py', 'migrate', app])
            except Exception as e:
                print(f"   ⚠️  Erro em {app}: {e}")
        
        # 4. Executar migrate geral
        print("\n🎯 Executando migrate geral...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("\n✅ MIGRAÇÕES CONCLUÍDAS COM SUCESSO!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        print("\n🔧 Tentando recuperação com --run-syncdb...")
        
        try:
            execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
            print("✅ Recuperação bem-sucedida!")
            return True
        except Exception as e2:
            print(f"❌ Falha na recuperação: {e2}")
            return False

def show_status():
    """Mostra o status das migrações"""
    try:
        print("\n📊 STATUS ATUAL DAS MIGRAÇÕES:")
        print("=" * 50)
        execute_from_command_line(['manage.py', 'showmigrations'])
        print("=" * 50)
    except Exception as e:
        print(f"❌ Erro ao mostrar status: {e}")

def main():
    """Função principal"""
    print("🏗️  SCRIPT DE MIGRAÇÃO DO BANCO DE DADOS ERP")
    print("=" * 50)
    
    # Configurar path do Django
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    success = run_migrations()
    
    if success:
        show_status()
        print("\n🎉 MIGRAÇÃO CONCLUÍDA!")
        print("💻 Agora você pode executar: python manage.py runserver")
    else:
        print("\n💥 FALHA NA MIGRAÇÃO!")
        print("🔧 Tente executar manualmente:")
        print("   python manage.py migrate --run-syncdb")
        print("   python manage.py migrate")

if __name__ == "__main__":
    main()