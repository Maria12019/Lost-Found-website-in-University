var piso=document.getElementById("Piso");

var error=document.getElementById("error");

/*for(var i=0; i<obj.length; i++){
    var obj2 = document.createElement("option");
    obj2.setAttribute("value",obj[i].id);
    obj2.innerHTML = obj[i].name;
    locales.appendChild(obj2);
} */

var estado1=false;
piso.addEventListener("input", maxPisos)

function maxPisos(){

    cadena=piso.value;
    if(cadena.length>2){
        error.style.visibility="visible";
        error.innerHTML=b2+" El piso no debe ser mayor a 2 dígitos";
        estado1=false; 

    }
    else {
        if(cadena.length==0){
            error.style.visibility="visible";
            estado1=false;
            error.innerHTML=a2+" El campo Piso se encuentra vacio, por favor completar";
        }
        else{
            error.style.visibility="hidden";
            estado1=true;

        }
    }
    console.log(estado1);

}