const frm = document.querySelector("form");
const resp1 = document.querySelector("#inMaior");
const resp2 = document.querySelector("#inMenor");
const resp3 = document.querySelector("#inMedia");
const resp4 = document.querySelector("#inPares");
const resp5 = document.querySelector("#inImpares");

frm.addEventListener("submit", (e) => {
    e.preventDefault();

    let num = Number(frm.inTam.value);
    if (num == "" || num < 0) {
        swal.fire({
            icon: 'error',
            title: 'Vish...',
            text: 'Valor inválido',
            confirmButtonColor: "#009966",
            iconColor: "#ED2622"
          });
    } else {
        let vet = new Array(num);
        let maior = -1;
        let menor = 999999;
        let media = 0;
        let par = 0;
        let impar = 0;

        for (let i = 0; i < vet.length; i++) {
            let vari = Math.floor(Math.random() * (100 - 0 + 1)) + 0;
            vet[i] = vari;
            media += vet[i];
            if (vet[i] % 2 == 0) {
                par += 1;
            } else {
                impar += 1;
            }

            if (vet[i] > maior) {
                maior = vet[i];
            }

            if (vet[i] < menor) {
                menor = vet[i];
            }
        }

        media = (media / num).toFixed(1);
        resp1.innerText = `Maior:  ${maior}`;
        resp2.innerText = `Menor:  ${menor}`;
        resp3.innerText = `Media:  ${media}`;
        resp4.innerText = `Qtd de Pares:  ${par}`;
        resp5.innerText = `Qtd Impares:  ${impar}`;

    }
    document.getElementById('inTam').value = '';
});