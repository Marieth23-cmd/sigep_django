# 🎉 API SIGEP - Documentação Rápida

## 📊 Arquitetura da Solução

```
┌─────────────────────────────────────────────────────────────┐
│                    NAVEGADOR (Frontend)                      │
│                                                               │
│  alunos.html │ cursos.html │ pagamentos.html │ ...          │
│     ↓              ↓              ↓                          │
│  JavaScript - Axios/Fetch - SigepAPI (api.js)               │
└─────────────────────────┬───────────────────────────────────┘
                          │
                    HTTP Requests
                          │
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                   DJANGO REST API                            │
│                   (/api/ endpoints)                          │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  home/api_views.py (ViewSets)                       │   │
│  │  • EscolaViewSet                                     │   │
│  │  • UsuarioViewSet                                    │   │
│  │  • CursoViewSet                                      │   │
│  │  • TurmaViewSet                                      │   │
│  │  • BolsaViewSet                                      │   │
│  │  • AlunoViewSet                                      │   │
│  │  • PagamentoViewSet                                  │   │
│  │  • AuditoriaViewSet                                  │   │
│  │  • ConfiguracaoEscolaViewSet                         │   │
│  └──────────────────────────────────────────────────────┘   │
│                          │                                   │
│  Serializers (validação)│ Views (lógica)                    │
│     ↓                   │                                   │
│  home/serializers.py ← → home/models.py                     │
└─────────────────────────┬───────────────────────────────────┘
                          │
                   Database Queries
                          │
                          ↓
┌─────────────────────────────────────────────────────────────┐
│           PostgreSQL (Supabase / Localhost)                 │
│                                                               │
│  escolas │ usuarios │ cursos │ turmas │ bolsas │ alunos    │
│  pagamentos │ auditoria │ configuracoes_escola             │
└─────────────────────────────────────────────────────────────┘
```

## 🔗 Endpoints Principais

### Alunos

```
GET    /api/alunos/                      ← Listar todos
POST   /api/alunos/                      ← Criar novo
GET    /api/alunos/por_escola/           ← Filtrar por escola
GET    /api/alunos/por_turma/            ← Filtrar por turma
GET    /api/alunos/{id}/pagamentos/      ← Ver pagamentos de um aluno
```

### Pagamentos

```
GET    /api/pagamentos/                  ← Listar todos
POST   /api/pagamentos/                  ← Registar novo
GET    /api/pagamentos/por_aluno/        ← Filtrar por aluno
GET    /api/pagamentos/por_mes_ano/      ← Filtrar por mês/ano
```

### Cursos

```
GET    /api/cursos/                      ← Listar todos
POST   /api/cursos/                      ← Criar novo
GET    /api/cursos/por_escola/           ← Filtrar por escola
```

### Escolas

```
GET    /api/escolas/                     ← Listar todas
POST   /api/escolas/                     ← Criar nova
GET    /api/escolas/{id}/usuarios/       ← Ver usuários
GET    /api/escolas/{id}/alunos/         ← Ver alunos
GET    /api/escolas/{id}/cursos/         ← Ver cursos
GET    /api/escolas/{id}/turmas/         ← Ver turmas
GET    /api/escolas/{id}/bolsas/         ← Ver bolsas
```

## 📝 Exemplos de Uso

### Exemplo 1: Listar Alunos (com Axios)

```javascript
axios
  .get("/api/alunos/")
  .then((res) => {
    console.log(res.data); // Array de alunos
    res.data.forEach((aluno) => {
      console.log(`${aluno.numero_aluno}: ${aluno.nome}`);
    });
  })
  .catch((err) => console.error(err));
```

### Exemplo 2: Criar Novo Aluno

```javascript
const novoAluno = {
  nome: "João da Silva",
  numero_aluno: 42,
  id_turma: 1,
  id_escola: 1,
  estado: "ACTIVO",
  data_nascimento: "2005-03-15",
  sexo: "Masculino",
};

axios
  .post("/api/alunos/", novoAluno)
  .then((res) => {
    console.log("Aluno criado:", res.data);
    alert("Aluno " + res.data.nome + " registado com sucesso!");
  })
  .catch((err) => {
    console.error("Erro:", err.response.data);
    alert("Erro ao registar aluno");
  });
```

### Exemplo 3: Registar Pagamento

