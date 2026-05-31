
1 - VARIÁVEIS E TIPOS DE DADOS
 Definição: Armazenam valores e possuem tipos dinâmicos.

x = 10           # int
y = 3.14         # float
nome = "Ana"     # string
ativo = True     # boolean
valores = [1,2,3] # list
coordenadas = (10,20) # tuple
dados = {'nome':'Ana','idade':25} # dict
conjunto = {1,2,3} # set


/*=============================


2 - OPERADORES
 Definição: Executam operações matemáticas, comparações e lógicas.

# Aritméticos: +, -, *, /, %, **, //
a = 10 + 5
b = 10 ** 2

# Comparação: ==, !=, >, <, >=, <=
print(a == b)

# Lógicos: and, or, not
print(True and False)


/*=============================


3 - ESTRUTURAS DE DECISÃO
 Definição: Permitem executar blocos condicionais.

idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

nota = 85
if nota >= 90:
    print("A")
elif nota >= 70:
    print("B")
else:
    print("C")


/*=============================


4 - LAÇOS / REPETIÇÃO
 Definição: Repetem blocos de código.

# for: percorre sequências
for i in range(5):
    print(i)

# while: enquanto condição verdadeira
n = 5
while n > 0:
    print(n)
    n -= 1

# break e continue
for i in range(5):
    if i == 3: break
    print(i)
for i in range(5):
    if i == 3: continue
    print(i)


/*=============================


5 - FUNÇÕES
 Definição: Agrupam código reutilizável.

def soma(a:int, b:int) -> int:
    return a + b

resultado = soma(2,3)

# Funções lambda (anônimas)
somar = lambda x,y: x+y


/*=============================


6 - MANIPULAÇÃO DE LISTAS E DICIONÁRIOS
 Definição: Métodos para acessar, modificar e iterar coleções.

lista = [1,2,3]
lista.append(4)
lista.remove(2)

# Dicionário
pessoa = {'nome':'Ana','idade':25}
print(pessoa['nome'])
pessoa['idade'] = 26

# Métodos úteis
valores = list(pessoa.values())
chaves = list(pessoa.keys())
itens = list(pessoa.items())


/*=============================


7 - CLASSES E ORIENTAÇÃO A OBJETOS
 Definição: Estrutura para POO.

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def mover(self, distancia):
        print(f"{self.nome} moveu {distancia}m")

class Cachorro(Animal):
    def latir(self):
        print("Au au")

dog = Cachorro('Rex')
dog.mover(10)
dog.latir()


/*=============================


8 - MÓDULOS E IMPORTS
 Definição: Organizam código e permitem reutilização.

import math
from datetime import datetime
print(math.sqrt(16))
print(datetime.now())


/*=============================


9 - EXCEÇÕES
 Definição: Tratamento de erros em tempo de execução.

try:
    valor = int('abc')
except ValueError as e:
    print('Erro:', e)
finally:
    print('Fim do bloco')


/*=============================


10 - EXPRESSÕES REGULARES
 Definição: Permitem buscar e manipular padrões em strings.

import re
texto = 'Meu email: teste@exemplo.pt'
padrao = r'\S+@\S+'
print(re.findall(padrao, texto))


/*=============================


11 - LIST COMPREHENSIONS
 Definição: Sintaxe concisa para criar listas.

quadrados = [x**2 for x in range(5)]
pares = [x for x in range(10) if x%2==0]


/*=============================


12 - TIPAGEM (Python 3.5+)
 Definição: Indicação opcional de tipos para variáveis e funções.


def saudacao(nome: str) -> str:
    return f'Olá {nome}'

/*=============================


1️⃣ Operadores Aritméticos
Operador	Descrição	Exemplo	Resultado
+	Adição	5 + 3	8
-	Subtração	5 - 3	2
*	Multiplicação	5 * 3	15
/	Divisão (float)	5 / 2	2.5
//	Divisão inteira (floor)	5 // 2	2
%	Resto da divisão (módulo)	5 % 2	1
**	Potência	5 ** 2	25

2️⃣ Operadores de Comparação
Operador	Descrição	Exemplo	Resultado
==	Igual a	5 == 5	True
!=	Diferente de	5 != 3	True
>	Maior que	5 > 3	True
<	Menor que	5 < 3	False
>=	Maior ou igual a	5 >= 5	True
<=	Menor ou igual a	5 <= 4	False

Python permite comparações encadeadas: 1 < x < 10

3️⃣ Operadores Lógicos
Operador	Descrição	Exemplo	Resultado
and	Verdadeiro se todas as condições forem verdadeiras	x>0 and x<10	True se x entre 1 e 9
or	Verdadeiro se qualquer condição for verdadeira	x<0 or x>10	True se x for fora do intervalo
not	Inverte o valor booleano	not x>5	True se x ≤ 5

⚠️ Não confundir com operadores bit a bit (&, |, ~)

4️⃣ Operadores de Atribuição
Operador	Descrição	Exemplo
=	Atribuição simples	x = 5
+=	Adição + atribuição	x += 3 → x = x + 3
-=	Subtração + atribuição	x -= 2 → x = x - 2
*=	Multiplicação + atribuição	x *= 4 → x = x * 4
/=	Divisão + atribuição	x /= 2 → x = x / 2
//=	Divisão inteira + atribuição	x //= 2
%=	Resto + atribuição	x %= 3
**=	Potência + atribuição	x **= 2
&=	AND bit a bit + atribuição	x &= 3
`	=`	OR bit a bit + atribuição
^=	XOR bit a bit + atribuição	x ^= 1
<<=	Deslocamento à esquerda + atribuição	x <<= 1
>>=	Deslocamento à direita + atribuição	x >>= 1
5️⃣ Operadores Bit a Bit
Operador	Descrição	Exemplo	Resultado
&	AND bit a bit	5 & 3	1
`	`	OR bit a bit	`5
^	XOR bit a bit	5 ^ 3	6
~	NOT bit a bit	~5	-6
<<	Deslocamento à esquerda	5 << 1	10
>>	Deslocamento à direita	5 >> 1	2 


Aritméticos: cálculos matemáticos básicos

Comparação: retorna True ou False

Lógicos: combina condições booleanas

Atribuição: atualiza valores de variáveis

Bit a bit: manipulam bits individuais







1️⃣ Operadores Aritméticos

Usados para cálculos matemáticos.

Operador	Significado	Exemplo	Resultado
+	adição	5 + 3	8
-	subtração	5 - 3	2
*	multiplicação	5 * 3	15
/	divisão	5 / 2	2.5
//	divisão inteira	5 // 2	2
%	resto da divisão	5 % 2	1
**	potência	5 ** 2	25

Exemplo:

a = 10
b = 3

print(a + b)
print(a // b)
print(a % b)
print(a ** b)

2️⃣ Operadores de Comparação

Comparam valores e retornam True ou False.

Operador	Significado	Exemplo
==	igual	5 == 5
!=	diferente	5 != 3
>	maior	5 > 3
<	menor	5 < 3
>=	maior ou igual	5 >= 5
<=	menor ou igual	5 <= 4

Exemplo:

x = 10
print(x > 5)
print(x == 10)

3️⃣ Operadores Lógicos

Usados para combinar condições.

Operador	Significado	Exemplo
and	e	x > 0 and x < 10
or	ou	x < 0 or x > 10
not	negação	not x > 5

Exemplo:

idade = 20

if idade > 18 and idade < 30:
    print("Jovem adulto")

4️⃣ Operadores de Atribuição

Servem para atribuir ou atualizar valores.

Operador	Exemplo	Equivalente
=	x = 5	
+=	x += 3	x = x + 3
-=	x -= 2	x = x - 2
*=	x *= 4	x = x * 4
/=	x /= 2	x = x / 2
//=	x //= 2	
%=	x %= 3	
**=	x **= 2	
&=	x &= 2	
`	=`	`x
^=	x ^= 2	
<<=	x <<= 1	
>>=	x >>= 1	

Exemplo:

x = 5
x += 3
print(x)

5️⃣ Operadores Bit a Bit

Manipulam bits dos números.

Operador	Significado	Exemplo
&	AND	5 & 3
`	`	OR
^	XOR	5 ^ 3
~	NOT	~5
<<	shift esquerda	5 << 1
>>	shift direita	5 >> 1

Exemplo:

print(5 & 3)
print(5 | 3)

6️⃣ Operadores de Pertença (Membership)

Verificam se um valor existe numa estrutura.

Operador	Significado
in	está dentro
not in	não está dentro

Exemplo:

lista = ["Ana", "João", "Maria"]

print("Ana" in lista)
print("Pedro" not in lista)

7️⃣ Operadores de Identidade

Verificam se duas variáveis apontam para o mesmo objeto na memória.

Operador	Significado
is	mesmo objeto
is not	objeto diferente

Exemplo:

a = [1,2]
b = a

print(a is b)

8️⃣ Operador Walrus (Python moderno)
Operador	Significado
:=	atribui valor dentro de expressão

Exemplo:

if (n := len("Python")) > 3:
    print(n)
📊 Resumo geral

Python tem 7 grandes grupos de operadores:

1️⃣ Aritméticos
2️⃣ Comparação
3️⃣ Lógicos
4️⃣ Atribuição
5️⃣ Bit a bit
6️⃣ Pertença (in)
7️⃣ Identidade (is)

operador moderno :=

