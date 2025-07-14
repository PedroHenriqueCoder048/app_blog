function partialHome(){
    var body = document.querySelector("main .container")
    body.id = "container-home"
    body.innerHTML = ""
    var ell = document.createElement("p");
    var text = document.createTextNode("minha page home")
    ell.appendChild(text);
    body.appendChild(ell)
    console.log(body)
}

function partialNewBlog() {
    var body = document.querySelector("main .container");
    body.id = "container-new-blog"
    body.innerHTML = "";

    var formNewBlog = document.createElement("form");
    formNewBlog.id = "form-new-post";
    formNewBlog.classList.add("form-control","mt-3");

    var inputTitleLabel = document.createElement("label");
    inputTitleLabel.textContent = "Título";
    inputTitleLabel.classList.add("form-label");

    var inputTitle = document.createElement("input");
    inputTitle.type = "text";
    inputTitle.classList.add("form-control");

    var inputDescriptionLabel = document.createElement("label");
    inputDescriptionLabel.textContent = "Descrição";
    inputDescriptionLabel.classList.add("form-label");

    var textareaDescription = document.createElement("textarea");
    textareaDescription.id = "descricao";
    textareaDescription.rows = 5;
    textareaDescription.classList.add("form-control");

    var buttonPublish = document.createElement("button");
    buttonPublish.textContent = "Publicar";
    buttonPublish.type = "button";
    buttonPublish.classList.add("btn", "btn-success", "mt-2","mx-1");

    var buttonCancel = document.createElement("button");
    buttonCancel.textContent = "Cancelar";
    buttonCancel.type = "button";
    buttonCancel.classList.add("btn", "btn-danger", "mt-2","mx-3");

    formNewBlog.appendChild(inputTitleLabel);
    formNewBlog.appendChild(inputTitle);
    formNewBlog.appendChild(inputDescriptionLabel);
    formNewBlog.appendChild(textareaDescription);
    formNewBlog.appendChild(buttonPublish);
    formNewBlog.appendChild(buttonCancel);


    body.appendChild(formNewBlog);
    console.log(body);
}

function partialMyData(){
    var body = document.querySelector("main .container");
    body.id = "container-my-data"
    body.innerHTML = "";

    var myDataForm = document.createElement("form")
    myDataForm.id = "form-put-data";
    myDataForm.classList.add("form-control");

    var nameLabel = document.createElement("Label");
    nameLabel.textContent = "Nome";
    nameLabel.id = "input-name-label";
    nameLabel.classList.add("form-label");

    var name = document.createElement("input");
    name.id = "input-name";
    name.classList.add("form-control");

    var userNameLabel = document.createElement("Label");
    userNameLabel.textContent = "Nome de Usuário";
    userNameLabel.id = "input-user-name-label";
    userNameLabel.classList.add("form-label");

    var userName = document.createElement("input");
    userName.id = "input-user-name";
    userName.classList.add("form-control");

    var surNameLabel = document.createElement("Label");
    surNameLabel.textContent = "Sobrenome";
    surNameLabel.id = "input-surname-label";
    surNameLabel.classList.add("form-label");

    var surName = document.createElement("input");
    surName.id = "input-surname";
    surName.classList.add("form-control");

    var passwordLabel = document.createElement("Label");
    passwordLabel.textContent = "Senha";
    passwordLabel.id = "input-password-label";
    passwordLabel.classList.add("form-label");

    var password = document.createElement("input");
    password.id = "input-password";
    password.type = "password";
    password.classList.add("form-control");

    var emailLabel = document.createElement("Label");
    emailLabel.textContent = "E-mail";
    emailLabel.id = "input-email-label";
    emailLabel.classList.add("form-label");

    var email = document.createElement("input");
    email.id = "input-email";
    email.type = "email";
    email.classList.add("form-control");

    var ageLabel = document.createElement("Label");
    ageLabel.textContent = "Data de Nascimento";
    ageLabel.id = "input-age-label";
    ageLabel.classList.add("form-label");

    var age = document.createElement("input");
    age.id = "input-age";
    age.type = "date";
    age.classList.add("form-control");

    var buttonSave = document.createElement("button");
    buttonSave.textContent = "Salvar";
    buttonSave.type = "button";
    buttonSave.classList.add("btn", "btn-success", "mt-2","mx-1");

    var buttonCancel = document.createElement("button");
    buttonCancel.textContent = "Cancelar";
    buttonCancel.type = "button";
    buttonCancel.classList.add("btn", "btn-danger", "mt-2","mx-1");


    myDataForm.appendChild(userNameLabel);
    myDataForm.appendChild(userName);

    myDataForm.appendChild(nameLabel);
    myDataForm.appendChild(name);

    myDataForm.appendChild(surNameLabel);
    myDataForm.appendChild(surName);

    myDataForm.appendChild(passwordLabel);
    myDataForm.appendChild(password);

    myDataForm.appendChild(emailLabel);
    myDataForm.appendChild(email);

    myDataForm.appendChild(ageLabel);
    myDataForm.appendChild(age);

    myDataForm.appendChild(buttonSave)
    myDataForm.appendChild(buttonCancel)


    body.appendChild(myDataForm);

}

function partialMyBlogs(){
    var body = document.querySelector("main .container");
    body.id = "container-my-blogs"
    body.innerHTML = "";

    var teste = document.createElement("h1")
    teste.textContent="minha publicações"

    body.appendChild(teste)
}

document.addEventListener("DOMContentLoaded", partialHome);

