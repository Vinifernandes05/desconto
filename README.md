# 💼💻 Sistema de Descontos em Pedidos

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de um sistema de cálculo de descontos aplicados a pedidos, permitindo **criar pedidos com diferentes tipos de desconto** e **listar pedidos registrados** de forma estruturada.

A aplicação foi construída em **Python** com foco em **Clean Architecture**, aplicando conceitos como **separação de responsabilidades em camadas, programação orientada a objetos, abstração, interfaces, Strategy Pattern e uso de DTOs (Data Transfer Objects)**.

Além disso, o projeto possui **persistência em memória**, **validação de tipos de desconto** e **padrões de design para desacoplamento entre camadas**.

---

## 🎯 Objetivos do Projeto

- Praticar Clean Architecture em Python
- Implementar cálculo de descontos com Strategy Pattern
- Aplicar abstração e polimorfismo via interfaces (ABC)
- Separar responsabilidades em camadas (Entidades, Casos de Uso, Adaptadores, Gateways, Frameworks, Presenters)
- Utilizar DTOs para transferência de dados entre camadas
- Desacoplar lógica de negócio da infraestrutura de persistência

---

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

### 🔹 Linguagem
- Python

### 🔹 Conceitos Aplicados
- Clean Architecture (arquitetura em camadas)
- Strategy Pattern (padrão de projeto para descontos)
- Abstração (Classes abstratas com ABC)
- Polimorfismo
- Encapsulamento
- DTOs (Data Transfer Objects)

### 🔹 Outros
- Git
- GitHub

---

## ⚙️ Funcionalidades

✔️ Criação de pedidos com cálculo automático de desconto  
✔️ Três tipos de desconto: Normal (10%), VIP (20%), Premium (30%)  
✔️ Listagem de todos os pedidos registrados  
✔️ Validação do tipo de desconto (lança erro para tipos inválidos)  
✔️ Exibição formatada dos resultados via Presenter

---

## 💰 Regras de Desconto

| Tipo de Desconto | Percentual |
|-------------------|------------|
| Normal | 10% |
| Premium | 30% |
| VIP | 20% |

---

## 📂 Estrutura do Projeto

```bash
DESCONTO
│
├── main.py                              # Ponto de entrada da aplicação
│
├── desconto_app/
│   └── src/
│       ├── app/
│       │   ├── adapters/
│       │   │   ├── controllers/
│       │   │   │   └── pedido_controller.py    # Controller (entrada da API)
│       │   │   └── repositories/
│       │   │       └── memory_pedido_repository.py  # Implementação do repositório em memória
│       │   │
│       │   ├── dtos/
│       │   │   ├── criar_pedido_input_dto.py   # DTO de entrada (dados para criar pedido)
│       │   │   └── criar_pedido_output_dto.py  # DTO de saída (resultado da criação)
│       │   │
│       │   ├── entities/
│       │   │   ├── desconto.py                 # Interface IDesconto + classes concretas de desconto
│       │   │   └── pedido.py                   # Entidade Pedido
│       │   │
│       │   ├── frameworks/
│       │   │   └── database/
│       │   │       ├── connection.py            # Conexão de banco (não utilizada)
│       │   │       └── memory_database.py       # Banco de dados em memória
│       │   │
│       │   ├── gateways/
│       │   │   └── pedido_gateway.py            # Interface abstrata do repositório
│       │   │
│       │   ├── presenters/
│       │   │   └── pedido_presenter.py          # Formatação dos dados para exibição
│       │   │
│       │   └── use_cases/
│       │       └── criar_pedido.py              # Caso de uso de criação e listagem de pedidos
│       │
│       └── services/
│           └── pedido_service.py                # Serviço alternativo (não utilizado no main)
│
├── .gitignore
└── README.md
```

---

## 🔄 Fluxo da Aplicação

1. `main.py` inicializa todas as dependências (Database, Repository, UseCase, Controller, Presenter)
2. O **PedidoController** recebe os dados para criação do pedido
3. O Controller monta um **CriarPedidoInputDTO** e delega ao caso de uso **CriarPedido**
4. O **CriarPedido** valida o tipo de desconto, cria a entidade **Pedido** com a estratégia correta
5. O **MemoryPedidoRepository** salva o pedido no **MemoryDatabase** (lista em memória)
6. Um **CriarPedidoOutputDTO** é retornado ao Controller
7. O **PedidoPresenter** formata o DTO em um dicionário para exibição
8. O resultado é impresso no console

---

## 🏗️ Conceitos de Arquitetura Aplicados

### 🔹 Clean Architecture
- Separação clara entre **domínio** (entities), **casos de uso** (use_cases), **adaptadores** (controllers, repositories), **gateways** e **frameworks** (database)

### 🔹 Strategy Pattern
- A interface `IDesconto` define um contrato para cálculo de desconto
- Cada tipo de desconto (`DescontoNormal`, `DescontoVIP`, `DescontoPremium`) implementa a estratégia de cálculo de forma independente

### 🔹 Abstração
- `IDesconto` e `IPedidoGateway` são classes abstratas (ABC) que definem contratos
- As implementações concretas são injetadas via dependência

### 🔹 Polimorfismo
- O método `calcular()` é implementado de forma diferente em cada classe de desconto
- O Pedido utiliza qualquer implementação de `IDesconto` de forma transparente

### 🔹 Encapsulamento
- Atributos das entidades e DTOs são encapsulados dentro das classes
- Cada camada expõe apenas o necessário

### 🔹 DTOs (Data Transfer Objects)
- `CriarPedidoInputDTO` transporta dados de entrada entre o Controller e o UseCase
- `CriarPedidoOutputDTO` transporta dados de saída entre o UseCase e o Presenter

### 🔹 Dependency Injection
- As dependências são injetadas nos construtores (ex: `MemoryPedidoRepository` recebe `MemoryDatabase`)

---

## 📞 Contato

👤 **Vinicius Sousa Fernandes**

- 📧 Email: vinifernandes2005@gmail.com
- 💼 LinkedIn: https://linkedin.com/in/viniciussousaf
- 💻 GitHub: https://github.com/Vinifernandes05
