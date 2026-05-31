1. BANCO DE DADOS

CREATE DATABASE nome_db; -- cria um novo banco de dados
DROP DATABASE nome_db; -- remove um banco de dados inteiro (cuidado!)
SHOW DATABASES; -- lista todos os bancos existentes
USE nome_db; -- seleciona o banco que será usado



📋 2. TABELAS

CREATE TABLE usuarios ( -- cria uma nova tabela chamada usuarios
    id INT AUTO_INCREMENT PRIMARY KEY, -- id único que aumenta automaticamente
    nome VARCHAR(100), -- campo de texto para nome
    email VARCHAR(150), -- campo de texto para email
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- data/hora automática de criação
);

DROP TABLE usuarios; -- apaga a tabela completamente
SHOW TABLES; -- mostra todas as tabelas do banco atual
DESCRIBE usuarios; -- mostra estrutura da tabela (colunas e tipos)



➕ 3. INSERT (INSERIR DADOS)

INSERT INTO usuarios (nome, email) -- define colunas que serão preenchidas
VALUES ('João', 'joao@email.com'); -- insere os valores na tabela



🔍 4. SELECT (CONSULTAR DADOS)

SELECT * FROM usuarios; -- seleciona todos os registros
SELECT nome, email FROM usuarios; -- seleciona apenas colunas específicas
SELECT * FROM usuarios WHERE id = 1; -- busca registro específico pelo id



✏️ 5. UPDATE (ATUALIZAR DADOS)

UPDATE usuarios -- indica a tabela que será atualizada
SET nome = 'João Silva' -- define novo valor
WHERE id = 1; -- define qual registro será alterado (obrigatório!)



❌ 6. DELETE (APAGAR DADOS)

DELETE FROM usuarios -- indica a tabela
WHERE id = 1; -- remove apenas o registro com id 1



🔎 7. FILTROS E ORDENAÇÃO

SELECT * FROM usuarios
WHERE nome LIKE 'Jo%' -- busca nomes que começam com "Jo"
ORDER BY nome ASC; -- ordena em ordem crescente

SELECT * FROM usuarios
ORDER BY id DESC; -- ordena do maior para o menor id

SELECT * FROM usuarios
LIMIT 10; -- limita a 10 resultados



🔗 8. JOINS (RELACIONAMENTOS)

SELECT pedidos.id, usuarios.nome -- seleciona dados de duas tabelas
FROM pedidos
INNER JOIN usuarios ON pedidos.usuario_id = usuarios.id; -- junta apenas registros correspondentes
SELECT usuarios.nome, pedidos.id -- mostra todos os usuários
FROM usuarios
LEFT JOIN pedidos ON usuarios.id = pedidos.usuario_id; -- mostra mesmo sem pedidos



🔢 9. FUNÇÕES

SELECT COUNT(*) FROM usuarios; -- conta total de registros
SELECT SUM(valor) FROM pedidos; -- soma valores
SELECT AVG(valor) FROM pedidos; -- média dos valores
SELECT MAX(valor) FROM pedidos; -- maior valor
SELECT MIN(valor) FROM pedidos; -- menor valor



🧱 10. ALTER TABLE (MODIFICAR TABELA)

ALTER TABLE usuarios ADD idade INT; -- adiciona nova coluna
ALTER TABLE usuarios DROP COLUMN idade; -- remove uma coluna
ALTER TABLE usuarios MODIFY nome VARCHAR(200); -- altera tipo/tamanho da coluna



🔐 11. USUÁRIOS E PERMISSÕES

CREATE USER 'user'@'localhost' IDENTIFIED BY 'senha'; -- cria usuário MySQL
GRANT ALL PRIVILEGES ON nome_db.* TO 'user'@'localhost'; -- dá permissões totais
FLUSH PRIVILEGES; -- atualiza permissões do sistema



🧰 12. phpMyAdmin (USO RÁPIDO)

SQL tab → escrever consultas manualmente
Ctrl + Enter → executar query
Ctrl + Space → autocompletar comandos SQL
Browse/Procurar → ver registros (SELECT visual)
✏️ Editar → altera registro
❌ Delete → apaga registro
📥 Exportar → baixar banco/tabela (SQL, CSV, etc.)
📤 Importar → subir arquivo .sql

🚀 DICA IMPORTANTE (MUITO USADA)
SELECT * FROM usuarios; -- usado para testar dados (evitar em produção)
-- SEMPRE use WHERE em UPDATE e DELETE para evitar apagar tudo


Resumo rápido
Comando	Serve para
SELECT	escolher dados
FROM	indicar tabela
WHERE	filtrar linhas
GROUP BY	agrupar
HAVING	filtrar grupos
ORDER BY	ordenar
JOIN	juntar tabelas
LIMIT	limitar resultados
DISTINCT	remover duplicados

Exemplo mental simples:

SELECT → o que quero ver
FROM → de onde vem
WHERE → quais quero
GROUP BY → como agrupar
HAVING → quais grupos ficam
ORDER BY → como ordenar
LIMIT → quantos mostrar


