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

$(document).ready(function() { //Falta Ordenar por fecha
    midatatable = $('#midatatable').DataTable({
        "lengthMenu": [
            [5, 25, 50, -1],
            [5, 25, 50, "All"]
        ],
        //"dom": '<"row"<"col-md-6"l><"col-md-6"f>><"row"rt><"row"<"col-md-6"i><"col-md-6"p>>',
        "dom": 'lrtip',
        'columnDefs': [
            { 'sortable': true, 'searchable': false, 'visible': false, 'type': 'num', 'targets': [0] }
        ],
        "order": [
            [0, "desc"]
        ],
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla =(",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            "buttons": {
                "copy": "Copiar",
                "colvis": "Visibilidad"
            }
        }
    });

    $('#midtbusqueda').keyup(function() {
        midatatable.search($(this).val()).draw();
    })

    $('#example').DataTable({
        "processing": true,
        "ajax": {
            "processing": true,
            "url": "justificaciones_list",
            "type": "GET",
            "dataSrc": ""
        },
        "columns": [
            { "data": "descripcion" },
            { "data": "fecha_inicio" },
            { "data": "fecha_fin" },
        ]
    });

    //I got mine working base on https://www.datatables.net/examples/plug-ins/range_filtering.html. Here is my jsfiddle https://jsfiddle.net/bindrid/2bkbx2y3/6/

    $(document).ready(function() {
        /*$.fn.dataTable.ext.search.push(
            function(settings, data, dataIndex) {
                var min = $('#min').val();
                var max = $('#max').val();
                //var min = '02/10/2019';
                //var max = '12/12/2019';
                //console.log($('#min').val());
                var startDate = new Date(data[4]);
                console.log(startDate);
                if (min == null && max == null) return true;
                if (min == null && startDate <= max) return true;
                if (max == null && startDate >= min) return true;
                if (startDate <= max && startDate >= min) return true;
                return false;
            }
        );
        */
        $.fn.dataTableExt.afnFiltering.push(
            function(oSettings, aData, iDataIndex) {
                var iFini = document.getElementById('min').value;
                var iFfin = document.getElementById('max').value;
                var iStartDateCol = 3;
                var iEndDateCol = 3;
                console.log(aData[3]);
                iFini = iFini.substring(6, 10) + iFini.substring(3, 5) + iFini.substring(0, 2);
                iFfin = iFfin.substring(6, 10) + iFfin.substring(3, 5) + iFfin.substring(0, 2);

                var datofini = aData[iStartDateCol].substring(6, 10) + aData[iStartDateCol].substring(3, 5) + aData[iStartDateCol].substring(0, 2);
                var datoffin = aData[iEndDateCol].substring(6, 10) + aData[iEndDateCol].substring(3, 5) + aData[iEndDateCol].substring(0, 2);

                if (iFini === "" && iFfin === "") {
                    return true;
                } else if (iFini <= datofini && iFfin === "") {
                    return true;
                } else if (iFfin >= datoffin && iFini === "") {
                    return true;
                } else if (iFini <= datofini && iFfin >= datoffin) {
                    return true;
                }
                return false;
            }
        );

        $('#min').daterangepicker({
                changeMonth: true,
                changeYear: true,
                singleDatePicker: true,
                locale: {
                    format: 'DD/MM/YYYY',
                    applyLabel: 'Submit',
                    cancelLabel: 'Clear',
                    fromLabel: 'From',
                    toLabel: 'To',
                    customRangeLabel: 'Custom',
                    daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
                    monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                    firstDay: 1
                }
            },
            function(start, end, label) {
                console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
            });

        $('#max').daterangepicker({

            changeMonth: true,
            changeYear: true,
            singleDatePicker: true,
            locale: {
                format: 'DD/MM/YYYY',
                applyLabel: 'Submit',
                cancelLabel: 'Clear',
                fromLabel: 'From',
                toLabel: 'To',
                customRangeLabel: 'Custom',
                daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
                monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                firstDay: 1
            }

        });

        var table = $('#midatatable').DataTable();

        // Event listener to the two range filtering inputs to redraw on input
        $('#min, #max').change(function() {
            table.draw();
        });
    });



});