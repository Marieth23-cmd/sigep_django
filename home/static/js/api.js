/**
 * Utilitários para comunicação com a API SIGEP
 */

// Use global API_BASE se definido no template (base.html), caso contrário fallback
const API_BASE_URL = (window && window.API_BASE) ? window.API_BASE : '/api/';

// Configurar axios para CSRF e requisições AJAX globalmente
if (typeof axios !== 'undefined') {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}

/**
 * Classe para gerenciar requisições à API
 */
class SigepAPI {
    constructor(baseURL = API_BASE_URL) {
        this.baseURL = baseURL;
        this.axios = axios;
    }

    /**
     * GET - Obter lista de recursos
     */
    async obter(endpoint, params = {}) {
        try {
            const response = await this.axios.get(`${this.baseURL}${endpoint}/`, { params });
            return response.data.results || response.data;
        } catch (error) {
            console.error(`Erro ao obter ${endpoint}:`, error);
            throw error;
        }
    }

    /**
     * POST - Criar novo recurso
     */
    async criar(endpoint, dados) {
        try {
            const response = await this.axios.post(`${this.baseURL}${endpoint}/`, dados);
            return response.data;
        } catch (error) {
            console.error(`Erro ao criar ${endpoint}:`, error);
            throw error;
        }
    }

    /**
     * PUT - Atualizar recurso completo
     */
    async atualizar(endpoint, id, dados) {
        try {
            const response = await this.axios.put(`${this.baseURL}${endpoint}/${id}/`, dados);
            return response.data;
        } catch (error) {
            console.error(`Erro ao atualizar ${endpoint}:`, error);
            throw error;
        }
    }

    /**
     * PATCH - Atualizar recurso parcial
     */
    async atualizarParcial(endpoint, id, dados) {
        try {
            const response = await this.axios.patch(`${this.baseURL}${endpoint}/${id}/`, dados);
            return response.data;
        } catch (error) {
            console.error(`Erro ao atualizar parcialmente ${endpoint}:`, error);
            throw error;
        }
    }

    /**
     * DELETE - Deletar recurso
     */
    async deletar(endpoint, id) {
        try {
            await this.axios.delete(`${this.baseURL}${endpoint}/${id}/`);
            return true;
        } catch (error) {
            console.error(`Erro ao deletar ${endpoint}:`, error);
            throw error;
        }
    }

    /**
     * Métodos específicos para cada entidade
     */

    // ESCOLAS
    async obterEscolas() {
        return this.obter('escolas');
    }

    async obterEscola(id) {
        const response = await this.axios.get(`${this.baseURL}escolas/${id}/`);
        return response.data;
    }

    async criarEscola(dados) {
        return this.criar('escolas', dados);
    }

    async atualizarEscola(id, dados) {
        return this.atualizar('escolas', id, dados);
    }

    // USUARIOS
    async obterUsuarios() {
        return this.obter('usuarios');
    }

    async obterUsuariosPorEscola(escolaId) {
        return this.obter('usuarios/por_escola', { escola_id: escolaId });
    }

    async criarUsuario(dados) {
        return this.criar('usuarios', dados);
    }

    // CURSOS
    async obterCursos() {
        return this.obter('cursos');
    }

    async obterCursosPorEscola(escolaId) {
        return this.obter('cursos/por_escola', { escola_id: escolaId });
    }

    async criarCurso(dados) {
        return this.criar('cursos', dados);
    }

    // TURMAS
    async obterTurmas() {
        return this.obter('turmas');
    }

    async obterTurmasPorEscola(escolaId) {
        return this.obter('turmas/por_escola', { escola_id: escolaId });
    }

    async criarTurma(dados) {
        return this.criar('turmas', dados);
    }

    // BOLSAS
    async obterBolsas() {
        return this.obter('bolsas');
    }

    async obterBolsasPorEscola(escolaId) {
        return this.obter('bolsas/por_escola', { escola_id: escolaId });
    }

    async criarBolsa(dados) {
        return this.criar('bolsas', dados);
    }

    // ALUNOS
    async obterAlunos() {
        return this.obter('alunos');
    }

    async obterAlunosPorEscola(escolaId) {
        return this.obter('alunos/por_escola', { escola_id: escolaId });
    }

    async obterAlunosPorTurma(turmaId) {
        return this.obter('alunos/por_turma', { turma_id: turmaId });
    }

    async criarAluno(dados) {
        return this.criar('alunos', dados);
    }

    // PAGAMENTOS
    async obterPagamentos() {
        return this.obter('pagamentos');
    }

    async obterPagamentosAluno(alunoId) {
        return this.obter('pagamentos/por_aluno', { aluno_id: alunoId });
    }

    async obterPagamentosMesAno(mes, ano) {
        return this.obter('pagamentos/por_mes_ano', { mes, ano });
    }

    async criarPagamento(dados) {
        return this.criar('pagamentos', dados);
    }

    // AUDITORIAS
    async obterAuditorias() {
        return this.obter('auditorias');
    }

    async obterAuditoriasUsuario(usuarioId) {
        return this.obter('auditorias/por_usuario', { usuario_id: usuarioId });
    }

    // CONFIGURACOES
    async obterConfiguracoes() {
        return this.obter('configuracoes');
    }

    async obterConfiguracaoEscola(escolaId) {
        return this.obter('configuracoes/por_escola', { escola_id: escolaId });
    }
}

// Instância global
const api = new SigepAPI();

/**
 * Funções utilitárias para UI
 */
function mostrarMensagem(elementId, mensagem, tipo = 'success') {
    const elemento = document.getElementById(elementId);
    if (elemento) {
        elemento.className = tipo;
        elemento.textContent = mensagem;
        elemento.style.display = 'block';
    }
}

function ocultarMensagem(elementId) {
    const elemento = document.getElementById(elementId);
    if (elemento) {
        elemento.style.display = 'none';
    }
}

function mostrarCarregamento(elementId) {
    const elemento = document.getElementById(elementId);
    if (elemento) {
        elemento.classList.add('active');
    }
}

function ocultarCarregamento(elementId) {
    const elemento = document.getElementById(elementId);
    if (elemento) {
        elemento.classList.remove('active');
    }
}

/**
 * Formatar data
 */
function formatarData(data) {
    const d = new Date(data);
    return d.toLocaleDateString('pt-PT');
}

/**
 * Formatar moeda
 */
function formatarMoeda(valor) {
    return new Intl.NumberFormat('pt-PT', { style: 'currency', currency: 'AOA' }).format(valor);
}
