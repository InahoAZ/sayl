function prueba7(legajo, nombre, apellido, licenciaMedica) {

    //document.getElementById("legajoNoFake").style.display = 'none';
    document.getElementById("legajoNoFake").textContent = legajo;
    document.getElementById("nombreNoFake").textContent = nombre;
    document.getElementById("apellidoNoFake").textContent = apellido;
    document.getElementById("licenciaMedicaNoFake").textContent = licenciaMedica;
};


$(".fechona").blur(function() { //Para los input con la clase fechona, cuando se pierde el foco en el mismo (blur)
    var date = Date.parse($(this).val()); //guardo lo que hay en el input y lo transformo a fecha para poder comparar
    if (date < Date.now()) { //Si la fecha del input es menor a la de hoy...
        $(".mensaje_toggle").show();
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'La fecha es invalida',
            footer: 'Las fecha debe ser de hoy en adelante'
        })
        $(this).val(''); //Limpia el input, pero se puede hacer lo que se quiera
    }

});

$(document).ready(function() {
    $('#midatatable').DataTable({
        "lengthMenu": [
            [5, 25, 50, -1],
            [5, 25, 50, "All"]
        ],
        "columnDefs": [{
            "type": "date-euro",
            "targets": 3
        }],
        "order": [
            [3, "desc"]
        ]
    });

});