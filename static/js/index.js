function verifyContainer() {
  var body = document.querySelector("main #main-container");
  if (!body) {
    console.error("Elemento não encontrado");
    return null;
  }
  return body;
}

function partialHome() {
  var body = verifyContainer();
  if (!body) return;

  body.innerHTML = "";
  var div = document.createElement("div");
  var h1 = document.createElement("h1");
  h1.textContent = "minha home";

  div.appendChild(h1);
  body.appendChild(div);
}

function partialNewBlog() {
  var body = verifyContainer();
  if (!body) return;

  body.innerHTML = "";

  const container = document.createElement("div");
  container.classList.add("container");

  const row = document.createElement("div");
  row.classList.add("row", "justify-content-center");

  const col = document.createElement("div");
  col.classList.add("col-md-4", "col-10");

  const form = document.createElement("form");
  form.id = "form-new-post";
  form.classList.add("form-control", "p-4", "shadow-sm", "rounded");

    const labelSubject = document.createElement("label");
    labelSubject.textContent = "Assuntos";
    labelSubject.classList.add("form-label");

    const selectSubject = document.createElement("select");
   selectSubject.classList.add("form-select");

  const labelTitle = document.createElement("label");
  labelTitle.textContent = "Título";
  labelTitle.classList.add("form-label");

  const inputTitle = document.createElement("input");
  inputTitle.type = "text";
  inputTitle.classList.add("form-control");

  const labelDesc = document.createElement("label");
  labelDesc.textContent = "Descrição";
  labelDesc.classList.add("form-label", "mt-3");

  const textareaDesc = document.createElement("textarea");
  textareaDesc.classList.add("form-control");
  textareaDesc.rows = 5;

  const buttonGroup = document.createElement("div");
  buttonGroup.classList.add("mt-3");

  const btnPublish = document.createElement("button");
  btnPublish.textContent = "Publicar";
  btnPublish.type = "button";
  btnPublish.classList.add("btn", "btn-success","mt-2","mx-1");

  const btnCancel = document.createElement("button");
  btnCancel.textContent = "Cancelar";
  btnCancel.type = "button";
  btnCancel.classList.add("btn", "btn-danger","mt-2","mx-1");


  form.appendChild(labelSubject);
  form.appendChild(selectSubject);
  form.appendChild(labelTitle);
  form.appendChild(inputTitle);
  form.appendChild(labelDesc);
  form.appendChild(textareaDesc);
  buttonGroup.appendChild(btnPublish);
  buttonGroup.appendChild(btnCancel);
  form.appendChild(buttonGroup);

  col.appendChild(form);
  row.appendChild(col);
  container.appendChild(row);
  body.appendChild(container);
}


function partialMyData(){
    const body = document.querySelector("main  #main-container");
    body.innerHTML = "";

    const container = document.createElement("div");
    container.classList.add("container");

    const row = document.createElement("div");
    row.classList.add("row", "justify-content-center");

    const col = document.createElement("div");
    col.classList.add("col-md-6", "col-12");

    const myDataForm = document.createElement("form");
    myDataForm.id = "form-put-data";
    myDataForm.classList.add("form-control","mt-3");

    const nameLabel = document.createElement("label");
    nameLabel.textContent = "Nome";
    nameLabel.id = "input-name-label";
    nameLabel.classList.add("form-label");

    const name = document.createElement("input");
    name.id = "input-name";
    name.classList.add("form-control");

    const userNameLabel = document.createElement("label");
    userNameLabel.textContent = "Nome de Usuário";
    userNameLabel.id = "input-user-name-label";
    userNameLabel.classList.add("form-label");

    const userName = document.createElement("input");
    userName.id = "input-user-name";
    userName.classList.add("form-control");

    const surNameLabel = document.createElement("label");
    surNameLabel.textContent = "Sobrenome";
    surNameLabel.id = "input-surname-label";
    surNameLabel.classList.add("form-label");

    const surName = document.createElement("input");
    surName.id = "input-surname";
    surName.classList.add("form-control");

    const passwordLabel = document.createElement("label");
    passwordLabel.textContent = "Senha";
    passwordLabel.id = "input-password-label";
    passwordLabel.classList.add("form-label");

    const password = document.createElement("input");
    password.id = "input-password";
    password.type = "password";
    password.classList.add("form-control");

    const emailLabel = document.createElement("label");
    emailLabel.textContent = "E-mail";
    emailLabel.id = "input-email-label";
    emailLabel.classList.add("form-label");

    const email = document.createElement("input");
    email.id = "input-email";
    email.type = "email";
    email.classList.add("form-control");

    const ageLabel = document.createElement("label");
    ageLabel.textContent = "Data de Nascimento";
    ageLabel.id = "input-age-label";
    ageLabel.classList.add("form-label");

    const age = document.createElement("input");
    age.id = "input-age";
    age.type = "date";
    age.classList.add("form-control");

    const buttonSave = document.createElement("button");
    buttonSave.textContent = "Salvar";
    buttonSave.type = "button";
    buttonSave.classList.add("btn", "btn-success", "mt-2","mx-1");

    const buttonCancel = document.createElement("button");
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

    myDataForm.appendChild(buttonSave);
    myDataForm.appendChild(buttonCancel);

    col.appendChild(myDataForm);
    row.appendChild(col);
    container.appendChild(row);
    body.appendChild(container);

}


function partialMyBlogs(){
    var body = document.querySelector("main  #main-container");
    body.innerHTML = "";

    var teste = document.createElement("h1")
    teste.textContent="minha publicações"

    body.appendChild(teste)
}

document.addEventListener("DOMContentLoaded", partialHome);

