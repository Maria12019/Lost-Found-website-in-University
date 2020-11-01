let modal = document.getElementById('miModal');
let modal4 = document.getElementById('miModal4');
let flex = document.getElementById('flex');
let abrira = document.getElementById('abrir');
let cerrar = document.getElementById('close');
var estado =true;

function abrir_1()
{
    modal.style.display = 'block';
    estado=true;
    return estado;
}

cerrar.addEventListener('click', function(){
    modal.style.display = 'none';
});

window.addEventListener('click', function(e){
    console.log(e.target);
    if(e.target == flex){
        modal.style.display = 'none';
    }
});

function myfunction()
{
    modal.style.display = 'none';
}

function myfunction3()
{
    while(estado==false)
    {
        modal.style.display="none";
        break;
    }
    if(estado==true)
    {
        modal.style.display="none";
        modal4.style.display = 'block';
        cambiar_estilo();
    }
}

function ventana()
{
    modal.style.display="none";
    modal4.style.display="block";
}

function cerrar_final()
{
    modal4.style.display="none";
}