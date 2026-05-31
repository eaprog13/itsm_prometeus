/*
=====================================================
 DICIONÁRIO – TODAS AS ESTRUTURAS DO JAVASCRIPT
=====================================================
*/

/*
=============================
 EXECUÇÃO SEQUENCIAL
=============================
*/

let a = 5;
a = a + 2;
console.log(a);

/*
=============================
 CONDIÇÃO (DECISÃO)
=============================
*/

if (a > 5) {
  console.log("Maior que 5");
} else {
  console.log("Menor ou igual a 5");
}

switch (a) {
  case 1:
    console.log("Um");
    break;
  default:
    console.log("Outro valor");
}

/*
=============================
 REPETIÇÃO (LOOPS)
=============================
*/

for (let i = 0; i < 3; i++) {
  console.log(i);
}

let n = 3;
while (n > 0) {
  n--;
}

do {
  n++;
} while (n < 3);

/*
=============================
 CONTROLO DE FLUXO
=============================
*/

for (let i = 0; i < 5; i++) {
  if (i === 3) break;
}

for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
}

function exemploReturn() {
  return "Fim";
}

try {
  JSON.parse("erro");
} catch (e) {
  console.log("Erro tratado");
}

// throw new Error("Erro manual");

/*
=============================
 ESTRUTURAS ASSÍNCRONAS
=============================
*/

async function carregar() {
  return "dados";
}

Promise.resolve("ok")
  .then(r => console.log(r));

/*
=============================
 FIM
=============================
*/
