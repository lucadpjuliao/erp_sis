# 🏢 Sistema ERP - Enterprise Resource Planning

> Sistema ERP moderno e completo desenvolvido em Django com interface responsiva, menu lateral animado e funcionalidades avançadas para gestão empresarial.

![Django](https://img.shields.io/badge/Django-5.2.5-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Python](https://img.shields.io/badge/Python-3.12+-yellow)

## ✨ **Funcionalidades Principais**

### 🎨 **Interface Moderna**
- ✅ **Menu Sidebar Responsivo** - Menu lateral animado com collapse/expand
- ✅ **Bootstrap 5 Integrado** - Design moderno e responsivo
- ✅ **Font Awesome** - Ícones vetoriais em toda interface
- ✅ **Design Gradiente** - Cores modernas com gradientes
- ✅ **Tema Escuro** - Sidebar elegante com tema escuro

### 📊 **Dashboard Interativo**
- ✅ **Cards Estatísticos** - Métricas em tempo real com animações
- ✅ **Visão Geral Financeira** - Receitas, despesas e saldo do mês
- ✅ **Alertas Inteligentes** - Contas em atraso e vencimentos
- ✅ **Ações Rápidas** - Botões para cadastros frequentes
- ✅ **Animações CSS** - Transições suaves e efeitos visuais

### 🏗️ **Core/Base**
- ✅ Dashboard interativo com métricas em tempo real
- ✅ Gestão de empresas/filiais
- ✅ Sistema de usuários e permissões
- ✅ Configurações globais do sistema

### 💰 **Módulo Financeiro**
- ✅ Plano de Contas hierárquico
- ✅ Centro de Custos com estrutura pai-filho
- ✅ Cadastro de Bancos
- ✅ Contas Bancárias
- ✅ Contas a Receber com FK para Clientes
- ✅ Contas a Pagar com FK para Fornecedores
- ✅ Movimentações Financeiras
- ✅ Relatórios financeiros

### 🏢 **Módulo Operacional**
- ✅ Cadastro de Pessoas (base para Clientes/Fornecedores)
- ✅ Gestão de Clientes
- ✅ Gestão de Fornecedores
- ✅ Gestão de Funcionários
- ✅ Cadastro de Produtos
- ✅ Categorias hierárquicas
- ✅ Unidades de Medida
- ✅ Controle de Estoque
- ✅ Movimentações de Estoque

### 🔗 **Relacionamentos FK Melhorados**
- ✅ **Contas a Receber → Cliente** - Referência direta
- ✅ **Contas a Pagar → Fornecedor** - Referência direta
- ✅ **Plano de Contas** - Hierarquia pai-filho
- ✅ **Centro de Custo** - Estrutura hierárquica
- ✅ **Integridade Referencial** - CASCADE e PROTECT adequados

## 🛠️ **Stack Tecnológica**

- **Backend:** Django 5.2.5, Django REST Framework 3.16.1
- **Banco de Dados:** PostgreSQL 12+
- **Frontend:** Bootstrap 5.3, Font Awesome 6.4, JavaScript ES6+
- **Python:** 3.12+
- **Outros:** python-decouple, psycopg2-binary, django-cors-headers

## 📋 **Pré-requisitos**

- Python 3.12 ou superior
- PostgreSQL 12 ou superior
- pip (gerenciador de pacotes Python)

## ⚡ **Instalação Rápida**

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd sistema-erp

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure o PostgreSQL (credenciais no .env)
cp .env.example .env

# 4. Execute a configuração automática
python create_database.py

# 5. Inicie o servidor
python manage.py runserver
```

## 🌐 **Acessos**

- **Dashboard:** http://127.0.0.1:8000/
- **Admin Django:** http://127.0.0.1:8000/admin/
- **Credenciais padrão:** admin / admin123

## 📊 **Screenshots**

### Dashboard Principal
```
🎯 Cards com métricas em tempo real
📈 Gráficos de receitas e despesas  
⚠️ Alertas de contas em atraso
🚀 Ações rápidas para cadastros
```

### Menu Sidebar Responsivo
```
🏠 Core (Dashboard, Empresas, Usuários, Configurações)
💰 Financeiro (Plano Contas, Centro Custo, Bancos, Contas)
🏢 Operacional (Pessoas, Clientes, Fornecedores, Produtos, Estoque)
```

## 🗄️ **Configuração PostgreSQL**

### Credenciais Padrão (configuráveis no .env)
```env
PGHOST=localhost
PGPORT=5432
PGUSER=postgres
PGPASSWORD=xbala
PGDATABASE=db_erp
```

### Script Automático
O sistema inclui script automático que:
- ✅ Cria o banco de dados
- ✅ Testa a conexão
- ✅ Executa migrações
- ✅ Cria superusuário padrão

## 📚 **Documentação**

- **[INSTALL.md](INSTALL.md)** - Guia completo de instalação
- **[CHANGELOG.md](CHANGELOG.md)** - Histórico de mudanças
- **Comentários no código** - Documentação inline

## 🔧 **Resolução de Problemas**

### Erro: "relation does not exist"
```bash
python migrate_database.py
```

### Erro de conexão PostgreSQL
1. Verifique se o PostgreSQL está rodando
2. Confirme credenciais no arquivo `.env`
3. Execute `python create_database.py`

### Para resetar completamente
```bash
dropdb db_erp  # CUIDADO: apaga todos os dados
python create_database.py
```

## 📈 **Estrutura do Projeto**

```
sistema-erp/
├── 🏗️ core/                 # Módulo base
│   ├── templates/           # Templates HTML
│   ├── static/             # CSS, JS, imagens
│   └── models.py           # Empresa, Configuração
├── 💰 financeiro/          # Módulo financeiro
│   └── models.py           # Plano Contas, Contas, Bancos
├── 🏢 operacional/         # Módulo operacional
│   └── models.py           # Pessoas, Produtos, Estoque
├── ⚙️ erp_system/          # Configurações Django
├── 🗄️ create_database.py   # Setup automático PostgreSQL
├── 🔧 migrate_database.py  # Migração segura
└── 📋 requirements.txt     # Dependências
```

## 🚀 **Próximos Passos**

### v1.2.0 - Templates Completos
- [ ] Templates para todos os módulos
- [ ] Formulários de cadastro/edição
- [ ] Confirmações e validações

### v1.3.0 - API REST Avançada
- [ ] ViewSets completos
- [ ] Serializers customizados
- [ ] Filtros e paginação

### v1.4.0 - Relatórios e Analytics
- [ ] Relatórios PDF
- [ ] Gráficos interativos
- [ ] Dashboard analytics

### v1.5.0 - Módulos Avançados
- [ ] Módulo de Vendas
- [ ] Módulo de Compras
- [ ] Integração NFe

## 🤝 **Contribuição**

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 **Licença**

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⭐ **Agradecimentos**

- Comunidade Django pela excelente documentação
- Bootstrap team pelo framework CSS moderno
- PostgreSQL team pelo banco de dados robusto
- Font Awesome pelos ícones vetoriais

---

<div align="center">

**[⬆ Voltar ao topo](#-sistema-erp---enterprise-resource-planning)**

Feito com ❤️ em Django | Contribuições são bem-vindas!

</div>