/*
=====================================================
 DICIONÁRIO DE ESTUDO – FUNDAMENTOS DE JAVASCRIPT
 Uso: Material de apoio no VS Code
=====================================================
*/
// NO DOM DO JS, SELECIONAR, GUARDAR, EXECUTAR.
// PEDIDOS NO JS, TUDO O QUE TENHA ID- DOCUMENT.ELEMENTBYDI
// JÁ TUDO O QUE SEJA ESTRUTURA OU CSS, QUERYSELECTOR
/*
=============================
 DECLARAÇÃO DE VARIÁVEIS
=============================
*/

// var
// Escopo global ou de função
// Permite redeclaração e reatribuição
// Pode causar comportamentos inesperados (evitar)
var a = 10;
var a = 20; // permitido

// let
// Escopo de bloco { }
// Não permite redeclaração no mesmo escopo
// Permite reatribuição
let b = 10;
b = 15; // permitido

// const
// Escopo de bloco
// Não permite redeclaração nem reatribuição
// Objetos e arrays podem ser mutados
const c = 10;

const pessoaConst = { nome: "Ana" };
pessoaConst.nome = "João"; // permitido

/*
=============================
 TIPOS DE DADOS PRIMITIVOS
=============================
*/

// string – texto
let nome = "Ana";

// number – números inteiros e decimais
let idade = 25;
let preco = 19.99;

// boolean – verdadeiro ou falso
let ativo = true;

// undefined – declarada sem valor
let x;

// null – ausência intencional de valor
let y = null;

// bigint – números inteiros muito grandes
let big = 12345678901234567890n;

// symbol – valor único
let id = Symbol("id");

/*
=============================
 TIPOS NÃO-PRIMITIVOS (OBJETOS)
=============================
*/

// object – pares chave-valor
let pessoa = { nome: "João", idade: 30 };

// array – listas
let cores = ["vermelho", "azul"];

// function – funções são objetos especiais
function ola() {
  console.log("Olá!");
}

/*
=============================
 ESTRUTURAS DE DECISÃO
=============================
*/

// if
if (idade >= 18) {
  console.log("Maior de idade");
}

// if...else
let hora = 10;
if (hora < 12) {
  console.log("Bom dia");
} else {
  console.log("Boa tarde");
}

// else if
let nota = 75;
if (nota >= 90) {
  console.log("A");
} else if (nota >= 70) {
  console.log("B");
} else {
  console.log("C");
}

// switch
let cor = "verde";
switch (cor) {
  case "vermelho":
    console.log("Pare");
    break;
  case "verde":
    console.log("Siga");
    break;
  default:
    console.log("Cor desconhecida");
}

/*
=============================
 ESTRUTURAS DE REPETIÇÃO
=============================
*/

// for – número conhecido de repetições
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// while – enquanto condição for verdadeira
let n1 = 5;
while (n1 > 0) {
  console.log(n1);
  n1--;
}

// do...while – executa pelo menos uma vez
let n2 = 5;
do {
  console.log(n2);
  n2--;
} while (n2 > 0);

// for...of – percorre arrays ou iteráveis
const frutas = ["maçã", "banana", "uva"];
for (const fruta of frutas) {
  console.log(fruta);
}

// for...in – percorre propriedades de objetos
const pessoaObj = { nome: "Ana", idade: 30 };
for (const chave in pessoaObj) {
  console.log(chave, pessoaObj[chave]);
}

// forEach – método de array
const numeros = [1, 2, 3];
numeros.forEach(n => console.log(n));

/*
=============================
 CONTROLO DE FLUXO
=============================
*/

// break – interrompe ciclo ou switch
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
}

// continue – salta para próxima iteração
for (let i = 0; i < 10; i++) {
  if (i === 5) continue;
  console.log(i);
}

// try...catch – tratamento de erros
try {
  JSON.parse("invalido");
} catch (erro) {
  console.log("Erro capturado");
}

// throw – lança erro manualmente
// throw new Error("Algo correu mal!");

/*
=============================
 PROGRAMAÇÃO ASSÍNCRONA
=============================
*/

// async / await
async function carregar() {
  const resposta = await fetch("url");
  return resposta;
}

// Promises
fetch("url")
  .then(r => r.json())
  .catch(e => console.log("erro"));

/*
=============================
 RESUMO MENTAL
=============================

JavaScript
├── Sequencial
├── Condição
│    ├─ if / else / else if
│    └─ switch
└── Repetição
     ├─ for
     ├─ while
     ├─ do...while
     ├─ for...of
     └─ for...in

=============================
 FIM DO DICIONÁRIO
=============================
*/


/*
=====================================================
 DICIONÁRIO COMPLETO DE JAVASCRIPT – COMENTADO EXPLÍCITO
 Uso: Material de apoio no VS Code
=====================================================
*/

/*=============================
1 - TIPOS DE DECLARAÇÃO DE VARIÁVEIS
=============================*/
/* var: escopo global ou de função, pode ser redeclarada, menos usada hoje em dia */
var idade = 25; // Exemplo de var

/* let: escopo de bloco (entre chaves {}), permite reatribuição, mas não permite redeclarar no mesmo escopo */
let nome = 'Ana';
nome = 'João'; // reatribuição

/* const: escopo de bloco, não permite reatribuir ou redeclarar. O conteúdo de arrays e objetos pode mudar, mas a referência não */
const PI = 3.1415;
const cores = ['vermelho', 'azul'];
cores.push('verde'); // permitido

