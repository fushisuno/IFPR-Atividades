const frm = document.querySelector("form");
const dvQuadro = document.querySelector("#divQuadro");

frm.addEventListener("submit", (e)=>{
    e.preventDefault();

    const tarefa = frm.inTarefa.value;

    const h5 = document.createElement("h5");
    const text = document.createTextNode(tarefa);
    h5.appendChild(text);
    h5.className = "h5_list";
    dvQuadro.appendChild(h5);


    frm.inTarefa.value = "";
    frm.inTarefa.focus();   

});

frm.btSelecionar.addEventListener("click", (e)=>{
    const tam = document.querySelectorAll("h5");

    if(tam.length == 0){
        swal.fire({
            icon: "info",
            title: "Sem tarefas selecionadas",
            text: "Selecione uma tarefa",
            confirmButtonColor: "#0dcaf0"
        })
    }

    let aux = -1;

    for(let i = 0;i<tam.length;i++){
        if(tam[i].className === "h5_list tarefa-selecionada"){
            tam[i].className = "h5_list tarefa-normal";
            aux = i;
            break;
        }
    }   

    if(aux == tam.length-1){
        aux = -1;
    }

    tam[aux + 1].className = "h5_list tarefa-selecionada";
});

const h5 = document.createElement("h5");
h5.addEventListener("click", (e) =>{
    alert("sus");
});