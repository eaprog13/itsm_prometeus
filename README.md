# Plataforma de Gestão de Infraestruturas Informáticas

## Introdução

Este projeto consiste no desenvolvimento de uma plataforma para gestão de infraestruturas informáticas de uma organização.

O sistema permite:

- Registo e gestão de ativos (hardware e software)
- Criação e gestão de tickets de suporte
- Atribuição automática de técnicos com base em carga de trabalho, competências e disponibilidade

O objetivo é criar uma solução eficiente para centralizar a gestão de recursos e problemas técnicos.

---

## Objetivo do Projeto

Criar uma aplicação que permita:

- Gerir utilizadores do sistema
- Gerir inventário de hardware e software
- Criar, atribuir e encerrar tickets de suporte
- Otimizar a distribuição de trabalho entre técnicos

---

## Stack Tecnológico

### Backend
- Python 3.14
- Flask 3.1.2

### Base de Dados
- PostgreSQL 18

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Controlo de Versões
- Git
- GitHub

---

## Requisitos Funcionais

### Gestão de Utilizadores
- Criar utilizadores
- Gerir perfis de utilizador

### Gestão de Produtos
- Listar hardware
- Listar software
- Organizar inventário de ativos

### Gestão de Tickets
- Criar tickets de suporte
- Encerrar tickets
- Colocar tickets em fila de espera
- Atribuir automaticamente técnicos aos tickets com base em:
  - Carga de trabalho
  - Competências
  - Disponibilidade

---

## Requisitos Não-Funcionais

- O sistema deve responder num tempo aceitável (entre 5 segundos e 1 minuto)
- A base de dados deve garantir integridade e consistência dos dados
- Deve suportar múltiplos utilizadores em simultâneo
- Deve permitir possibilidade de backup da base de dados

---

## Diagramas

### Modelo Entidade-Relacionamento
*(A inserir posteriormente)*  
Diagrama que representa as relações entre utilizadores, tickets e produtos.

### Diagrama de Classes
*(A inserir posteriormente)*  
Representação da lógica do domínio e estrutura das classes principais do sistema.

---

## Stack Tecnológico (Resumo)

- Backend: Python + FastAPI  
- Base de Dados: PostgreSQL  
- Frontend: HTML, CSS, JavaScript + Bootstrap  
- Versionamento: Git + GitHub  

---

## Conclusão

Este projeto propõe a criação de uma aplicação para gestão de infraestruturas informáticas, permitindo a gestão de utilizadores, tickets e ativos (hardware e software).

Foi escolhida a stack Python + Flask devido à sua simplicidade e proximidade com a sintaxe em aprendizagem. O PostgreSQL foi selecionado por estar alinhado com o contexto académico da unidade de administração de bases de dados.

Inicialmente será utilizado Bootstrap para o frontend, com o objetivo de criar uma interface simples e funcional. Caso necessário, poderá ser substituído por uma aplicação em consola.

Este README representa uma primeira abordagem à definição de requisitos funcionais, não funcionais e arquitetura do sistema.