/*=============================
2 - TIPOS DE DADOS
=============================*/
// Primitivos: valores imutáveis e de tipos simples
let ativo = true;          // boolean
let preco = 19.99;         // number
let x;                     // undefined
let y = null;              // null
let big = 12345678901234567890n; // bigint
let id = Symbol('id');     // symbol, identificadores únicos

// Não primitivos (objetos): podem ser mutáveis e armazenam coleções ou funções
let pessoa = { nome: 'João', idade: 30 }; // object
let lista = [1,2,3];                      // array
function ola() { console.log('Olá'); }    // function

/*=============================
3 - ESTRUTURAS DE DECISÃO
=============================*/
// if: executa bloco de código se a condição for verdadeira
if (idade >= 18) { console.log('Maior de idade'); }

// if...else: executa um bloco se verdadeiro, outro se falso
if (hora < 12) { console.log('Bom dia'); } else { console.log('Boa tarde'); }

// else if: permite testar várias condições sequencialmente
if (nota >= 90) { console.log('A'); } else if (nota >= 70) { console.log('B'); } else { console.log('C'); }

// switch: alternativa quando temos várias opções específicas
switch(cor) {
  case 'vermelho': console.log('Pare'); break;
  case 'verde': console.log('Siga'); break;
  default: console.log('Cor desconhecida');
}

/*=============================
4 - ESTRUTURAS DE REPETIÇÃO
=============================*/
// for: repete código N vezes
for(let i=0;i<5;i++){ console.log(i); }

// while: repete enquanto condição for verdadeira
let n=5; while(n>0){ console.log(n); n--; }

// do...while: garante execução pelo menos uma vez
let m=5; do { console.log(m); m--; } while(m>0);

// for...of: percorre arrays ou strings
const frutas=['maçã','banana','uva'];
for(const fruta of frutas){ console.log(fruta); }

// for...in: percorre propriedades de objetos
const pessoaObj={ nome:'Ana', idade:30 };
for(const chave in pessoaObj){ console.log(chave, pessoaObj[chave]); }

// forEach: método de array para percorrer itens
const numeros=[1,2,3];
numeros.forEach(n => console.log(n));

/*=============================
5 - CONTROLE DE FLUXO
=============================*/
// break: interrompe um loop ou switch
for(let i=0;i<10;i++){ if(i===5) break; }

// continue: pula para a próxima iteração do loop
for(let i=0;i<10;i++){ if(i===5) continue; console.log(i); }

// try...catch: captura erros em tempo de execução
try{ JSON.parse('invalido'); } catch(erro){ console.log('Erro capturado'); }

// throw: lança um erro manualmente
throw new Error('Algo correu mal!');

/*=============================
6 - FUNÇÕES AVANÇADAS
=============================*/
// Arrow function: sintaxe curta e lexicalmente ligada
const soma = (a,b) => a+b;

// Parâmetros default: valor padrão se não for passado
function ola(nome='Guest'){ console.log(`Olá ${nome}`); }

// Rest parameters: agrupa múltiplos argumentos em um array
function total(...numeros){ return numeros.reduce((acc,n)=>acc+n,0); }

// Spread operator: expande arrays ou objetos
const arr1=[1,2]; const arr2=[...arr1,3,4];

// IIFE - Immediately Invoked Function Expression
(function(){ console.log('IIFE executada'); })();

/*=============================
7 - MANIPULAÇÃO DE ARRAYS
=============================*/
// Métodos úteis de arrays
nums=[1,2,3,4];
nums.map(n=>n*2);     // cria novo array com resultados
nums.filter(n=>n>2); // filtra valores
nums.reduce((acc,n)=>acc+n,0); // reduz a um valor
nums.find(n=>n>2);   // retorna primeiro que atende condição
nums.some(n=>n>3);   // retorna true se algum atender condição
nums.every(n=>n>0);  // retorna true se todos atenderem condição
nums.includes(2);     // verifica existência

/*=============================
8 - OBJETOS AVANÇADOS
=============================*/
Object.keys(pessoa);           // retorna array de chaves
Object.values(pessoa);         // retorna array de valores
Object.entries(pessoa);        // retorna array de [chave, valor]
Object.assign({}, pessoa);     // copia objeto
pessoa.hasOwnProperty('nome'); // verifica se chave existe

// Computed properties: cria chaves dinamicamente
let chave='idade';
let pessoaComp={[chave]:30};

/*=============================
9 - OPERADORES AVANÇADOS
=============================*/
// Operador ternário: condição ? valor1 : valor2
const resultado = idade>=18 ? 'Adulto':'Menor';

// Coalescência nula: retorna valor padrão se null ou undefined
const valor = pessoa?.idade ?? 0;

// Encadeamento opcional: evita erros se objeto ou propriedade não existir
console.log(pessoa?.endereco?.rua);

/*=============================
10 - MÓDULOS (ES6+)
=============================*/
// export const PI = 3.14;
// export default function soma(a,b){ return a+b; }
// import soma from './arquivo.js';

/*=============================
11 - EVENTOS DO DOM
=============================*/
// addEventListener: adiciona eventos a elementos
const btn=document.querySelector('button');
btn.addEventListener('click',()=>{ console.log('Clicou'); });

// event.preventDefault(): evita comportamento padrão (ex: envio de formulário)
// event.stopPropagation(): impede propagação do evento para elementos pais

/*=============================
12 - ASSÍNCRONO E PROMISES
=============================*/
// async/await: pausa execução até a Promise resolver
async function carregar(){
  const dados = await fetch('url');
}

// Promises com then/catch/finally
fetch('url')
  .then(r=>r.json())
  .catch(e=>console.log('Erro'))
  .finally(()=>console.log('Fim'));