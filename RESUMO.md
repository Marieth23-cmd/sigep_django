# 🎯 SIGEP - API REST | Sumário Executivo

## 📌 O Que Você Pediu

> Criar uma API e fazer o template consumir a mesma

## ✅ O Que Implementamos

### 1. **API REST Completa com Django REST Framework**

- ✅ 9 modelos Django para toda estrutura de dados
- ✅ Serializers validação e transformação de dados
- ✅ 9 ViewSets com operações CRUD completas
- ✅ Endpoints customizados para filtros avançados
- ✅ Paginação configurada
- ✅ Suporte a CORS para requisições do frontend

### 2. **Templates Dinâmicos Consumindo a API**

- ✅ `alunos.html` - Lista, busca e cria alunos via API
- ✅ `cursos.html` - Gerencia cursos via API
- ✅ `pagamentos.html` - Registra pagamentos com estatísticas

### 3. **JavaScript Utilitário**

- ✅ Classe `SigepAPI` com métodos prontos
- ✅ Requisições simplificadas com Axios
- ✅ Tratamento de erros e loading

---

## 📊 Estrutura Criada

```
🌍 FRONTEND (Navegador)
   ↓ JavaScript/Axios
📡 API REST (/api/)
   ↓ Django ORM
💾 PostgreSQL (Supabase)
```

---

## 🚀 Como Usar

### **Passo 1: Setup**

```powershell
# Windows PowerShell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

### **Passo 2: Configurar .env**

```env
DATABASE_URL=postgresql://user:pass@host:5432/dbname
SECRET_KEY=sua-chave-aqui
DEBUG=True
```

### **Passo 3: Executar**

```bash
python manage.py runserver
```

### **Passo 4: Acessar**

- 🌐 Site: http://127.0.0.1:8000
- 🔌 API: http://127.0.0.1:8000/api/
- 🔐 Admin: http://127.0.0.1:8000/admin/

---

## 📋 Endpoints Disponíveis

### Alunos

```javascript
GET    /api/alunos/                    // Listar
POST   /api/alunos/                    // Criar
GET    /api/alunos/por_turma/?turma_id=1
GET    /api/alunos/por_escola/?escola_id=1
```

### Pagamentos

```javascript
GET    /api/pagamentos/
POST   /api/pagamentos/
GET    /api/pagamentos/por_mes_ano/?mes=6&ano=2026
```

### Cursos, Turmas, Bolsas, Escolas, Usuários

```javascript
GET    /api/cursos/
GET    /api/turmas/
GET    /api/bolsas/
GET    /api/escolas/
GET    /api/usuarios/
// ... mesmas operações para todos
```

---

## 💻 Exemplos de Código

### Listar alunos (JavaScript)

```javascript
const alunos = await axios.get("/api/alunos/");
console.log(alunos.data);
```

### Criar aluno

```javascript
await axios.post("/api/alunos/", {
  nome: "João Silva",
  numero_aluno: 42,
  id_turma: 1,
  id_escola: 1,
  estado: "ACTIVO",
});
```

### Registar pagamento

```javascript
await axios.post("/api/pagamentos/", {
  id_aluno: 1,
  mes: 6,
  ano: 2026,
  valor_propina: 15000,
  valor_pago: 15000,
  data_pagamento: "2026-06-15",
});
```

### Usar Classe SigepAPI

```javascript
// Pré-configurada em api.js
const alunos = await api.obterAlunos();
const pagamentos = await api.obterPagamentosMesAno(6, 2026);
await api.criarAluno({ ... });
```

---

## 📦 Arquivos Implementados

```
✅ home/models.py                 (9 modelos)
✅ home/serializers.py            (9 serializers)
✅ home/api_views.py              (9 viewsets)
✅ home/urls.py                   (configurado com DRF)
✅ home/static/js/api.js          (classe SigepAPI)
✅ home/templates/alunos.html     (dinâmico)
✅ home/templates/cursos.html     (dinâmico)
✅ home/templates/pagamentos.html (dinâmico)
✅ sigep/settings.py              (DRF + CORS)
✅ requirements.txt               (atualizadas)
✅ setup.ps1                       (script setup Windows)
✅ setup.sh                        (script setup Linux)
✅ API_README.md                   (doc completa)
✅ QUICK_START.md                  (guia rápido)
✅ SETUP.md                        (instrções)
```

---

## 🔌 Como Conectar ao Supabase

Na sua DATABASE_URL no `.env`:

```env
DATABASE_URL=postgresql://postgres:SuaSenha@db.SuaRegiao.supabase.co:5432/postgres
```

As tabelas serão criadas automaticamente pelo Django com `python manage.py migrate`

---

## ⚡ Funcionalidades

| Funcionalidade       | Status          |
| -------------------- | --------------- |
| CRUD Alunos          | ✅ Completo     |
| CRUD Cursos          | ✅ Completo     |
| CRUD Turmas          | ✅ Completo     |
| CRUD Pagamentos      | ✅ Completo     |
| CRUD Escolas         | ✅ Completo     |
| Filtros Avançados    | ✅ Implementado |
| Templates Dinâmicos  | ✅ 3 templates  |
| Classe JS Utilitária | ✅ SigepAPI     |
| Paginação            | ✅ Configurada  |
| CORS                 | ✅ Ativo        |
| Admin Django         | ✅ Disponível   |

---

## 🎨 Fluxo de Uma Requisição

```
1. Usuário clica em "Novo Aluno"
   ↓
