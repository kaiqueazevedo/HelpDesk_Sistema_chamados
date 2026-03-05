(() => {
  const API = "http://127.0.0.1:5000/chamados";

  async function carregarChamados() {
    try {
      const response = await fetch(API);
      const chamados = await response.json();
      const lista = document.getElementById("listaChamados");
      lista.innerHTML = "";

      chamados.forEach(chamado => {
        lista.innerHTML += `
          <div class="card">
            <h3>${chamado.titulo}</h3>
            <p>${chamado.descricao}</p>
            <p class="status ${chamado.status}">Status: ${chamado.status}</p>
            ${chamado.status === "aberto" ? 
              `<button onclick="fecharChamado(${chamado.id})">Fechar chamado</button>` : ""}
          </div>
        `;
      });
    } catch (err) {
      console.error("Erro ao carregar chamados:", err);
      const msg = document.getElementById("mensagem");
      if (msg) msg.innerText = "Erro ao carregar chamados!";
    }
  }

  async function criarChamado() {
    const titulo = document.getElementById("titulo").value.trim();
    const descricao = document.getElementById("descricao").value.trim();

    if (!titulo || !descricao) {
      const msg = document.getElementById("mensagem");
      if (msg) msg.innerText = "Preencha título e descrição!";
      return;
    }

    try {
      await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, descricao })
      });

      document.getElementById("titulo").value = "";
      document.getElementById("descricao").value = "";
      const msg = document.getElementById("mensagem");
      if (msg) msg.innerText = "Chamado criado com sucesso!";
      carregarChamados();
    } catch (err) {
      console.error("Erro ao criar chamado:", err);
      const msg = document.getElementById("mensagem");
      if (msg) msg.innerText = "Erro ao criar chamado!";
    }
  }

  async function fecharChamado(id) {
    try {
      await fetch(`${API}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: "fechado" })
      });
      carregarChamados();
    } catch (err) {
      console.error("Erro ao fechar chamado:", err);
      const msg = document.getElementById("mensagem");
      if (msg) msg.innerText = "Erro ao fechar chamado!";
    }
  }

  // Expõe funções para HTML
  window.criarChamado = criarChamado;
  window.fecharChamado = fecharChamado;

  // Carrega chamados ao iniciar
  carregarChamados();
})();