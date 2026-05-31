/*
=====================================================
 DICIONÁRIO – DOM, EVENTOS E FORMULÁRIOS
=====================================================
*/
Primeiro → apanhas os elementos do HTML
Depois → lês os valores
Depois → validas se estão vazios
Depois → mostras mensagem
Finalmente → ligas tudo ao botão
/*
=============================
 DOM (Document Object Model)
=============================
*/

// Seletores
const titulo = document.getElementById("titulo");
const itens = document.querySelectorAll(".item");
const valor = document.querySelector('[name="email"]').value;
// Alterar conteúdo
titulo.textContent = "Novo título";

titulo.innerHTML = "<strong>Título</strong>";

// Alterar estilos
titulo.style.color = "blue";

// Classes CSS
titulo.classList.add("ativo");
titulo.classList.remove("ativo");
titulo.classList.toggle("ativo");

/*
=============================
 EVENTOS
=============================
*/

const botao = document.querySelector("button");

botao.addEventListener("click", () => {
  console.log("Botão clicado");
});

// Evento com objeto event
botao.addEventListener("mouseover", (event) => {
  console.log(event.type);
});

/*
=============================
 FORMULÁRIOS
=============================
*/

const form = document.querySelector("form");
const inputNome = document.querySelector("#nome");

form.addEventListener("submit", (e) => {
  e.preventDefault(); // evita reload
  console.log(inputNome.value);
});

// Validação simples
if (inputNome.value === "") {
  console.log("Campo obrigatório");
}

/*
=============================
 FIM
=============================
*/


/* MANIPULAÇÃO DE DOM */

getElementById(): seleciona um elemento pelo seu ID.
Exemplo:
let elemento = document.getElementById('meuId');

getElementsByClassName(): seleciona todos os elementos com uma determinada classe. Retorna um HTMLCollection.
Exemplo:
let elementos = document.getElementsByClassName('minhaClasse');

getElementsByTagName(): seleciona todos os elementos com um determinado nome de tag. Retorna um HTMLCollection.
Exemplo:
let paragrafos = document.getElementsByTagName('p');

querySelector(): seleciona o primeiro elemento que corresponde a um seletor CSS.
Exemplo:
let elemento = document.querySelector('.minhaClasse');

querySelectorAll(): seleciona todos os elementos que correspondem a um seletor CSS. Retorna um NodeList.;
Exemplo:;
let elementos = document.querySelectorAll('.minhaClasse');



/* ALTERAR CONTEUDO */
innerHTML: permite alterar o conteúdo HTML interno de um elemento.

Exemplo:

let elemento = document.getElementById('meuId');
	elemento.innerHTML = 'Novo conteúdo';
textContent: permite alterar o conteúdo textual de um elemento, ignorando HTML.

Exemplo:

let elemento = document.querySelector('.minhaClasse');
	elemento.textContent = 'Novo texto';
setAttribute(): permite definir o valor de um atributo de um elemento.

Exemplo:

let imagem = document.querySelector('img');
	imagem.setAttribute('src', 'novaImagem.jpg');
getAttribute(): permite obter o valor de um atributo de um elemento.

Exemplo:

let link = document.querySelector('a');
	let href = link.getAttribute('href');

