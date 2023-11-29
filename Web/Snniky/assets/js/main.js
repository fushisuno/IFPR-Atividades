const frm = document.querySelector("form")
const bntList = document.querySelector("#btnListarUsers");
const userDados = []
var idUser = 0;

window.onload = function(){
    criarTable()
}

/*
frm.addEventListener("submit", (e) => {
    var nome = document.querySelector("#nome").value
    var senha = document.querySelector("#senha").value
    save(nome, senha)
    //deletes()
});

bntList.addEventListener('click', (e) => {
    e.preventDefault()
    listar()
    userDados.forEach(element => {
        document.querySelector("#users_list").innerHTML += `<h2>Id: ${element.id} - Nome: ${element.nome} - Senha: ${element.senha}</h2>`
    });
})
*/