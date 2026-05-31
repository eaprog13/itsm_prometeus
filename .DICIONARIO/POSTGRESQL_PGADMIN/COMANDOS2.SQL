# 🧠 MySQL + phpMyAdmin Cheat Sheet (COMPLETO COM COMENTÁRIOS DETALHADOS)

---

# 🗄️ BANCO DE DADOS


CREATE DATABASE nome_db; -- cria um novo banco de dados no servidor MySQL, usado para armazenar tabelas e dados de uma aplicação
DROP DATABASE nome_db; -- remove permanentemente um banco de dados inteiro, incluindo todas as tabelas e dados (operação irreversível)
SHOW DATABASES; -- lista todos os bancos de dados existentes no servidor MySQL ao qual o utilizador tem acesso
USE nome_db; -- seleciona um banco de dados específico para que todas as queries seguintes sejam executadas dentro dele


---

# 📋 TABELAS

sql
CREATE TABLE usuarios ( -- cria uma nova tabela chamada usuarios onde serão armazenados registros
    id INT AUTO_INCREMENT PRIMARY KEY, -- cria um identificador único que aumenta automaticamente a cada novo registo
    nome VARCHAR(100), -- campo de texto para armazenar o nome do utilizador com limite de 100 caracteres
    email VARCHAR(150), -- campo de texto para armazenar o email do utilizador com limite de 150 caracteres
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- guarda automaticamente a data e hora em que o registo foi criado
);

DROP TABLE usuarios; -- elimina completamente a tabela e todos os dados dentro dela
SHOW TABLES; -- mostra todas as tabelas existentes dentro do banco de dados selecionado
DESCRIBE usuarios; -- mostra a estrutura completa da tabela (colunas, tipos de dados e restrições)


--

# ➕ INSERT (INSERIR DADOS)


INSERT INTO usuarios (nome, email) -- define em quais colunas os dados serão inseridos
VALUES ('João', 'joao@email.com'); -- insere os valores correspondentes nas colunas especificadas

---

# 🔍 SELECT (CONSULTAR DADOS)

SELECT * FROM usuarios; -- seleciona todos os registos e todas as colunas da tabela
SELECT nome, email FROM usuarios; -- seleciona apenas colunas específicas, melhorando performance
SELECT * FROM usuarios WHERE id = 1; -- filtra e retorna apenas o registo cujo id seja igual a 1

---

# ✏️ UPDATE (ATUALIZAR DADOS)

UPDATE usuarios -- indica qual tabela será atualizada
SET nome = 'João Silva' -- define o novo valor para a coluna selecionada
WHERE id = 1; -- define a condição que identifica qual registo será atualizado (essencial para evitar alterações em massa)

---

# ❌ DELETE (APAGAR DADOS)

DELETE FROM usuarios -- indica a tabela de onde os dados serão removidos
WHERE id = 1; -- define exatamente qual registo será apagado para evitar eliminar todos os dados

---

# 🔎 FILTROS E ORDENAÇÃO

SELECT * FROM usuarios
WHERE nome LIKE 'Jo%' -- pesquisa nomes que começam com "Jo" usando padrão de texto
ORDER BY nome ASC; -- ordena os resultados em ordem crescente (A-Z)

SELECT * FROM usuarios
ORDER BY id DESC; -- ordena os resultados do maior para o menor id

SELECT * FROM usuarios
LIMIT 10; -- limita a consulta aos primeiros 10 registos retornados

---

# 🔗 JOINS (RELACIONAR TABELAS)

SELECT pedidos.id, usuarios.nome
FROM pedidos
INNER JOIN usuarios ON pedidos.usuario_id = usuarios.id; -- junta tabelas e retorna apenas registos que existem em ambas as tabelas

SELECT usuarios.nome, pedidos.id
FROM usuarios
LEFT JOIN pedidos ON usuarios.id = pedidos.usuario_id; -- retorna todos os utilizadores mesmo que não tenham pedidos associados

---

# 🔢 FUNÇÕES SQL

SELECT COUNT(*) FROM usuarios; -- conta o número total de registos na tabela
SELECT SUM(valor) FROM pedidos; -- soma todos os valores de uma coluna numérica
SELECT AVG(valor) FROM pedidos; -- calcula a média dos valores
SELECT MAX(valor) FROM pedidos; -- devolve o maior valor encontrado
SELECT MIN(valor) FROM pedidos; -- devolve o menor valor encontrado

---

# 🧱 ALTER TABLE

ALTER TABLE usuarios ADD idade INT; -- adiciona uma nova coluna à tabela existente
ALTER TABLE usuarios DROP COLUMN idade; -- remove uma coluna da tabela
ALTER TABLE usuarios MODIFY nome VARCHAR(200); -- altera o tipo ou tamanho de uma coluna existente

---

# 🔐 USUÁRIOS E PERMISSÕES

CREATE USER 'user'@'localhost' IDENTIFIED BY 'senha'; -- cria um novo utilizador com acesso local ao MySQL
GRANT ALL PRIVILEGES ON nome_db.* TO 'user'@'localhost'; -- concede todas as permissões ao utilizador sobre um banco específico
FLUSH PRIVILEGES; -- recarrega as permissões para que as alterações tenham efeito imediato

---

# 🧰 phpMyAdmin (USO DETALHADO)

## ⌨️ Atalhos úteis

* Ctrl + Enter → executa a query SQL atual no editor
* Ctrl + Space → ativa autocompletar de tabelas, colunas e comandos SQL
* Ctrl + / → comenta uma linha de código SQL

## 🖱️ Funcionalidades da interface

* SQL → área onde se escrevem e executam queries manualmente
* Browse / Procurar → visualização dos dados armazenados na tabela (SELECT gráfico)
* ✏️ Editar → permite alterar um registo existente diretamente na interface
* ❌ Apagar → remove um registo específico da tabela
* 📥 Exportar → permite descarregar base de dados ou tabela em formatos como SQL, CSV ou JSON
* 📤 Importar → permite carregar ficheiros SQL para dentro do banco de dados

---

# ⚠️ BOAS PRÁTICAS IMPORTANTES

SELECT * FROM usuarios; -- usado apenas para testes e desenvolvimento, pode ser pesado em produção

-- sempre utilizar WHERE em UPDATE e DELETE para evitar alterações ou eliminações acidentais de todos os dados

---

# 🚀 RESUMO FINAL

✔ Criação e gestão de bases de dados
✔ Criação e manipulação de tabelas
✔ CRUD completo (Create, Read, Update, Delete)
✔ Filtros e ordenação avançada
✔ Joins entre tabelas
✔ Funções agregadas
✔ Gestão de utilizadores e permissões
✔ Utilização prática do phpMyAdmin
