/*
function traerDetalleSol() {
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET', '/sol_usu/detalle?soliId=' + soliId, true);
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            switch (xhttp.status) {
                case 200:
                    myFunction(JSON.parse(xhttp.responseText));
                    console.log('hola');
                    break;
            }
        }
    }
    xhttp.send();
}

function myFunction(datos) {
    var variable = document.getElementById("detalleSoli");
    var a = variable.childNodes[1].id;
    let miNodo = document.createElement('ul');
    miNodo.classList.add('pd-tags');

    for (let item of datos) {
        let miNodoLiTitle = document.createElement('li');
        let miNodoTitle = document.createElement('span');
        miNodoTitle.textContent = "NRO. SOLICITUD:" + item.nro_solicitud;

        let miNodoLiFechaEnv = document.createElement('li');
        let miNodoFechaEnv = document.createElement('span');
        miNodoFechaEnv.textContent = "FECHA DE ENVÍO DE LA SOLICITUD:" + item.fecha_envio;

        miNodoLiTitle.appendChild(miNodoTitle);
        miNodoLiFechaEnv.appendChild(miNodoFechaEnv);

        miNodo.appendChild(miNodoLiTitle);
        miNodo.appendChild(miNodoLiFechaEnv);

        document.getElementById("detalleSoli").appendChild(miNodo);
    }
}

function prueba(){
    console.log('holis'+soliId);
}
body.onload = prueba();*/