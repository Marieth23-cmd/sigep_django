const buttons = document.querySelectorAll(".tab-btn");
const contents = document.querySelectorAll(".tab-content");

// Restaurar a aba ativa após reload
function restoreActiveTab() {
  const savedTab = localStorage.getItem("activeTab") || "inicio";
  
  buttons.forEach((b) => b.classList.remove("active"));
  contents.forEach((c) => c.classList.remove("active"));
  
  const activeBtn = document.querySelector(`[data-tab="${savedTab}"]`);
  if (activeBtn) {
    activeBtn.classList.add("active");
  }
  
  const activeContent = document.getElementById(savedTab);
  if (activeContent) {
    activeContent.classList.add("active");
  }
}

// Função para abrir abas nas configurações
function abrirTab(event, tabName) {
  event.preventDefault();
  
  // Remove classe active de todos os tab-pane
  const panes = document.querySelectorAll(".tab-pane");
  panes.forEach((pane) => pane.classList.remove("active"));
  
  // Remove classe active de todos os botões de configurações
  const configBtns = document.querySelectorAll(".configuracoes-tabs .tab-btn");
  configBtns.forEach((btn) => btn.classList.remove("active"));
  
  // Adiciona classe active ao pane selecionado
  const selectedPane = document.getElementById(tabName);
  if (selectedPane) {
    selectedPane.classList.add("active");
  }
  
  // Adiciona classe active ao botão clicado
  event.target.closest(".tab-btn").classList.add("active");
  
  // Salva a aba ativa
  localStorage.setItem("activeConfigTab", tabName);
}

// Editar utilizador - abre modal
function editarUtilizador(userId) {
  const modal = document.getElementById("modal-editar");
  modal.style.display = "flex";
  
  // Guardar o ID do utilizador sendo editado
  modal.dataset.userId = userId;
  
  // Preencher formulário com dados atuais
  const userCard = document.getElementById(`user-${userId}`);
  const nome = userCard.querySelector("h4").textContent;
  const email = userCard.querySelector("p").textContent;
  
  document.getElementById("edit-nome").value = nome;
  document.getElementById("edit-email").value = email;
  document.getElementById("edit-senha").value = "";
  document.getElementById("edit-senha-confirm").value = "";
}

// Fechar modal
function fecharModal(event) {
  if (event && event.target.id !== "modal-editar") return;
  
  const modal = document.getElementById("modal-editar");
  modal.style.display = "none";
  
  // Limpar formulário
  document.getElementById("edit-nome").value = "";
  document.getElementById("edit-email").value = "";
  document.getElementById("edit-senha").value = "";
  document.getElementById("edit-senha-confirm").value = "";
}

// Salvar alterações do utilizador
function salvarUtilizador() {
  const modal = document.getElementById("modal-editar");
  const userId = modal.dataset.userId;
  
  const nome = document.getElementById("edit-nome").value;
  const email = document.getElementById("edit-email").value;
  const senha = document.getElementById("edit-senha").value;
  const senhaConfirm = document.getElementById("edit-senha-confirm").value;
  
  // Validação básica
  if (!nome || !email) {
    alert("Nome e email são obrigatórios!");
    return;
  }
  
  if (senha && senha !== senhaConfirm) {
    alert("As senhas não coincidem!");
    return;
  }
  
  if (senha && senha.length < 6) {
    alert("Senha deve ter pelo menos 6 caracteres!");
    return;
  }
  
  // Atualizar card do utilizador
  const userCard = document.getElementById(`user-${userId}`);
  userCard.querySelector("h4").textContent = nome;
  userCard.querySelector("p").textContent = email;
  
  // Aqui você enviaria os dados para o servidor (POST/PUT)
  console.log("Dados para salvar:", { userId, nome, email, senha });
  
  alert("Utilizador atualizado com sucesso!");
  fecharModal();
}

// Restaurar aba de configurações ao carregar
document.addEventListener("DOMContentLoaded", function() {
  restoreActiveTab();
  
  // Atualizar título do header
  updateHeaderTitle();
  
  // Restaurar aba de configurações se existir
  const savedConfigTab = localStorage.getItem("activeConfigTab") || "geral";
  const savedPane = document.getElementById(savedConfigTab);
  if (savedPane) {
    const panes = document.querySelectorAll(".tab-pane");
    panes.forEach((pane) => pane.classList.remove("active"));
    savedPane.classList.add("active");
    
    // Destacar botão correspondente
    const configBtns = document.querySelectorAll(".configuracoes-tabs .tab-btn");
    configBtns.forEach((btn) => btn.classList.remove("active"));
    
    const btnIndex = Array.from(document.querySelectorAll(".tab-pane")).indexOf(savedPane);
    if (configBtns[btnIndex]) {
      configBtns[btnIndex].classList.add("active");
    }
  }
  
  // Dropdown menu
  setupDropdownMenu();
  // Renderizar gráfico de relatórios ao carregar
  renderRelatoriosChart();
});

