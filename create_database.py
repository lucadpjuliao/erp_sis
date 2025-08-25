#!/usr/bin/env python3
"""
Script para criar e configurar o banco de dados PostgreSQL para o sistema ERP
"""

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Configurações do banco
DB_HOST = os.getenv("PGHOST", "localhost")
DB_PORT = os.getenv("PGPORT", "5432")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASSWORD = os.getenv("PGPASSWORD", "xbala")
DB_NAME = os.getenv("PGDATABASE", "db_erp")

def create_database():
    """Cria o banco de dados se não existir"""
    try:
        # Conecta ao PostgreSQL sem especificar o banco
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Verifica se o banco existe
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        exists = cursor.fetchone()
        
        if not exists:
            print(f"Criando banco de dados '{DB_NAME}'...")
            cursor.execute(f'CREATE DATABASE "{DB_NAME}"')
            print(f"✅ Banco de dados '{DB_NAME}' criado com sucesso!")
        else:
            print(f"✅ Banco de dados '{DB_NAME}' já existe.")
        
        cursor.close()
        conn.close()
        
    except psycopg2.Error as e:
        print(f"❌ Erro ao conectar/criar banco: {e}")
        return False
    
    return True

def test_connection():
    """Testa a conexão com o banco de dados"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Conexão com PostgreSQL estabelecida!")
        print(f"📊 Versão: {version[0]}")
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Erro na conexão: {e}")
        return False

def run_migrations():
    """Executa as migrações do Django"""
    try:
        print("🔄 Executando migrações...")
        
        # Configura o Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_system.settings')
        django.setup()
        
        # Executa makemigrations
        print("📝 Gerando migrações...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        
        # Executa migrate
        print("🚀 Aplicando migrações...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("✅ Migrações aplicadas com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro nas migrações: {e}")
        return False

def create_superuser():
    """Cria um superusuário padrão"""
    try:
        from django.contrib.auth.models import User
        
        username = 'admin'
        email = 'admin@erp.com'
        password = 'admin123'
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print(f"✅ Superusuário criado: {username} / {password}")
        else:
            print(f"✅ Superusuário '{username}' já existe.")
            
    except Exception as e:
        print(f"❌ Erro ao criar superusuário: {e}")

def main():
    """Função principal"""
    print("🏗️  CONFIGURAÇÃO DO BANCO DE DADOS ERP")
    print("=" * 50)
    
    print("\n📋 Configurações:")
    print(f"Host: {DB_HOST}")
    print(f"Porta: {DB_PORT}")
    print(f"Usuário: {DB_USER}")
    print(f"Banco: {DB_NAME}")
    
    print("\n🔧 Etapa 1: Criando banco de dados...")
    if not create_database():
        return
    
    print("\n🔧 Etapa 2: Testando conexão...")
    if not test_connection():
        return
    
    print("\n🔧 Etapa 3: Executando migrações...")
    if not run_migrations():
        return
    
    print("\n🔧 Etapa 4: Criando superusuário...")
    create_superuser()
    
    print("\n🎉 CONFIGURAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 50)
    print("💻 Para iniciar o servidor:")
    print("   python manage.py runserver")
    print("\n🌐 Acesso admin:")
    print("   http://127.0.0.1:8000/admin/")
    print("   Usuário: admin")
    print("   Senha: admin123")

if __name__ == "__main__":
    main()