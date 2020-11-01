let modal = document.getElementById('miModal');
let modal2 = document.getElementById('miModal2');
let modal3 = document.getElementById('miModal3');
let modal4 = document.getElementById('miModal4');
let flex = document.getElementById('flex');
let abrira = document.getElementById('abrir');
let cambio = document.getElementById('cambio');
let cerrar = document.getElementById('close');
let cerrar2 = document.getElementById('close2');
let icono_mostrar = document.getElementById('ocultar_icono');
let ocultar=document.getElementById('ocultar');
var estado =true;

/*abrir.addEventListener('click', function (){
    cambio.innerHTML="deseas aceptar la";
    modal.style.display = 'block';
    
});*/


function abrir_1()
{
    cambio.innerHTML="deseas aceptar la";
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

function myfunction2()
{
    cambio.innerHTML="deseas rechazar la";
    modal.style.display = 'block';
    estado=false;
    return estado;
    
}


function cambiar_estilo()
{

    //ocultar.style.display="none";
    //icono_mostrar.style.display="block";
    $('#ocultar_icono').show(5000);
    
}


function myfunction3()
{


    while(estado==false)
    {
        modal.style.display="none";
        modal2.style.display = 'block';
        break;
    }
    if(estado==true)
    {
        modal.style.display="none";
        modal3.style.display = 'block';
        $('#ocultar').hide(5000);
        
        cambiar_estilo();
    }

    

    /*
    if(myfunction2()==1)
    {
        modal.style.display="none";
        modal2.style.display = 'block';

    }
    else
    {
        if((abrir_1()==9))
        {
            modal.style.display="none";
            modal3.style.display = 'block';

        }
            
          
    }*/


   
}

cerrar2.addEventListener('click', function(){
    modal2.style.display = 'none';
});

function ventana()
{
    modal3.style.display="none";
    modal4.style.display="block";

}

function cerrar_final()
{
    modal4.style.display="none";

}