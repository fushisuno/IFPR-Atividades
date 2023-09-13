const frm = document.querySelector("form");
const dvPalco = document.querySelector("#divPalco");
const poltronas = 240;
const reservadas = [];


window.addEventListener("load", ()=>{
    for(let i = 1;i < 241; i++){
      const figure = document.createElement("figure");
      const imgStatus = document.createElement("img");

      imgStatus.src = "./assets/img/ocupada.jpg";

      const figureCap = document.createElement("figcaption");
      
      const zeros = i<10 ? "00": i<100? "0": "";

      // Cria o número da poltrona
      const num = document.createTextNode(`${zeros}${i}`);


      figureCap.appendChild(num);
      figure.appendChild(imgStatus);
      figure.appendChild(figureCap);

      dvPalco.appendChild(figure);
    }
});

