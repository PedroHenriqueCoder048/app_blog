function atualizarConteudo(){
    var ell = document.createElement("p");
    var text = document.createTextNode("minha page home")
    var body = document.querySelector("main div")
    ell.appendChild(text);
    body.appendChild(ell)
    console.log(body)
}

document.addEventListener("DOMContentLoaded", atualizarConteudo);

