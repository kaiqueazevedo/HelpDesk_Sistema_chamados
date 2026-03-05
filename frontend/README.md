#  HelpDesk - Sistema de Chamados

Sistema simples e moderno para **criação e gerenciamento de chamados**, desenvolvido com **Python (Flask) no backend** e **HTML, CSS e JavaScript no frontend**.

O objetivo do projeto é demonstrar a criação de uma **API REST + Interface Web responsiva**, permitindo criar e atualizar chamados de forma simples.

---

# Preview

Interface moderna com:

* layout futurista
* design responsivo
* cards dinâmicos
* atualização automática dos chamados

---

#  Tecnologias Utilizadas

### Backend

* Python
* Flask
* Flask-CORS

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

---

#  Estrutura do Projeto

```
helpdesk/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

---

#  Funcionalidades

✔ Criar chamado
✔ Listar chamados
✔ Alterar status para **fechado**
✔ Interface responsiva
✔ Comunicação com API REST
✔ Atualização dinâmica com JavaScript

---

#  Funcionamento

O sistema possui:

### API Backend

Endpoints disponíveis:

| Método | Endpoint      | Descrição               |
| ------ | ------------- | ----------------------- |
| GET    | /chamados     | Lista todos os chamados |
| POST   | /chamados     | Cria um chamado         |
| PUT    | /chamados/:id | Fecha um chamado        |

---

# Exemplo de Chamado

```
{
  "id": 1,
  "titulo": "Erro no sistema",
  "descricao": "Sistema não abre",
  "status": "aberto"
}
```

---

#  Como Executar o Projeto

## 1 Clonar Repositório

```
git clone https://github.com/seuusuario/helpdesk.git
```

---

## 2 Instalar dependências

```
pip install flask flask-cors
```

---

## 3 Rodar o backend

```
python app.py
```

Servidor iniciará em:

```
http://127.0.0.1:5000
```

---

##  Rodar o frontend

Abra o arquivo:

```
index.html
```

ou utilize:

```
python -m http.server
```

---

# Exemplo da Interface

Criar chamado:

```
Título
Descrição
[ Criar Chamado ]
```

Lista de chamados:

```
Chamado 1
Status: aberto
[ Fechar chamado ]
```

---

#  Interface

* Design moderno
* Layout responsivo
* Cards animados
* Feedback visual para status

---

#  Melhorias Futuras

* Sistema de login
* Usuários e permissões
* Banco de dados (PostgreSQL ou MySQL)
* Upload de anexos
* Sistema de comentários
* Dashboard com métricas
* Notificações

---

Desenvolvedor focado em:

* Automação com Python
* APIs REST
* Processamento de dados
* Sistemas Web

---

#  Objetivo do Projeto

Este projeto foi criado para:

* prática de **integração Frontend + Backend**
* desenvolvimento de **API REST**
* construção de **projetos para portfólio**
* aprendizado de **arquitetura web**

---


