# ITSM Prometeus

Aplicação de consola para gestão de serviços de IT (ITSM — IT Service Management), desenvolvida em Python com persistência em PostgreSQL.

Permite a gestão de users, produtos, departamentos, categorias e tickets de suporte, com autenticação e permissões diferenciadas por perfil (Admin, Técnico, User).

---

## Funcionalidades

- **Autenticação** por email e password
- **Gestão de Users** — criar, editar, consultar e eliminar (Admin)
- **Gestão de Produtos** — criar, editar, consultar e eliminar (Admin)
- **Gestão de Departamentos e Categorias** — configuração do sistema (Admin)
- **Gestão de Tickets**:
  - Abertura de tickets por Users, com **atribuição automática** ao técnico com menos tickets activos
  - **Fila de trabalho por técnico**, ordenada por prioridade (Alta → Média → Baixa)
  - Fechar, reabrir e devolver tickets (com observação para o user)
- **Validação de dados** através de encapsulamento (`@property`) em todos os modelos
- **Tratamento de erros** centralizado, sem crashes em inputs inválidos
- **Testes automatizados** com `pytest` para as regras de validação

---

## Perfis e Permissões

| Acção                             | Admin         | Técnico               | User |
|---|---|---|---|
| Gerir departamentos e categorias  | ✅            | ❌                   | ❌ |
| Gerir users                       | ✅            | ❌                   | ❌ |
| Gerir produtos                    | ✅            | ❌                   | ❌ |
| Criar ticket                      | ✅            | ❌                   | ✅ |
| Consultar tickets                 | ✅ (todos)    | ✅ (próprios)        | ✅ (próprios) |
| Editar / Fechar / Reabrir ticket  | ✅            | ✅                   | ❌ |
| Devolver ticket (com observação)  | ❌            | ✅                   | ❌ |
| Eliminar ticket                   | ✅            | ❌                   | ❌ |

---

## Arquitectura

O projecto segue uma arquitectura em camadas, separando responsabilidades:

```
itsm_prometeus/
│
├── main.py                      # Ponto de entrada da aplicação
├── seed.py                      # Script de seeding (dados de teste)
├── requirements.txt             # Dependências do projecto
│
├── modules/
│   ├── ligar_db.py               # Ligação à base de dados PostgreSQL
│   ├── auth.py                   # Lógica de autenticação (login)
│   ├── seguranca.py              # Hash e verificação de passwords (PBKDF2)
│   ├── erros.py                  # Tratamento de erros e inputs seguros
│   ├── menus.py                  # Interface de consola (menus por perfil)
│   │
│   ├── users.py                  # Modelo User (com encapsulamento)
│   ├── produtos.py               # Modelo Produto
│   ├── tickets.py                # Modelo Ticket
│   ├── categorias.py             # Modelo Categoria
│   └── departamentos.py          # Modelo Departamento
│
├── repositorios/                 # Camada DAO — acesso à base de dados
│   ├── ddl.sql                   # Script de criação das tabelas (DDL)
│   ├── user_repo.py
│   ├── produto_repo.py
│   ├── ticket_repo.py
│   ├── categoria_repo.py
│   └── departamento_repo.py
│
└── tests/                        # Testes automatizados (pytest)
    ├── test_users.py
    ├── test_tickets.py
    └── test_seguranca.py
```

### Camadas

| Camada | Responsabilidade |
|---|---|
| **Modelos** (`modules/*.py`) | Representam os dados e validam-nos via `@property` |
| **Repositórios** (`repositorios/`) | Acesso à base de dados (CRUD) — padrão DAO |
| **Menus** (`modules/menus.py`) | Interface com o utilizador, por perfil |
| **Auth** (`modules/auth.py`, `modules/seguranca.py`) | Autenticação do user e hash das passwords |
| **Erros** (`modules/erros.py`) | Inputs seguros e tratamento de excepções |

---

## Modelo de Dados

```
departamentos ──< users >── tickets >── produtos
                              │
                          categorias
```

| Tabela | Descrição |
|---|---|
| `departamentos` | Departamentos da organização (IT, Suporte, RH, ...) |
| `categorias` | Categorias de tickets (Hardware, Software, Rede, ...) |
| `users` | Utilizadores do sistema, com `tipo` (admin/tecnico/user) |
| `produtos` | Equipamentos e produtos passíveis de gerar tickets |
| `tickets` | Pedidos de suporte, ligados a user, técnico, produto e categoria |

O script de criação das tabelas está em [`repositorios/ddl.sql`](./repositorios/ddl.sql).

---

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e em execução
- `pip` para gestão de pacotes

---

## Instalação

