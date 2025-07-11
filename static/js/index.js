function partialHome(){
    var body = document.querySelector("main .container-home")
    body.innerHTML = ""
    var ell = document.createElement("p");
    var text = document.createTextNode("minha page home")
    ell.appendChild(text);
    body.appendChild(ell)
    console.log(body)
}

function partialNewBlog(){
    var body = document.querySelector("main .container-home")
    body.innerHTML = ""
    
    // Form para o novo blog
    var formNewBlog = document.createElement("form");
    formNewBlog.id = "form-new-post"

    var inputTitleLabel =document.createElement("label")
    inputTitleLabel.textContent = "Titulo"
    inputTitleLabel.classList.add("form-label")

    var inputTitle = document.createElement("input")
    inputTitle.type = "text"
    inputTitle.classList.add("form-control")

    var inputDescriptionLabel =document.createElement("label")
    inputDescriptionLabel.textContent = "Descrição"
    inputDescriptionLabel.classList.add("form-label")

    var inputDescription =document.createElement("input")
    inputDescription.type = "text-area"
    inputDescription.classList.add("form-control") 

    formNewBlog.appendChild(inputTitleLabel)
    formNewBlog.appendChild(inputTitle)
    formNewBlog.appendChild(inputDescriptionLabel)
    formNewBlog.appendChild(inputDescription)

    body.appendChild(formNewBlog)
    console.log(body)
}


document.addEventListener("DOMContentLoaded", partialHome);

