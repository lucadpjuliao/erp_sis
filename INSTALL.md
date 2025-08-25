# 🛠️ Guia de Instalação - Sistema ERP

## 📋 Pré-requisitos

### Sistema Operacional
- Windows 10/11, macOS, ou Linux (Ubuntu 20.04+)

### Software Necessário
- **Python 3.12+** - [Download Python](https://python.org/downloads/)
- **PostgreSQL 12+** - [Download PostgreSQL](https://postgresql.org/download/)
- **Git** - [Download Git](https://git-scm.com/downloads/)

## 🚀 Instalação Passo a Passo

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/sistema-erp.git
cd sistema-erp
```

### 2. Criar Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

#### 4.1. Instalar PostgreSQL
**Windows:**
- Baixe e instale pelo [site oficial](https://postgresql.org/download/windows/)
- Durante a instalação, defina a senha do usuário `postgres`

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
```

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

#### 4.2. Configurar Usuário e Banco
```sql
-- Conectar ao PostgreSQL como superusuário
sudo -u postgres psql

-- Criar usuário (se não existir)
CREATE USER postgres WITH PASSWORD 'xbala';
ALTER USER postgres CREATEDB;

-- Sair do psql
\q
```

### 5. Configurar Variáveis de Ambiente

#### 5.1. Copiar arquivo de exemplo
```bash
cp .env.example .env
```

#### 5.2. Editar arquivo .env
```env
# Configurações do Banco PostgreSQL
PGHOST=localhost
PGPORT=5432
PGUSER=postgres
PGPASSWORD=xbala
PGDATABASE=db_erp

# Configurações do Django
SECRET_KEY=django-insecure-fwpkjr*+=!-!l9d7w4&xoj6fvqlvqz#^r)s$^3v*9)5i$1)-gz
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Executar Configuração Automática
```bash
python create_database.py
```

#### 6.1. Em caso de erro de migração
```bash
python migrate_database.py
```

### 7. Executar o Servidor
```bash
python manage.py runserver
```

## 🌐 Acessar o Sistema

- **Dashboard Principal:** http://127.0.0.1:8000/
- **Admin Django:** http://127.0.0.1:8000/admin/
- **Credenciais:** admin / admin123

## 🔧 Resolução de Problemas

### Erro: "psycopg2 não encontrado"
```bash
# Ubuntu/Debian
sudo apt-get install libpq-dev python3-dev

# CentOS/RHEL
sudo yum install postgresql-devel python3-devel

# Depois reinstalar
pip install psycopg2-binary
```

### Erro: "relation does not exist"
```bash
python migrate_database.py
```

### Erro: "PostgreSQL não está rodando"
```bash
# Windows (Services)
# Iniciar serviço "postgresql-x64-xx"

# Ubuntu/Debian
sudo systemctl start postgresql
sudo systemctl enable postgresql

# macOS
brew services start postgresql
```

### Erro: "Port 8000 já em uso"
```bash
python manage.py runserver 8080
```

## 🔄 Comandos Úteis

### Backup do Banco
```bash
pg_dump -U postgres -h localhost db_erp > backup.sql
```

### Restaurar Backup
```bash
psql -U postgres -h localhost db_erp < backup.sql
```

### Resetar Banco de Dados
```bash
# CUIDADO: Apaga todos os dados!
dropdb -U postgres db_erp
python create_database.py
```

### Criar Usuário Admin Adicional
```bash
python manage.py createsuperuser
```

### Coletar Arquivos Estáticos (Produção)
```bash
python manage.py collectstatic
```

## 📱 Funcionalidades Disponíveis

### ✅ Implementado
- [x] Dashboard interativo
- [x] Menu responsivo com sidebar
- [x] Módulo Core (Empresas, Usuários, Configurações)
- [x] Módulo Financeiro (Plano de Contas, Centros de Custo, Bancos, Contas)
- [x] Módulo Operacional (Pessoas, Clientes, Fornecedores, Produtos, Estoque)
- [x] Interface moderna com Bootstrap 5
- [x] Relacionamentos FK entre módulos
- [x] Script de migração automática
- [x] Configuração PostgreSQL

### 🔮 Próximas Versões
- [ ] Templates completos para todas as views
- [ ] API REST completa
- [ ] Relatórios PDF
- [ ] Gráficos interativos
- [ ] Módulo de Vendas
- [ ] Módulo de Compras
- [ ] Integração NFe

## 🆘 Suporte

### Documentação
- **README.md** - Visão geral do projeto
- **INSTALL.md** - Este guia de instalação
- **requirements.txt** - Dependências Python

### Problemas Comuns
1. **Erro de migração:** Execute `python migrate_database.py`
2. **PostgreSQL não conecta:** Verifique credenciais no `.env`
3. **Porta em uso:** Use `python manage.py runserver 8080`
4. **Permissões negadas:** Execute como administrador (Windows) ou use `sudo` (Linux)

### Contato
- Abra uma issue no GitHub
- Verifique logs em `debug.log` (se existir)
- Execute `python manage.py check` para diagnósticos

## 📄 Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.