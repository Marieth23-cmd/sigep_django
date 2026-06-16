#!/bin/bash
# Script de configuração inicial do SIGEP

echo "=========================================="
echo "SIGEP - Setup Inicial"
echo "=========================================="

# Ativar ambiente virtual
echo "✓ Ativando ambiente virtual..."
source env/Scripts/activate

# Instalar dependências
echo "✓ Instalando/atualizando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Criar migrações
echo "✓ Criando migrações..."
python manage.py makemigrations

# Aplicar migrações
echo "✓ Aplicando migrações ao banco de dados..."
python manage.py migrate

# Coletar arquivos estáticos
echo "✓ Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo ""
echo "=========================================="
echo "Setup concluído com sucesso!"
echo "=========================================="
echo ""
echo "Para executar o servidor, use:"
echo "python manage.py runserver"
echo ""
echo "Acesse: http://127.0.0.1:8000"
echo ""
