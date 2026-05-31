
=============================
 OPERADORES ARITMÉTICOS
=============================
Usados para cálculos matemáticos
*/

// Adição (+)
// Soma valores
5 + 3; // 8

// Subtração (-)
// Subtrai valores
5 - 3; // 2

// Multiplicação (*)
5 * 3; // 15

// Divisão (/)
6 / 3; // 2

// Módulo (%)
// Resto da divisão
5 % 2; // 1

// Exponenciação (**)
2 ** 3; // 8

// Incremento (++)
let x = 5;
x++; // x = 6

// Decremento (--)
let y = 5;
y--; // y = 4

/*
Nota:
O operador + também concatena strings
*/
"5" + 3; // "53"

/*
=============================
 OPERADORES DE COMPARAÇÃO
=============================
Retornam true ou false
*/

// Igualdade (valor)
5 == "5"; // true

// Igualdade estrita (valor e tipo)
5 === "5"; // false

// Diferente
5 != 3; // true

// Diferente estrito
5 !== "5"; // true

// Maior que
5 > 3; // true

// Menor que
5 < 3; // false

// Maior ou igual
5 >= 5; // true

// Menor ou igual
5 <= 3; // false

/*
Boa prática:
Usar sempre === e !==
*/

/*
=============================
 OPERADORES LÓGICOS
=============================
Usados para combinar condições
*/

// AND (&&)
// true se ambas forem verdadeiras
true && false; // false

// OR (||)
// true se uma for verdadeira
true || false; // true

// NOT (!)
// Inverte o valor lógico
!true; // false

/*
=============================
 EXEMPLOS PRÁTICOS
=============================
*/

// Exemplo 1: Verificação simples
let idade = 20;
idade >= 18; // true

// Exemplo 2: Condição composta
let temCarta = true;
idade >= 18 && temCarta; // true

// Exemplo 3: Uso em if
let preco = 120;
let desconto = true;

if (preco > 100 && desconto) {
  console.log("Desconto aplicado");
} else {
  console.log("Sem desconto");
}

/*
=============================
 FIM DO DICIONÁRIO
=============================
*/