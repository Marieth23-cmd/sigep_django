# Script de configuração inicial do SIGEP para Windows
# Execute: powershell -ExecutionPolicy Bypass -File setup.ps1

Write-Host "=========================================="
Write-Host "SIGEP - Setup Inicial (Windows)" -ForegroundColor Green
Write-Host "=========================================="
Write-Host ""

# Ativar ambiente virtual
Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
& .\env\Scripts\Activate.ps1

# Instalar dependências
Write-Host "Instalando/atualizando dependências..." -ForegroundColor Yellow
python -m pip install --upgrade pip
pip install -r requirements.txt

# Criar migrações
Write-Host "Criando migrações..." -ForegroundColor Yellow
python manage.py makemigrations

# Aplicar migrações
Write-Host "Aplicando migrações ao banco de dados..." -ForegroundColor Yellow
python manage.py migrate

# Coletar arquivos estáticos
Write-Host "Coletando arquivos estáticos..." -ForegroundColor Yellow
python manage.py collectstatic --noinput

Write-Host ""
Write-Host "=========================================="
Write-Host "Setup concluído com sucesso!" -ForegroundColor Green
Write-Host "=========================================="
Write-Host ""
Write-Host "Para executar o servidor, use:" -ForegroundColor Cyan
Write-Host "python manage.py runserver"
Write-Host ""
Write-Host "Acesse: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host ""