```javascript
const pagamento = {
  id_aluno: 1,
  mes: 6,
  ano: 2026,
  valor_propina: 15000.0,
  valor_pago: 15000.0,
  data_pagamento: "2026-06-15",
  metodo_pagamento: "Transferência",
  observacao: "Pagamento completo",
};

axios
  .post("/api/pagamentos/", pagamento)
  .then((res) => console.log("Pagamento registado!", res.data))
  .catch((err) => console.error("Erro:", err));
```

### Exemplo 4: Usar Classe SigepAPI

```javascript
// Obter todos os alunos de uma turma
api.obterAlunosPorTurma(1).then((alunos) => {
  console.log(`${alunos.length} alunos encontrados`);
});

// Obter pagamentos de um aluno
api.obterPagamentosAluno(5).then((pagamentos) => {
  let total = pagamentos.reduce((sum, p) => sum + p.valor_pago, 0);
  console.log("Total pago:", total);
});

// Obter pagamentos de um mês específico
api
  .obterPagamentosMesAno(6, 2026)
  .then((pagamentos) => console.log(pagamentos));
```

## 🚀 Executar o Projeto

### 1️⃣ Setup Inicial (Windows)

```powershell
# Abrir PowerShell e executar:
powershell -ExecutionPolicy Bypass -File setup.ps1
```

### 2️⃣ Configurar .env

Criar arquivo `.env` na raiz:

```env
SECRET_KEY=django-insecure-sua-chave-aqui
DEBUG=True
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/sigep
```

### 3️⃣ Iniciar Servidor

```bash
python manage.py runserver
```

### 4️⃣ Acessar

- **Frontend**: http://127.0.0.1:8000
- **API**: http://127.0.0.1:8000/api/
- **Admin**: http://127.0.0.1:8000/admin/

## 📦 Arquivos Criados/Modificados

| Arquivo                        | Status        | Descrição             |
| ------------------------------ | ------------- | --------------------- |
| home/models.py                 | ✅ Criado     | 9 modelos Django      |
| home/serializers.py            | ✅ Criado     | Serializers DRF       |
| home/api_views.py              | ✅ Criado     | ViewSets da API       |
| home/urls.py                   | ✅ Modificado | Roteadores DRF        |
| home/templates/alunos.html     | ✅ Modificado | Consome API           |
| home/templates/cursos.html     | ✅ Modificado | Consome API           |
| home/templates/pagamentos.html | ✅ Modificado | Consome API           |
| home/static/js/api.js          | ✅ Criado     | Classe SigepAPI       |
| sigep/settings.py              | ✅ Modificado | DRF + CORS            |
| sigep/urls.py                  | ✅ OK         | Já include home.urls  |
| requirements.txt               | ✅ Modificado | +DRF +CORS            |
| API_README.md                  | ✅ Criado     | Documentação completa |
| SETUP.md                       | ✅ Criado     | Guia de setup         |
| setup.ps1                      | ✅ Criado     | Script Windows        |
| setup.sh                       | ✅ Criado     | Script Linux/Mac      |

## 🔐 Segurança

⚠️ **Antes de ir para Produção:**

```python
# settings.py
DEBUG = False
SECRET_KEY = 'gere-uma-chave-segura-real'
ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com']

CORS_ALLOWED_ORIGINS = [
    'https://seu-dominio.com',
    'https://www.seu-dominio.com',
]

# Usar HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 🐛 Troubleshooting Rápido

| Problema                    | Solução                                       |
| --------------------------- | --------------------------------------------- |
| API retorna 404             | Verifique URL com `/api/` no final            |
| Database connection refused | Verifique DATABASE_URL no .env                |
| CORS error                  | Verifique CORS_ALLOWED_ORIGINS em settings.py |
| Import error em models      | Certifique-se que migrations estão feitas     |
| Template não carrega dados  | Verifique console do navegador (F12)          |

## 📚 Documentação Completa

Para documentação detalhada, consulte:

- **API_README.md** - Guia completo da API
- **SETUP.md** - Instruções de setup
- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [Django Docs](https://docs.djangoproject.com/)

## ✅ Checklist Final

- [ ] Clonar/baixar código
- [ ] Executar `setup.ps1` (ou `setup.sh`)
- [ ] Criar arquivo `.env`
- [ ] Executar `python manage.py runserver`
- [ ] Acessar http://127.0.0.1:8000
- [ ] Testar endpoints em http://127.0.0.1:8000/api/

---

**🎯 Pronto para usar! A sua API REST do SIGEP está 100% funcional! 🚀**
