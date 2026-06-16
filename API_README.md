# SIGEP - Sistema de Gestão de Escolas (Com API Django REST)

## 🚀 Instalação e Configuração

### 1. Ativar o Ambiente Virtual

```bash
# No Windows (PowerShell)
.\env\Scripts\Activate.ps1

# Ou CMD
env\Scripts\activate.bat
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DATABASE_URL=postgresql://usuario:senha@host:porta/nome_banco

# Exemplo com Supabase:
# DATABASE_URL=postgresql://postgres:sua_senha@db.sua_regiao.supabase.co:5432/postgres
```

### 4. Fazer Migrações do Banco de Dados

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate
```

### 5. Executar o Servidor

```bash
python manage.py runserver
```

Acesse em: http://127.0.0.1:8000

## 📚 Endpoints da API

Todos os endpoints estão disponíveis em `/api/`:

### Escolas

- `GET /api/escolas/` - Listar todas as escolas
- `POST /api/escolas/` - Criar nova escola
- `GET /api/escolas/{id}/` - Obter detalhes de uma escola
- `PUT /api/escolas/{id}/` - Atualizar escola
- `DELETE /api/escolas/{id}/` - Deletar escola
- `GET /api/escolas/{id}/usuarios/` - Listar usuários de uma escola
- `GET /api/escolas/{id}/alunos/` - Listar alunos de uma escola
- `GET /api/escolas/{id}/cursos/` - Listar cursos de uma escola
- `GET /api/escolas/{id}/turmas/` - Listar turmas de uma escola

### Usuários

- `GET /api/usuarios/` - Listar todos os usuários
- `POST /api/usuarios/` - Criar novo usuário
- `GET /api/usuarios/por_escola/?escola_id=1` - Listar usuários de uma escola

### Cursos

- `GET /api/cursos/` - Listar todos os cursos
- `POST /api/cursos/` - Criar novo curso
- `GET /api/cursos/por_escola/?escola_id=1` - Listar cursos de uma escola

### Turmas

- `GET /api/turmas/` - Listar todas as turmas
- `POST /api/turmas/` - Criar nova turma
- `GET /api/turmas/por_escola/?escola_id=1` - Listar turmas de uma escola
- `GET /api/turmas/{id}/alunos/` - Listar alunos de uma turma

### Bolsas

- `GET /api/bolsas/` - Listar todas as bolsas
- `POST /api/bolsas/` - Criar nova bolsa
- `GET /api/bolsas/por_escola/?escola_id=1` - Listar bolsas de uma escola

### Alunos

- `GET /api/alunos/` - Listar todos os alunos
- `POST /api/alunos/` - Criar novo aluno
- `GET /api/alunos/por_escola/?escola_id=1` - Listar alunos de uma escola
- `GET /api/alunos/por_turma/?turma_id=1` - Listar alunos de uma turma
- `GET /api/alunos/{id}/pagamentos/` - Listar pagamentos de um aluno

### Pagamentos

- `GET /api/pagamentos/` - Listar todos os pagamentos
- `POST /api/pagamentos/` - Registar novo pagamento
- `GET /api/pagamentos/por_aluno/?aluno_id=1` - Listar pagamentos de um aluno
- `GET /api/pagamentos/por_mes_ano/?mes=6&ano=2026` - Listar pagamentos de um mês/ano

### Auditorias

- `GET /api/auditorias/` - Listar auditorias
- `GET /api/auditorias/por_usuario/?usuario_id=1` - Listar auditorias de um usuário

### Configurações

- `GET /api/configuracoes/` - Listar configurações
- `GET /api/configuracoes/por_escola/?escola_id=1` - Configuração de uma escola

## 🎯 Como Usar a API nos Templates

### Usando Fetch API

```javascript
// Obter alunos
fetch("/api/alunos/")
  .then((response) => response.json())
  .then((data) => console.log(data));

// Criar novo aluno
fetch("/api/alunos/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    nome: "João Silva",
    numero_aluno: 1,
    id_turma: 1,
    id_escola: 1,
    estado: "ACTIVO",
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

### Usando Axios (já incluído no projeto)

```javascript
// Obter alunos
axios.get("/api/alunos/").then((response) => console.log(response.data));

// Criar novo aluno
axios
  .post("/api/alunos/", {
    nome: "João Silva",
    numero_aluno: 1,
    id_turma: 1,
    id_escola: 1,
    estado: "ACTIVO",
  })
  .then((response) => console.log(response.data));
```

### Usando Classe SigepAPI (recomendado)

```javascript
// Obter todos os alunos
api
  .obterAlunos()
  .then((alunos) => console.log(alunos))
  .catch((erro) => console.error(erro));

// Obter alunos de uma escola específica
api.obterAlunosPorEscola(1).then((alunos) => console.log(alunos));

// Criar novo aluno
api
  .criarAluno({
    nome: "João Silva",
    numero_aluno: 1,
    id_turma: 1,
    id_escola: 1,
    estado: "ACTIVO",
  })
  .then((aluno) => console.log(aluno));
```

## 📁 Estrutura do Projeto

```
SIGEP/
├── manage.py
├── requirements.txt
├── .env
├── sigep/
│   ├── settings.py          # Configurações Django (REST Framework, CORS)
│   ├── urls.py              # URLs principais
│   ├── asgi.py
│   └── wsgi.py
├── home/
│   ├── migrations/          # Migrações de banco de dados
│   ├── models.py            # Modelos Django
│   ├── serializers.py       # Serializers DRF
│   ├── api_views.py         # ViewSets da API
│   ├── views.py             # Views tradicionais
│   ├── urls.py              # URLs da app
│   ├── admin.py
│   ├── apps.py
│   ├── static/
│   │   ├── css/
│   │   │   └── dashboard.css
│   │   └── js/
│   │       ├── api.js       # Classe utilitária para API
│   │       └── dashboard.js
│   └── templates/
│       ├── base.html
│       ├── alunos.html      # Consumindo API
│       ├── cursos.html      # Consumindo API
│       ├── pagamentos.html  # Consumindo API
│       ├── turmas.html
│       ├── header.html
│       ├── sidebar.html
│       └── ...outros templates
├── env/                     # Ambiente virtual
└── db.sqlite3
```

## 🔒 Segurança para Produção

### 1. Atualizar settings.py

```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
CORS_ALLOWED_ORIGINS = ['https://seu-dominio.com']
```

### 2. Coletar arquivos estáticos

```bash
python manage.py collectstatic --noinput
```

### 3. Criar superuser (administrador)

```bash
python manage.py createsuperuser
```

## 📊 Admin Django

Acesse em: http://127.0.0.1:8000/admin/

Faça login com as credenciais de superuser para gerenciar os dados.

## 🐛 Troubleshooting

### Erro: "django.core.exceptions.ImproperlyConfigured"

- Verifique se as variáveis de ambiente estão configuradas corretamente no arquivo `.env`

### Erro: "psycopg2 connection refused"

- Verifique a DATABASE_URL
- Certifique-se de que o servidor PostgreSQL/Supabase está acessível

### Erro 404 na API

- Verifique se está usando a URL correta: `/api/` (com barra no final)

## 📝 Próximos Passos

1. Implementar autenticação de usuários
2. Adicionar paginação nos endpoints
3. Implementar filtros mais avançados
4. Adicionar validações customizadas
5. Implementar exportação de dados (CSV, PDF)
6. Adicionar testes unitários

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação do Django REST Framework:
https://www.django-rest-framework.org/