**1. Clonar o repositório e criar o ambiente virtual**
```bash
git clone <url-do-repositorio>
cd itsm_prometeus
python -m venv venv
```

**2. Activar o ambiente virtual**
```bash
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instalar as dependências**
```bash
pip install -r requirements.txt
```

**4. Criar a base de dados**

No PostgreSQL (via pgAdmin ou `psql`), cria uma base de dados chamada `itsm_prometeus` e corre o script das tabelas:
```bash
createdb -U postgres itsm_prometeus
psql -U postgres -d itsm_prometeus -f repositorios/ddl.sql
```

**5. Configurar a ligação à base de dados**

As credenciais não ficam no código: define a password da base de dados numa variável de ambiente antes de correr o programa.
```powershell
$env:ITSM_DB_PASSWORD = "a_tua_password"   # PowerShell
```
```bash
export ITSM_DB_PASSWORD="a_tua_password"   # bash
```
Opcionais (têm estes valores por omissão): `ITSM_DB_HOST=localhost`, `ITSM_DB_NAME=itsm_prometeus`, `ITSM_DB_USER=postgres`. O `modules/ligar_db.py` lê-as assim:
```python
import os

import psycopg

def get_connection():
    return psycopg.connect(
        host=os.environ.get("ITSM_DB_HOST", "localhost"),
        dbname=os.environ.get("ITSM_DB_NAME", "itsm_prometeus"),
        user=os.environ.get("ITSM_DB_USER", "postgres"),
        password=os.environ.get("ITSM_DB_PASSWORD"),
    )
```

**6. Popular a base de dados com dados de teste (opcional, mas recomendado)**

Cria departamentos, categorias, produtos, tickets e as contas de teste abaixo. Correr uma só vez, na pasta do projecto:
```bash
python seed.py
```

Sem o seed, a base de dados fica sem nenhum user e não há com quem entrar: é preciso inserir pelo menos um admin à mão.

---

## Como executar

```bash
python main.py
```

### Credenciais de teste (após correr o `seed.py`)

| Perfil | Email | Password |
|---|---|---|
| Admin | ana.silva@itsm.pt | admin123 |
| Técnico | bruno.costa@itsm.pt | tecnico123 |
| Técnico | carla.mendes@itsm.pt | tecnico456 |
| User | david.lopes@itsm.pt | user123 |
| User | eva.martins@itsm.pt | user456 |

As passwords são guardadas com hash (PBKDF2-SHA256 com salt, em `modules/seguranca.py`), nunca em texto simples. Contas antigas que ainda tenham a password em texto simples passam a hash no primeiro login.

---

## Testes Automatizados

O projecto inclui testes com `pytest` para as regras de encapsulamento dos modelos `User` e `Ticket` e para o hash das passwords. Não precisam da base de dados.

```bash
pytest tests/ -v
```

Os testes cobrem:
- Validação de email, contacto, tipo, turno e password (`User`)
- Validação de estado e prioridade (`Ticket`)
- Comportamento correcto na criação e edição de objectos
- Hash das passwords: o hash não contém a password, salt diferente em cada hash, password certa aceite e errada rejeitada, e as passwords antigas em texto simples continuam a funcionar (`seguranca.py`)

---

## Tratamento de Erros

A aplicação está protegida contra:
- **Inputs inválidos** (ex: letras onde se espera um número) — através de `input_inteiro()`
- **Erros de validação dos modelos** (`ValueError`) — através de `executar()`, que apanha o erro e mantém o programa em execução
- **Erros inesperados** (ex: falhas de ligação à base de dados) — apanhados genericamente, sem crash

Toda esta lógica está centralizada em `modules/erros.py`.

---

## Decisões de Arquitectura

- **PostgreSQL com `psycopg[binary]`** em vez de `psycopg2`, devido a incompatibilidades do `psycopg2` com Python 3.14
- **`departamento` separado de `tipo`** no modelo `User` — o primeiro representa a unidade organizacional, o segundo o nível de permissões no sistema
- **Atribuição automática de técnicos** baseada no menor número de tickets activos, para distribuição equilibrada de carga de trabalho
- **Fila por prioridade** implementada com `CASE` em SQL, evitando lógica de ordenação no lado do Python
- **Encapsulamento nos modelos** (`@property`) garante que nenhum dado inválido chega à base de dados quando os objectos são correctamente construídos antes da chamada ao repositório

---

## Possíveis Melhorias Futuras

- Migração da interface de consola para uma API REST (Flask/FastAPI)
- Relatórios e métricas (tickets por categoria, tempo médio de resolução)
- Sistema de notificações para técnicos com novos tickets atribuídos
