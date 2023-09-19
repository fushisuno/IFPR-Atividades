const frm = document.querySelector("form");
const dvQuadro = document.querySelector(".items_vet");
const vetNum = Array();
let aux = 0;

/* Metodo 1*/
frm.addEventListener("submit", (e)=>{
    e.preventDefault();
    dvQuadro.innerHTML = "";

    const tarefa = frm.inTarefa.value;

    if(tarefa == null || tarefa == ""){
        swal.fire({
            icon: "error",
            title: "Valor inválido",
            text: "Selecione uma tarefa",
            confirmButtonColor: "#0dcaf0"
        })
    }else{
        vetNum.push(Number(tarefa));
    }
    
    vetNum.sort((a, b) => (a - b));

    for(let i = 0;i<vetNum.length;i++){
        let h5 = document.createElement("h5");
        console.log(vetNum[i]);
        let text = document.createTextNode(vetNum[i]);
        h5.appendChild(text);
        h5.className = "h5_list";

        dvQuadro.insertAdjacentElement('beforeend', h5)
    }
    
    frm.inTarefa.value = "";
    frm.inTarefa.focus();
    aux++;   

});





/* Metodo 1*/
/*
const frm = document.querySelector("form");
const dvQuadro = document.querySelector(".items_vet");
const vetNum = Array();
let aux = 0;


frm.addEventListener("submit", (e)=>{
    e.preventDefault();
    dvQuadro.innerHTML = ""

    const tarefa = frm.inTarefa.value;
    let boll = 0;

    if(tarefa == null || tarefa == ""){
        swal.fire({
            icon: "error",
            title: "Valor inválido",
            text: "Selecione uma tarefa",
            confirmButtonColor: "#0dcaf0"
        })
    }else{
    if(aux == 0){
        vetNum.push(Number(tarefa));
    }
    else{
        //Ordenação feita a mão
    
        let sus = Number(tarefa);
        let aux2 = 0;
        for(let i = 0;i<vetNum.length;i++){
            if(sus < vetNum[i]){
                aux2 = vetNum[i];
                vetNum[i] = sus;
                sus = aux2;
                boll = 1;
            }else{
                if(boll == 1){
                vetNum[i] = sus;
                }
            }
        }
        vetNum.push(sus);
        `vetNum.push(Number(tarefa));`
    }
    
    `vetNum.sort;`
    for(let i = 0;i<vetNum.length;i++){
        dvQuadro.insertAdjacentHTML("beforeend", `<h5 class='h5_list'>${vetNum[i]}</h5>`)
    }
    }
    
    frm.inTarefa.value = "";
    frm.inTarefa.focus();
    aux++;   

});
*/

/* Metodo 2 */
/*
        for (let i = 0; i < vetNum.length; i++) {
            dvQuadro.innerHTML += `<h5 class='h5_list'>${vetNum[i]}</h5>`
        }
*/