// Mapa de títulos das páginas
const pageTitles = {
  "inicio": "Início",
  "gestao-geral": "Gestão Geral",
  "alunos": "Alunos",
  "cursos": "Cursos",
  "turmas": "Turmas",
  "pagamentos": "Pagamentos",
  "relatorios": "Relatórios",
  "configuracoes": "Configurações"
};

// Atualizar título do header dinamicamente
function updateHeaderTitle() {
  const activeContent = document.querySelector(".tab-content.active");
  if (activeContent && activeContent.id) {
    const title = pageTitles[activeContent.id] || "Início";
    const pageTitle = document.getElementById("page-title");
    if (pageTitle) {
      pageTitle.textContent = title;
    }
  }
}

// Setup do dropdown menu (opcional, já funciona com hover no CSS)
function setupDropdownMenu() {
  const userProfile = document.querySelector(".user-profile");
  const dropdownMenu = document.querySelector(".dropdown-menu");
  
  if (!userProfile || !dropdownMenu) return;
  
  userProfile.addEventListener("click", function(e) {
    if (e.target.closest(".dropdown-menu")) return;
    dropdownMenu.style.display = dropdownMenu.style.display === "flex" ? "none" : "flex";
  });
  
  // Fechar dropdown ao clicar fora
  document.addEventListener("click", function(e) {
    if (!e.target.closest(".user-profile")) {
      dropdownMenu.style.display = "none";
    }
  });
  
  // Logout
  const logoutBtn = document.querySelector(".dropdown-item.logout");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", function(e) {
      e.preventDefault();
      if (confirm("Tem a certeza que deseja sair?")) {
        // Aqui você redirecionaria para logout
        alert("Funcionalidade de logout a ser implementada");
      }
    });
  }
}

// Renderizar gráfico de relatórios (Receita Esperada vs Real) em HTML
function renderRelatoriosChart() {
  const data = [
    { mes: "Jan", esperada: 10.2, real: 8.9 },
    { mes: "Fev", esperada: 10.5, real: 9.4 },
    { mes: "Mar", esperada: 11.0, real: 9.1 },
    { mes: "Abr", esperada: 11.3, real: 10.0 },
    { mes: "Mai", esperada: 11.8, real: 10.6 },
    { mes: "Jun", esperada: 12.0, real: 10.3 },
  ];

  const placeholder = document.querySelector('.chart-placeholder');
  if (!placeholder) return;

  // limpar conteúdo atual
  placeholder.innerHTML = '';

  // encontrar maior valor para normalizar alturas
  const max = Math.max(...data.map(d => Math.max(d.esperada, d.real)));

  data.forEach(d => {
    const group = document.createElement('div');
    group.className = 'chart-bar-group';

    const bars = document.createElement('div');
    bars.className = 'bars';

    const barEsperada = document.createElement('div');
    barEsperada.className = 'bar esperada';
    const hE = Math.round((d.esperada / max) * 100);
    barEsperada.style.height = hE + '%';
    barEsperada.setAttribute('data-value', d.esperada);

    const barReal = document.createElement('div');
    barReal.className = 'bar real';
    const hR = Math.round((d.real / max) * 100);
    barReal.style.height = hR + '%';
    barReal.setAttribute('data-value', d.real);

    bars.appendChild(barEsperada);
    bars.appendChild(barReal);

    const label = document.createElement('span');
    label.textContent = d.mes;

    group.appendChild(bars);
    group.appendChild(label);

    placeholder.appendChild(group);
  });
}

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    buttons.forEach((b) => b.classList.remove("active"));

    contents.forEach((c) => c.classList.remove("active"));

    btn.classList.add("active");

    const tab = btn.dataset.tab;
    
    // Salvar a aba ativa no localStorage
    localStorage.setItem("activeTab", tab);

    document.getElementById(tab).classList.add("active");
    
    // Atualizar título do header
    updateHeaderTitle();
    // Renderizar gráfico se for a aba de relatórios
    if (tab === 'relatorios') renderRelatoriosChart();
  });
});


window.addEventListener('load', () => {
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        preloader.style.opacity = '0';
        setTimeout(() => preloader.style.display = 'none', 500);
    }, 1500);
});