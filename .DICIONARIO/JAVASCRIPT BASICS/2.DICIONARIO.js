/********************TIPOS DE DECLARAÇÃO DE VARIÁVEIS********************/
var
Escopo global ou de função.
Permite redeclarar e reatribuir.
Pode causar comportamentos inesperados → pouco usado hoje.

let 
Escopo de bloco (entre { }).
Não permite redeclaração no mesmo escopo.
Pode ser alterada (reatribuição).

const
Escopo de bloco.
Não permite redeclarar e não permite reatribuir.
O conteúdo de objetos e arrays pode mudar, mas a referência não.
/************************************************************************/

/***************TIPOS DE DADOS PRIMITIVOS E NAO-PRIMITIVOS***************/

Primitivos

string — textos
let nome = "Ana";

number — números (inteiros e decimais)
let idade = 25;
let preco = 19.99;

boolean — verdadeiro ou falso
let ativo = true;

undefined — variável declarada mas sem valor
let x;

null — ausência intencional de valor
let y = null;

bigint — números inteiros muito grandes
let big = 12345678901234567890n;

symbol — valores únicos, usados como identificadores
let id = Symbol("id");



Não-primitivos (objetos)

object — coleções de pares chave-valor
let pessoa = { nome: "João", idade: 30 };

array — listas
let cores = ["vermelho", "azul"];

function — funções são tipos especiais de objetos
function ola() { console.log("Olá!"); }


Tipo	      Exemplo	  Mutável?
string	    "Olá"	    não
number	    42	      não
boolean	    true	    não
undefined	  undefined	—
null	      null	    —
bigint	    10n	      não
symbol	    Symbol()	não
object	    {}	      sim
array	      []	      sim
/************************************************************************/


/**********************ESTRUTURAS DE DECISÃO(CONDIÇÃO)*******************/
if - Executa código se a condição for verdadeira.
if (idade >= 18) {
  console.log("Maior de idade");
}


if...else - Executa um bloco se a condição for verdadeira e outro se for falsa.
if (hora < 12) {
  console.log("Bom dia");
} else {
  console.log("Boa tarde");
}


else if - Permite testar várias condições.
if (nota >= 90) {
  console.log("A");
} else if (nota >= 70) {
  console.log("B");
} else {
  console.log("C");
}


switch - Boa alternativa quando tens várias opções específicas.
switch (cor) {
  case "vermelho":
    console.log("Pare");
    break;
  case "verde":
    console.log("Siga");
    break;
  default:
    console.log("Cor desconhecida");


/*********************ESTRUTURAS DE REPETIÇÃO (LOOPS)********************/

for - Quando sabes o número de repetições.
for (let i = 0; i < 5; i++) {
  console.log(i);
}


while - Repete enquanto a condição for verdadeira.
let n = 5;
while (n > 0) {
  console.log(n);
  n--;
}


do...while - Garante que o bloco executa pelo menos uma vez.
let n = 5;
do {
  console.log(n);
  n--;
} while (n > 0);


for...of - Usado para percorrer arrays, strings ou qualquer coisa iterável.
const frutas = ["maçã", "banana", "uva"];

for (const fruta of frutas) {
  console.log(fruta);
}


for...in - Percorre propriedades de objetos.
const pessoa = { nome: "Ana", idade: 30 };

for (const chave in pessoa) {
  console.log(chave, pessoa[chave]);
}


Array.prototype.forEach() - Não é um “loop” da linguagem, mas é muito usado para percorrer arrays.
const numeros = [1, 2, 3];
numeros.forEach(n => console.log(n));

/*************NÃO SÃO LAÇOS NEM CONDIÇÕES MAS CONTROLAM O COMPORTAMENTO*************/
BREAK - Interrompe um ciclo ou um switch.
for (let i = 0; i < 10; i++) {
  if (i === 5) break;

CONTINUE - Salta para a próxima iteração do ciclo.
for (let i = 0; i < 10; i++) {
  if (i === 5) continue;
  console.log(i);

try...CATCH - Estrutura de tratamento de erros.
try {
  JSON.parse("invalido");
} catch (erro) {
  console.log("Erro capturado");
}

throw - Lança um erro manualmente.
throw new Error("Algo correu mal!");

/********************ESTRUTURA ESPECIAL PARA ASSÍNCRONO********************* */
Usadas quando lidamos com operações assíncronas (API, timers, etc.).

async/await - Pausa o código até a Promise resolver.
async function carregar() {
  const dados = await fetch("url");
}

Promise.then() / .catch() / .finally()
fetch("url")
  .then(r => r.json())
  .catch(e => console.log("erro"));
/*********************************************************************** */


Decisão
if, else, else if
switch


Repetição
for
while
do...while
for...of
for...in
forEach (método de array)


Controlo de fluxo
break
continue
return
try...catch
throw


Assíncrono
async/await
promises
/******************************************************************** */

/*
JavaScript
│
├── Sequencial
│    └─ Código executa linha a linha
│
├── Condição (Seleção)
│    ├─ if
│    ├─ if...else
│    ├─ else if
│    └─ switch
│
└── Repetição (Loops)
     ├─ for          → repetir N vezes
     ├─ while        → repetir enquanto condição verdadeira
     ├─ do...while   → repete pelo menos 1 vez
     ├─ for...of     → percorrer arrays
     └─ for...in     → percorrer objetos

*/