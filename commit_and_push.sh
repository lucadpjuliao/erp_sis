#!/bin/bash
echo "Fazendo commit das alterações..."
git add -A
git commit -m "Fix: Resolvido erro 'django_session does not exist' - Instalado PostgreSQL, configurado banco, executado migrações e criado superusuário admin"
echo "Fazendo push para o GitHub..."
git push origin main
echo "Atualização concluída no GitHub!"