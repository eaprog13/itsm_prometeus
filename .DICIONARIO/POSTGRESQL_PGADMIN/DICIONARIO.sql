-- VERIFICAR O BANCO E O SCHEMAS


-- Verificar qual banco está selecionado
SELECT current_database();

-- Listar todos os schemas
SELECT schema_name
FROM information_schema.schemata;

----------------------------------------------------------

--CRIAR E APAGAR TABELAS

--Apagar caso, exista.
DROP TABLE IF EXISTS public.pessoas;
DROP TABLE IF EXISTS public.cursos;

-- Criar tabela pessoas
CREATE TABLE public.pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    idade INT
);

--------------------------------------------------------
--INSERIR DADOS

-- Inserir dados na tabela pessoas
INSERT INTO public.pessoas (nome, idade)
VALUES
('Alice', 25),
('Bruno', 30),
('Carla', 22);

--------------------------------------------------------------
--CONSULTAR DADOS

-- Selecionar tudo da tabela pessoas
SELECT * FROM public.pessoas;

-- Selecionar apenas nomes
SELECT nome FROM public.pessoas;

-- Filtrar pessoas com idade maior que 24
SELECT nome, idade 
FROM public.pessoas 
WHERE idade > 24;

-- Ordenar pessoas por idade
SELECT * 
FROM public.pessoas 
ORDER BY idade DESC;

----------------------------------------------------------------

5️⃣ Atualizar e deletar dados
-- Atualizar idade de Alice
UPDATE public.pessoas
SET idade = 26
WHERE nome = 'Alice';

-- Deletar pessoa chamada Carla
DELETE FROM public.pessoas
WHERE nome = 'Carla';
6️⃣ Consultas com múltiplas tabelas (JOIN)

Vamos associar pessoas a cursos (exemplo básico de estudo):

-- Criar tabela de matrícula
DROP TABLE IF EXISTS public.matriculas;

CREATE TABLE public.matriculas (
    pessoa_id INT REFERENCES public.pessoas(id),
    curso_id INT REFERENCES public.cursos(id)
);

-- Inserir dados de matrícula
INSERT INTO public.matriculas (pessoa_id, curso_id)
VALUES
(1, 1),  -- Alice em Matemática
(2, 2),  -- Bruno em Física
(3, 1);  -- Carla em Matemática

-- Consultar pessoas com seus cursos
SELECT p.nome AS pessoa, c.nome AS curso
FROM public.matriculas m
JOIN public.pessoas p ON m.pessoa_id = p.id
JOIN public.cursos c ON m.curso_id = c.id;