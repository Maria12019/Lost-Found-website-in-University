/*****************Modal para cierre solicitud de objeto usuario*******************/
$(".objeto5").click(function(){
    Swal.fire({
      title: "Ingrese las características del objeto",
      input: 'textarea',
      inputPlaceholder: 'Escriba las características aquí...',
      inputAttributes: {
        'caract': 'caractObj'
      },
      confirmButtonText: "OK",
      showCancelButton: true,
      confirmButtonColor: '#3085d6'
    }).then((result)=>{
        if(result.isConfirmed){
            Swal.fire({
                title: '¿Está seguro de enviar la solicitud?',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: 'grey',
                confirmButtonText: 'Enviar'
              }).then((result) => {
                if (result.isConfirmed) {
                  $('#obj1').submit(); //agregado 
                  Swal.fire(
                    '¡Listo!',
                    'La solicitud ha sido enviada con éxito.',
                    'success',
                  )
                }
              })
        }
    })
    if (text) {
        Swal.fire(text)
      }
});

/*****************Modal para cierre de sesión*******************/
$("#registrar_1").click(function(){
    Swal.fire({
        title: '¿Está seguro de que desea cerrar sesión?',
        showCancelButton: true,
        confirmButtonColor: '#e77b3c',
        cancelButtonColor: 'grey',
        confirmButtonText: 'OK'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/logout";
        }
      })
});

