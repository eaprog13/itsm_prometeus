/*
=====================================================
 DICIONÁRIO – APIs, FETCH E JSON
=====================================================
*/

/*
=============================
 JSON
=============================
*/

// Converter objeto em JSON
const obj = { nome: "Ana", idade: 30 };
const jsonString = JSON.stringify(obj);

// Converter JSON em objeto
const jsonObj = JSON.parse(jsonString);

/*
=============================
 FETCH (HTTP REQUESTS)
=============================
*/

// GET
fetch("https://api.exemplo.com/dados")
  .then(res => res.json())
  .then(dados => console.log(dados))
  .catch(err => console.log(err));

// POST
fetch("https://api.exemplo.com/dados", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ nome: "Ana" })
});

/*
=============================
 ASYNC / AWAIT
=============================
*/

async function obterDados() {
  try {
    const res = await fetch("https://api.exemplo.com/dados");
    const dados = await res.json();
    console.log(dados);
  } catch (e) {
    console.log("Erro na API");
  }
}

/*
=============================
 PROMISES
=============================
*/

const promessa = new Promise((resolve, reject) => {
  let sucesso = true;
  if (sucesso) resolve("OK");
  else reject("Erro");
});

promessa
  .then(r => console.log(r))
  .catch(e => console.log(e))
  .finally(() => console.log("Fim"));

/*
=============================
 FIM
=============================
*/
