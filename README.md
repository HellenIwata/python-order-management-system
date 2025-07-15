# Sistema de Gerenciamento de Clientes e Pedidos

Este é um projeto simples em Python de um sistema de gerenciamento que opera via linha de comando (CLI). Ele permite o cadastro e a manipulação de dados de clientes e seus respectivos pedidos.

O sistema foi desenvolvido como um exercício prático de Python, focando em manipulação de dicionários, funções, entrada e saída de dados e modularização de código.

**Atenção:** Os dados são armazenados em memória e serão perdidos ao fechar o programa.

---

## 🚀 Funcionalidades

O projeto é dividido em dois módulos principais:

### 👤 Gerenciamento de Clientes (`customers.py`)

- **Cadastrar Clientes:** Adiciona novos clientes ao sistema com nome, telefone, endereço e email.
- **Listar Clientes:** Exibe uma lista completa de todos os clientes cadastrados.
- **Buscar Clientes:** Permite a busca de clientes por nome, telefone ou email.
- **Atualizar Clientes:** Modifica as informações de um cliente já existente.

### 📦 Gerenciamento de Pedidos (`orders.py`)

- **Criar Pedidos:** Gera um novo pedido e o vincula a um cliente cadastrado.
- **Adicionar Múltiplos Itens:** Permite adicionar vários itens a um mesmo pedido, cada um com sua própria quantidade e valor unitário.
- **Calcular Subtotal e Total:** Calcula automaticamente o subtotal por item e o valor total do pedido.
- **Listar Pedidos:** Mostra todos os pedidos, detalhando o cliente, os itens, subtotais e valor total.
- **Buscar Pedidos:** Encontra pedidos que contenham um item específico.
- **Atualizar Pedidos:** Permite adicionar ou remover itens de um pedido existente.

---

## 🛠️ Como Executar

Para utilizar o sistema, você precisa ter o Python 3 instalado em sua máquina.

1.  Clone ou faça o download deste repositório.
2.  Navegue até a pasta do projeto pelo terminal.
3.  Você pode executar cada módulo de forma independente.

#### Para gerenciar clientes:

Execute o seguinte comando no seu terminal:
```bash
python customers.py
```

#### Para gerenciar pedidos:

Execute o seguinte comando no seu terminal:
```bash
python orders.py
```

Após executar o comando, um menu interativo aparecerá no console, guiando você através das opções disponíveis.

---

## 📂 Estrutura do Projeto

```
sistema-gerenciamento-pedidos/
├── customers.py     # Contém toda a lógica para o CRUD de clientes.
└── orders.py        # Contém toda a lógica para o CRUD de pedidos.
```

---

## 💡 Melhorias Futuras

- [ ] **Persistência de Dados:** Implementar a gravação e leitura dos dados em arquivos (como JSON ou CSV) ou em um banco de dados (como SQLite) para que as informações não se percam.
- [ ] **Menu Principal Unificado:** Criar um arquivo `main.py` que sirva como ponto de entrada único para o sistema, permitindo ao usuário escolher entre gerenciar clientes ou pedidos.
- [ ] **Refatoração para POO:** Migrar a estrutura baseada em dicionários para Programação Orientada a Objetos, utilizando classes `Customer` e `Order`.
- [ ] **Implementar Exclusão:** Adicionar a funcionalidade para remover clientes e pedidos.
- [ ] **Melhorar Validação de Dados:** Aprimorar as validações de entrada do usuário para evitar erros.