2. JavaScript abre modal
   ↓
3. Usuário preenche formulário
   ↓
4. JavaScript (axios) faz POST /api/alunos/
   ↓
5. Django processa request
   ↓
6. Serializer valida dados
   ↓
7. Model salva no Supabase PostgreSQL
   ↓
8. Response volta com status 201 e dados
   ↓
9. JavaScript atualiza tabela dinâmicamente
   ↓
10. Usuário vê novo aluno na lista
```

---

## 🔒 Segurança

**⚠️ Antes de Produção:**

- [ ] Alterar `SECRET_KEY` para valor seguro
- [ ] Configurar `DEBUG = False`
- [ ] Usar HTTPS
- [ ] Definir `ALLOWED_HOSTS` específicos
- [ ] Restringir CORS origins
- [ ] Implementar autenticação de usuário
- [ ] Adicionar rate limiting

---

## 📞 Suporte Rápido

| Problema           | Solução                         |
| ------------------ | ------------------------------- |
| API retorna 404    | URL deve ter `/api/` no final   |
| CORS Error         | Verifique CORS_ALLOWED_ORIGINS  |
| BD não conecta     | Verifique DATABASE_URL          |
| Dados não aparecem | Veja console do navegador (F12) |

---

## 🎓 Próximos Passos Opcionais

1. **Autenticação**: Implementar login de usuários
2. **Relatórios**: Exportar dados para CSV/PDF
3. **Gráficos**: Adicionar dashboard com Chart.js
4. **Notificações**: Alertas para atrasos
5. **Mobile**: Fazer versão mobile-responsiva
6. **Testes**: Adicionar testes unitários

---

## 📚 Documentação Disponível

- `QUICK_START.md` - Guia rápido (👈 COMECE AQUI)
- `API_README.md` - Documentação completa da API
- `SETUP.md` - Instruções detalhadas de configuração
- `setup.ps1` - Script automatizado (Windows)
- `setup.sh` - Script automatizado (Linux/Mac)

---

## 🎉 Resultado Final

**✅ Uma API REST totalmente funcional que:**

- ✅ Conecta ao seu Supabase PostgreSQL
- ✅ Disponibiliza todos os dados via endpoints
- ✅ Permite CRUD completo
- ✅ É consumida dinamicamente pelos templates
- ✅ Está pronta para produção com ajustes
- ✅ Pode ser usada por mobile apps também

---

## 🚀 Comece Agora!

```bash
# 1. Execute o setup
powershell -ExecutionPolicy Bypass -File setup.ps1

# 2. Configure o .env com sua DATABASE_URL

# 3. Inicie o servidor
python manage.py runserver

# 4. Acesse http://127.0.0.1:8000
```

**Pronto! Sua API REST está viva! 🎊**

---

_Criado com ❤️ para SIGEP - Sistema de Gestão de Escolas_
