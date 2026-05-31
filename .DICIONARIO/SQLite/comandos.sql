Comandos base de SQLite
Gestão da base de dados
sql
-- Criar/abrir base de dados (na linha de comandos)
sqlite3 minha_base.db

-- Ver bases de dados ligadas
.databases

-- Sair
.quit
Tabelas
sql
-- Criar tabela
CREATE TABLE utilizadores (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT    NOT NULL,
    email   TEXT    UNIQUE,
    idade   INTEGER
);

-- Ver tabelas existentes
.tables

-- Ver estrutura de uma tabela
.schema utilizadores

-- Apagar tabela
DROP TABLE IF EXISTS utilizadores;
CRUD
sql
-- INSERT
INSERT INTO utilizadores (nome, email, idade)
VALUES ('Ana Silva', 'ana@email.com', 30);

-- SELECT
SELECT * FROM utilizadores;
SELECT nome, email FROM utilizadores WHERE idade > 25;

-- UPDATE
UPDATE utilizadores
SET idade = 31
WHERE id = 1;

-- DELETE
DELETE FROM utilizadores WHERE id = 1;
Filtros e ordenação
sql
WHERE nome = 'Ana'          -- igualdade
WHERE idade BETWEEN 20 AND 40
WHERE nome LIKE 'A%'        -- começa por A
WHERE email IS NULL
ORDER BY nome ASC           -- ou DESC
LIMIT 10 OFFSET 20          -- paginação
Agregações
sql
SELECT COUNT(*)        FROM utilizadores;
SELECT AVG(idade)      FROM utilizadores;
SELECT MAX(idade)      FROM utilizadores;
SELECT MIN(idade)      FROM utilizadores;
SELECT SUM(idade)      FROM utilizadores;

-- Agrupar
SELECT cidade, COUNT(*) AS total
FROM utilizadores
GROUP BY cidade
HAVING total > 5;
Joins
sql
-- INNER JOIN
SELECT u.nome, p.titulo
FROM utilizadores u
INNER JOIN posts p ON p.user_id = u.id;

-- LEFT JOIN (inclui utilizadores sem posts)
SELECT u.nome, p.titulo
FROM utilizadores u
LEFT JOIN posts p ON p.user_id = u.id;
Índices
sql
-- Criar índice (acelera pesquisas)
CREATE INDEX idx_email ON utilizadores(email);

-- Apagar índice
DROP INDEX idx_email;
Transações
sql
BEGIN TRANSACTION;
  UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;

-- Cancelar em caso de erro
ROLLBACK;
Comandos úteis do terminal SQLite
Comando	Descrição
.tables	Lista todas as tabelas
.schema	Mostra o DDL completo
.headers on	Mostra cabeçalhos nas queries
.mode column	Formata saída em colunas
.output file.txt	Redireciona output para ficheiro
.read script.sql	Executa um ficheiro SQL
.help	Lista todos os comandos



-------

1. Tipos de dados no SQLite

O SQLite é mais flexível do que outros SGBDs. Os tipos mais comuns são:

INTEGER
REAL
TEXT
BLOB
NULL

Exemplo:

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL
);
2. Chaves estrangeiras (Foreign Keys)
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES utilizadores(id)
);

Ativar suporte a foreign keys:

PRAGMA foreign_keys = ON;
3. ALTER TABLE

Adicionar colunas a tabelas existentes:

ALTER TABLE utilizadores
ADD COLUMN telefone TEXT;

Renomear tabela:

ALTER TABLE utilizadores
RENAME TO clientes;
4. DISTINCT

Remover duplicados:

SELECT DISTINCT cidade
FROM utilizadores;
5. IN

Filtrar vários valores:

SELECT *
FROM utilizadores
WHERE idade IN (18, 25, 30);
6. Subqueries
SELECT nome
FROM utilizadores
WHERE idade > (
    SELECT AVG(idade)
    FROM utilizadores
);
7. Ver informação da tabela
PRAGMA table_info(utilizadores);

Resultado típico:

cid	nome	tipo	notnull
0	id	INTEGER	0
1	nome	TEXT	1
8. Backup da base de dados

Dentro do terminal SQLite:

.backup backup.db

Ou na shell:

cp minha_base.db backup.db
9. Importar e exportar CSV

Importar:

.mode csv
.import utilizadores.csv utilizadores

Exportar:

.headers on
.mode csv
.output utilizadores.csv

SELECT * FROM utilizadores;

.output stdout
10. Consulta completa de exemplo
SELECT
    u.nome,
    COUNT(p.id) AS total_posts
FROM utilizadores u
LEFT JOIN posts p
    ON p.user_id = u.id
WHERE u.idade >= 18
GROUP BY u.id, u.nome
HAVING total_posts > 0
ORDER BY total_posts DESC
LIMIT 10;

Se estiveres a aprender SQLite para desenvolvimento (Python, C#, Java, PHP, Node.js, etc.), os comandos que mais vais usar no dia a dia são:

CREATE TABLE
INSERT INTO
SELECT
UPDATE
DELETE
WHERE
ORDER BY
GROUP BY
JOIN
CREATE INDEX
BEGIN / COMMIT / ROLLBACK