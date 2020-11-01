
console.log("se conecto aaaa");

/*document.querySelector("#boton").addEventListener(("click"),traerDatos());*/


function myFunction()
{
    console.log("Dentro de la funcion");
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET','http://127.0.0.1:5000/objeto/list',true)
    xhttp.send();
    xhttp.onreadystatechange=function()
    {
        if(this.readyState==4&&this.status==200)
        {
            console.log(this.responseText);
        }
    }
}



