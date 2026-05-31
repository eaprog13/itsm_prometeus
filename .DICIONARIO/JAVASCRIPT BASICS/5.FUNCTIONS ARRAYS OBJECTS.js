/*
=====================================================
 DICIONÁRIO DE ESTUDO – FUNÇÕES, ARRAYS E OBJETOS
 Uso: Material de apoio no VS Code
=====================================================
*/
//🧠 Função faz coisas.
//    Array guarda coisas.
/*
=============================
 FUNÇÕES
=============================
*/

// Função declarativa
function soma(a, b) {
  return a + b;
}

// Função com parâmetros e retorno
let resultado = soma(2, 3); // 5

// Função anónima
const subtrair = function (a, b) {
  return a - b;
};

// Arrow function (função seta)
const multiplicar = (a, b) => a * b;

// Arrow function com bloco
const dividir = (a, b) => {
  if (b === 0) return null;
  return a / b;
};

// Parâmetros por defeito
function saudacao(nome = "Utilizador") {
  console.log(`Olá, ${nome}`);
}

// Função sem retorno explícito
function mostrarMensagem() {
  console.log("Mensagem exibida");
}

/*
=============================
 ARRAYS
=============================
*/

// Criação de array
let numeros = [1, 2, 3, 4];

// Acesso por índice (começa em 0)
numeros[0]; // 1

// Tamanho do array
numeros.length; // 4

// Adicionar elementos
numeros.push(5);      // fim
numeros.unshift(0);   // início

// Remover elementos
numeros.pop();        // fim
numeros.shift();      // início

// Percorrer array com for
for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}

// forEach
numeros.forEach(n => console.log(n));

// map – cria novo array transformado
let dobrados = numeros.map(n => n * 2);

// filter – filtra valores
let pares = numeros.filter(n => n % 2 === 0);

// find – encontra o primeiro valor
let encontrado = numeros.find(n => n > 2);

// includes – verifica se existe
numeros.includes(3); // true

/*
=============================
 OBJETOS
=============================
*/

// Criação de objeto
const pessoa = {
  nome: "Ana",
  idade: 30,
  ativo: true
};

// Acesso às propriedades
pessoa.nome;          // dot notation
pessoa["idade"];     // bracket notation

// Alterar valores
pessoa.idade = 31;

// Adicionar nova propriedade
pessoa.profissao = "Programadora";

// Remover propriedade
delete pessoa.ativo;

// Percorrer objeto com for...in
for (const chave in pessoa) {
  console.log(chave, pessoa[chave]);
}

// Object.keys – retorna chaves
Object.keys(pessoa);

// Object.values – retorna valores
Object.values(pessoa);

// Object.entries – pares chave/valor
Object.entries(pessoa);

/*
=============================
 ARRAYS DE OBJETOS
=============================
*/

const alunos = [
  { nome: "João", nota: 15 },
  { nome: "Maria", nota: 18 },
  { nome: "Pedro", nota: 12 }
];

// map com objetos
let nomes = alunos.map(a => a.nome);

// filter com objetos
let aprovados = alunos.filter(a => a.nota >= 14);

// find com objetos
let melhorAluno = alunos.find(a => a.nota === 18);

/*
=============================
 BOAS PRÁTICAS
=============================
*/

// Usar const sempre que possível
// Usar funções pequenas e reutilizáveis
// Evitar mutações desnecessárias

/*
=============================
 RESUMO RÁPIDO
=============================

Funções
- Declarativa
- Anónima
- Arrow function

Arrays
- push / pop / shift / unshift
- map / filter / find / forEach

Objetos
- Propriedades
- for...in
- Object.keys / values / entries

=============================
 FIM DO DICIONÁRIO
=============================
*/
