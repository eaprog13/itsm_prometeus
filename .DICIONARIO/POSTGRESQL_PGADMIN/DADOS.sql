1️⃣ Números
Tipo	Descrição	Exemplo
SMALLINT	Número inteiro pequeno (2 bytes)	0, -100, 32767
INTEGER ou INT	Número inteiro padrão (4 bytes)	100, 2026
BIGINT	Número inteiro grande (8 bytes)	1234567890123
SERIAL	Inteiro auto-incremental (4 bytes)	Usado para id
BIGSERIAL	Inteiro auto-incremental grande	Para IDs maiores
DECIMAL(p,s) ou NUMERIC(p,s)	Número exato com precisão	12.34
REAL	Número de ponto flutuante (4 bytes)	3.14
DOUBLE PRECISION	Número de ponto flutuante maior (8 bytes)	3.14159265
2️⃣ Texto / Strings
Tipo	Descrição	Exemplo
CHAR(n)	Texto fixo com n caracteres	'A' ou 'ABCD'
VARCHAR(n)	Texto variável até n caracteres	'Alice'
TEXT	Texto ilimitado	'Este é um texto longo'

💡 Dica: Para campos de nomes, emails, descrições, VARCHAR ou TEXT são os mais usados.

3️⃣ Datas e horas
Tipo	Descrição	Exemplo
DATE	Data (ano-mês-dia)	'2026-03-10'
TIME	Hora (HH:MM:SS)	'14:30:00'
TIMESTAMP	Data e hora completas	'2026-03-10 14:30:00'
INTERVAL	Duração de tempo	'2 days'
4️⃣ Booleano
Tipo	Descrição	Exemplo
BOOLEAN	Verdadeiro ou falso	TRUE / FALSE
5️⃣ Tipos especiais do PostgreSQL
Tipo	Descrição	Exemplo
UUID	Identificador único universal	'550e8400-e29b-41d4-a716-446655440000'
JSON	Armazena dados em formato JSON	'{"nome":"Alice","idade":25}'
JSONB	Versão binária do JSON, mais rápida para consultas	'{"nome":"Alice","idade":25}'
ARRAY	Array de qualquer tipo	INTEGER[], TEXT[]
BYTEA	Dados binários	Arquivos ou imagens