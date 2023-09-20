const frm = document.querySelector("form");
const dvQuadro = document.querySelector(".items_vet");
const btRemove = document.querySelector("#btRemove")
const vetNum = Array();

/* Metodo 1*/
frm.addEventListener("submit", (e)=>{
    e.preventDefault();
    dvQuadro.innerHTML = "";

    const tarefa = frm.inTarefa.value;

    if(Number(tarefa) < 0 || Number(tarefa) > 100 || tarefa.length < 1){
        swal.fire({
            icon: "error",
            title: "Valor inválido",
            text: "Digite um valor ente 0 e 100",
            confirmButtonColor: "#0dcaf0"
        })
    }else{
        vetNum.push(+tarefa)
    }
    
    vetNum.sort((a, b) => (a - b));

    for(let i = 0;i<vetNum.length;i++){
        let h5 = document.createElement("h5");
        let text = document.createTextNode(vetNum[i]);
        h5.appendChild(text);
        h5.className = "h5_list";
        dvQuadro.insertAdjacentElement('beforeend', h5)

        
    }
    frm.inTarefa.value = "";
    frm.inTarefa.focus();
});


btRemove.addEventListener('click', ()=>{
    debugger
    dvQuadro.innerHTML = "";
    const tarefa = Number(frm.inTarefa.value);

    if(vetNum.indexOf(Number(tarefa)) == -1){
        swal.fire({
            icon: "error",
            title: "Valor não encontrado",
            text: "Remova um valor válido",
            confirmButtonColor: "#0dcaf0"
        })
    }else{
        while(vetNum.indexOf(tarefa) != -1){
            vetNum.splice(vetNum.indexOf(tarefa), 1)
        }
    }

    vetNum.forEach((element) => {
        dvQuadro.insertAdjacentHTML('beforeend', `<h5 class="h5_list">${element}</h5>`)
    });
    frm.inTarefa.value = "";
    frm.inTarefa.focus();
})

