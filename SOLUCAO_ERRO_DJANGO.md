# Solução para o Erro "relation 'django_session' does not exist"

## Problema
O erro ocorria porque as tabelas do Django não foram criadas no banco de dados PostgreSQL. Especificamente, a tabela `django_session` não existia.

## Solução Implementada

### 1. Instalação de Dependências
- Instalado PostgreSQL e suas dependências
- Criado ambiente virtual Python
- Instalado Django e outras dependências

### 2. Configuração do Banco de Dados
- Criado banco de dados `db_erp`
- Configurado usuário `postgres` com senha `xbala`
- Criado arquivo `.env` com as configurações

### 3. Execução das Migrações
- Executado `python manage.py migrate` para criar todas as tabelas
- Incluindo:
  - `django_session` (sessões)
  - `auth_user` (usuários)
  - `django_admin_log` (logs do admin)
  - Tabelas das aplicações customizadas

### 4. Criação do Superusuário
- Criado usuário admin com senha `admin123`
- Credenciais para acessar o painel administrativo

## Arquivos Modificados

### requirements.txt
```
Django==5.2.5
djangorestframework==3.16.1
python-decouple==3.8
Pillow==10.4.0
django-cors-headers==4.4.0
psycopg2==2.9.10  # Atualizado para versão compatível com Python 3.13
```

### .env
```
PGDATABASE=db_erp
PGUSER=postgres
PGPASSWORD=xbala
PGHOST=localhost
PGPORT=5432
```

## Comandos para Executar

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Verificar migrações
python manage.py showmigrations

# Executar migrações (se necessário)
python manage.py migrate

# Iniciar servidor
python manage.py runserver 0.0.0.0:8000
```

## Acesso ao Admin
- URL: http://127.0.0.1:8000/admin/
- Usuário: `admin`
- Senha: `admin123`

## Status
✅ Erro resolvido - Tabelas criadas com sucesso
✅ Banco de dados configurado
✅ Migrações executadas
✅ Superusuário criado
✅ Sistema pronto para uso