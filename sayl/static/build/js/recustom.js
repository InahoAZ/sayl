function prueba7(legajo, nombre, apellido, licenciaMedica) {

    //document.getElementById("legajoNoFake").style.display = 'none';
    document.getElementById("legajoNoFake").textContent = legajo;
    document.getElementById("nombreNoFake").textContent = nombre;
    document.getElementById("apellidoNoFake").textContent = apellido;
    document.getElementById("licenciaMedicaNoFake").textContent = licenciaMedica;
};

function formato(texto) {
    return texto.replace(/^(\d{4})-(\d{2})-(\d{2})$/g, '$3-$2-$1');
}


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
    $('#min').val('');
    $('#max').val('');
    midatatable = $('#midatatable').DataTable({
        "orderCellsTop": true,
        "fixedHeader": true,
        "lengthMenu": [
            [5, 10, 25, 50, -1],
            [5, 10, 25, 50, "Todos"]
        ],
        //"dom": '<"row"<"col-md-6"l><"col-md-6"f>><"row"rt><"row"<"col-md-6"i><"col-md-6"p>>',
        "dom": "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>" +
            "<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        "iDisplayLength": 5,
        initComplete: function() {
            console.log("Carga2");
            $('#min').val('');
            $('#max').val('');
            var columnas_permitidas = $('.dt_filtrable');
            this.api().columns(columnas_permitidas).every(function() {
                var column = this;
                var select = $('<select class="select2"><option value=""></option></select>')
                    .appendTo($(column.footer()).empty())
                    .on('change', function() {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                        console.log(column.index())
                    });
                console.log()
                column.data().unique().sort().each(function(d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
            var columnas_rangos = $('.dt_rango_fecha');
            this.api().columns(columnas_rangos).every(function() {
                var column = this;
                var select = $('<input class="" id="min">')
                    .appendTo($(column.footer()).empty())
                    .on('change', function() {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        $.fn.dataTableExt.afnFiltering.push(
                            function(oSettings, aData, iDataIndex) {
                                var iFini = document.getElementById('min').value;
                                var rango = iFini.split(' - ');
                                if (rango.length > 1) {
                                    var iFini = rango[0]
                                    var iFfin = rango[1];
                                } else {
                                    var iFfin = '';
                                }
                                console.log(iFini, "***", iFfin);
                                //var iFfin = document.getElementById('max').value;
                                var iStartDateCol = column.index();
                                var iEndDateCol = column.index();
                                console.log("dato: ", aData[column.index()]);
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
                        column
                        //.search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                        console.log(column.index())
                    });
                console.log()

                // column.data().unique().sort().each(function(d, j) {
                //     select.append('<option value="' + d + '">' + d + '</option>')
                // });
            });
            var columnas_time = $('.dt_time_range_2col');
            console.log("LEN: ", columnas_time.length)
            this.api().columns(columnas_time).every(function() {
                var column = this;
                var select = $('<input class="col col-md-5" id="hs_min' + column.index() + '"><div class="col col-md-2 text-center"><p><br>-</p></div><input  class="col col-md-5"  id="hs_max' + column.index() + '">')
                    .appendTo($(column.footer()).empty())
                    .on('change', function() {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        $.fn.dataTableExt.afnFiltering.push(
                            function(oSettings, aData, iDataIndex) {
                                var iFini = document.getElementById('hs_min' + column.index() + '').value;
                                var iFfin = document.getElementById('hs_max' + column.index() + '').value;

                                //var iFfin = document.getElementById('max').value;
                                var iStartDateCol = column.index();
                                var iEndDateCol = column.index();
                                //console.log("dato2: ", aData[column.index() + 1]);

                                console.log(iFini);
                                iFini = iFini.substring(0, 2) + iFini.substring(3, 5) + iFini.substring(6, 8);
                                console.log(iFini);
                                iFfin = iFfin.substring(0, 2) + iFfin.substring(3, 5) + iFfin.substring(6, 8);

                                var datofini = aData[iStartDateCol].substring(0, 2) + aData[iStartDateCol].substring(3, 5) + aData[iStartDateCol].substring(6, 8);
                                var datoffin = aData[iEndDateCol].substring(0, 2) + aData[iEndDateCol].substring(3, 5) + aData[iEndDateCol].substring(6, 8);
                                console.log(iFini, "|", datofini, "|", datoffin, "|", iFfin)
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
                        column
                        //.search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                        console.log(column.index())
                    });
                console.log()

                // column.data().unique().sort().each(function(d, j) {
                //     select.append('<option value="' + d + '">' + d + '</option>')
                // });
            });





        },
        "buttons": [{
            extend: 'pdfHtml5',
            className: '',
            text: '<i class="fa fa-file-pdf-o text-left"></i>PDF',
            //Aca le digo que solo los <th> que NO tengan la class="noExport" aparezcan en el reporte
            exportOptions: {
                columns: ':not(.noExport)'
            },
            select: true,
            filename: 'reporte_pdf',
            orientation: 'portrait', //landscape
            pageSize: 'A4', //A3 , A5 , A6 , legal , letter
            customize: function(doc) {
                //El titulo lo saco de un input oculto para poder usar esta misma configuracion para reportes distintos, entonces cambia el titulo segun el reporte.
                var titulo = $('#titulo_reporte').val();
                var usuario = $('#usuario_reporte').val();
                var filtros = [];
                var inputs = $(".filter");

                //Voy agregando a un array todos los filtros que se hayan usado (los inputs tienen que tener la class="filter" y un name, ya que el name le da el titulo del filtro.)
                for (var i = 0; i < inputs.length; i++) {
                    if ($(inputs[i]).val() != "") {
                        filtros.push($(inputs[i]).attr("name") + ": " + $(inputs[i]).val() + "\n")
                    }
                }
                if (filtros.length == 0) {
                    filtros.push("No se aplicaron Filtros");
                }
                //Transformo todo en un string.
                var filtrostr = filtros.join(" ");
                //quitamos el titulo por defecto del pdfhtml5 eliminando el primer elemento del pdf que esta en el array content.
                //doc.content.splice(0, 1);
                doc.content[0] = [{ text: titulo + "\n", bold: true, alignment: "left", fontSize: 10 }, { text: 'Filtros: ', bold: true, alignment: "left" }, { text: filtrostr, alignment: "left" }];
                //console.log(doc.content[0]);
                //Fecha para usar en el reporte mas adelante
                var now = new Date();
                var jsDate = now.getDate() + '-' + (now.getMonth() + 1) + '-' + now.getFullYear();

                //Para poner una imagen hay que convertirla a Base64 con esta pagina se puede:
                // http://codebeautify.org/image-to-base64-converter


                //#region aca esta el logo en base64 (expandir, es muy largo xd)
                var logo = 'data:image/png;base64,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';
                //#endregion



                // Ahora establecemos los margenes: [left,top,right,bottom] o [horizontal,vertical]
                // si ponemos solo un numero se establece ese mismo para todos los margenes
                doc.pageMargins = [20, 135, 20, 50];

                // Tamaño de fuente de todo el documento
                doc.defaultStyle.fontSize = 9;
                // Tamaño de fuente del encabezado
                doc.styles.tableHeader.fontSize = 10;

                //Al elemento 0 (porque borre el titulo al principio) del contenido o sea la tabla
                //lo centramos forzadamente
                //doc.content[0].margin = [100, 0, 100, 0]

                // Para personalizar el encabezado:
                // Creamos un encabezado con 3 columnas
                // A la izquierda: Logo
                // En el medio: Titulo
                // A la derecha: algo xd
                var univ = $('#universidad').val()
                var facultad = $('#facultad').val()
                var direccion = $('#direccion').val()
                doc['header'] = (function() {
                    return {
                        columns: [{
                                image: logo,
                                width: 100,
                                margin: [0, 50, 0, 0]
                            },
                            {
                                alignment: 'center',
                                text: [{ text: "Facultad de Ciencias Económicas" + '\n', bold: true, fontSize: 12 }, { text: "Carlos Pellegrini 269, N3350 Apóstoles, Misiones \n Teléfono: 03758 42-3232 \n \n \n" }],
                                fontSize: 10,
                                margin: [0, 20, 0, 0]
                            },
                            {
                                alignment: 'right',
                                fontSize: 9,
                                text: [{ text: 'Fecha: ', bold: true }, { text: jsDate.toString() }, { text: '\n Generado por: ', bold: true }, { text: usuario + "\n" }],
                                width: 80,
                                margin: [0, 10, 0, 0],
                                alignment: 'left'
                            }
                        ],
                        margin: 20
                    }
                });
                // Create a footer object with 2 columns
                // Left side: report creation date
                // Right side: current page and total pages
                doc['footer'] = (function(page, pages) {
                    return {
                        columns: [{
                                alignment: 'left',
                                text: ['Generado el: ', { text: jsDate.toString() }],
                                fontSize: 9,
                            },
                            {
                                alignment: 'right',
                                text: ['Pagina ', { text: page.toString() }, ' de ', { text: pages.toString() }],
                                fontSize: 9,
                            }
                        ],
                        margin: 20
                    }
                });
                //Funcion que pone cada columna en tamaño *, para que se ajuste automagicamente. cuenta cada <td> del data table y genera array del tipo [*,*,*,..,n] y establece dicho array como width.
                var colCount = new Array();
                //console.log(table.data().count());

                //Para saber si la tabla esta vacia o nel pastel.
                var esVacio;
                //Captura el mensaje del datatable cuando esta vacio
                var tdvacio = $('.dataTables_empty').html()
                if (tdvacio == 'No se encontraron resultados') {
                    esVacio = true;
                } else {
                    esVacio = false;
                }

                if (!esVacio) {
                    $("#midatatable").find('tbody tr:first-child td').each(function() {
                        if ($(this).attr('colspan')) {
                            for (var j = 1; j <= $(this).attr('colspan'); $j++) {
                                colCount.push('*');
                            }
                        } else { colCount.push('*'); }
                    });
                    console.log(colCount);
                    doc.content[1].table.widths = colCount;
                }

                //console.log(colCount);
                //colCount.push('*'); //Le pongo uno mas porque tengo un td oculto (el id)


                //Es equivalente a: doc.content[0].table.widths = ['*', '*', '*', '*', '*', '*'];


                // Para personalizar el pie de pagina:
                // Creamos un objeto de pie de pagina con dos columnas
                // Lado izquierdo: Fecha de creacion del reporte
                // Lado derecho: pagina actual y total de pagina
                // doc['footer'] = (function(page, pages) {
                //     return {
                //         columns: [{
                //                 alignment: 'left',
                //                 text: ['Fecha de Generacion: ', { text: jsDate.toString() }]
                //             },
                //             {
                //                 alignment: 'right',
                //                 text: ['pagina ', { text: page.toString() }, ' de ', { text: pages.toString() }]
                //             }
                //         ],
                //         margin: 20
                //     }
                // });

                // Change dataTable layout (Table styling)
                // To use predefined layouts uncomment the line below and comment the custom lines below
                // doc.content[0].layout = 'lightHorizontalLines'; // noBorders , headerLineOnly
                var objLayout = {};
                objLayout['hLineWidth'] = function(i) { return 1; };
                objLayout['vLineWidth'] = function(i) { return 1; };
                objLayout['hLineColor'] = function(i) { return '#aaa'; };
                objLayout['vLineColor'] = function(i) { return '#aaa'; };
                objLayout['paddingLeft'] = function(i) { return 4; };
                objLayout['paddingRight'] = function(i) { return 4; };
                doc.content[1].layout = objLayout;
            },
        }],
        "pageLength": 100,
        "processing": true,
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
            "sEmptyTable": "Ningún dato disponible en esta tabla",
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
    midatatable.rows({ selected: true }).data();

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

        var interval = setInterval(function() {
            var momentNow = moment();
            $('#date-part').html(momentNow.format('dddd').substring(0, 3).toUpperCase() + ' ' + momentNow.format('DD MM YYYY')

            );
            $('#time-part').html(momentNow.format('HH:mm:ss'));
        }, 100);

    });


    $(document).ready(function() {
        $('#min').val('');
        $('#max').val('');
        $('#daterangepicker').val('').change();
        $('#midtbusqueda').val('');
        midatatable.search('').draw();
        midatatable.draw();
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
        // $.fn.dataTableExt.afnFiltering.push(
        //     function(oSettings, aData, iDataIndex) {
        //         var iFini = document.getElementById('min').value;
        //         var rango = iFini.split(' - ');
        //         if (rango.length > 1) {
        //             var iFini = rango[0]
        //             var iFfin = rango[1];
        //         } else {
        //             var iFfin = document.getElementById('max').value;
        //         }
        //         //var iFfin = document.getElementById('max').value;
        //         var iStartDateCol = 3;
        //         var iEndDateCol = 3;
        //         console.log("dato: ", aData[3]);
        //         iFini = iFini.substring(6, 10) + iFini.substring(3, 5) + iFini.substring(0, 2);
        //         iFfin = iFfin.substring(6, 10) + iFfin.substring(3, 5) + iFfin.substring(0, 2);

        //         var datofini = aData[iStartDateCol].substring(6, 10) + aData[iStartDateCol].substring(3, 5) + aData[iStartDateCol].substring(0, 2);
        //         var datoffin = aData[iEndDateCol].substring(6, 10) + aData[iEndDateCol].substring(3, 5) + aData[iEndDateCol].substring(0, 2);

        //         if (iFini === "" && iFfin === "") {
        //             return true;
        //         } else if (iFini <= datofini && iFfin === "") {
        //             return true;
        //         } else if (iFfin >= datoffin && iFini === "") {
        //             return true;
        //         } else if (iFini <= datofini && iFfin >= datoffin) {
        //             return true;
        //         }
        //         return false;
        //     }
        // );

        $('#min').daterangepicker({
                changeMonth: true,
                changeYear: true,
                singleDatePicker: false,
                locale: {
                    format: 'DD/MM/YYYY',
                    applyLabel: 'Aceptar',
                    cancelLabel: 'Limpiar',
                    fromLabel: 'Desde',
                    toLabel: 'Hasta',
                    customRangeLabel: 'Personalizado',
                    daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
                    monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                    firstDay: 1
                },
                drops: 'up',
                ranges: {
                    'Hoy': [moment(), moment()],
                    'Ayer': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                    'Ultimos 7 Días': [moment().subtract(6, 'days'), moment()],
                    'Ultimos 30 Días': [moment().subtract(29, 'days'), moment()],
                    'Este Mes': [moment().startOf('month'), moment().endOf('month')],
                    'Mes Anterior': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
                },
                alwaysShowCalendars: true,
            },
            // function(start, end, label) {
            //     $('#min').val(start.format('DD-MM-YYYY'));
            //     console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));


            // }
        );

        $('#min').on('cancel.daterangepicker', function(ev, picker) {
            //do something, like clearing an input
            $('#min').val('');
            midatatable.search('').draw();
            table.draw();
        });

        $('#daterangepicker').daterangepicker({

            changeMonth: true,
            changeYear: true,
            singleDatePicker: false,
            locale: {
                format: 'DD/MM/YYYY',
                applyLabel: 'Aceptar',
                cancelLabel: 'Limpiar',
                fromLabel: 'Desde',
                toLabel: 'Hasta',
                customRangeLabel: 'Personalizado',
                daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
                monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                firstDay: 1
            },
            drops: 'down',
            opens: 'left',
            ranges: {
                'Hoy': [moment(), moment()],
                'Ayer': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                'Ultimos 7 Días': [moment().subtract(6, 'days'), moment()],
                'Ultimos 30 Días': [moment().subtract(29, 'days'), moment()],
                'Este Mes': [moment().startOf('month'), moment().endOf('month')],
                'Mes Anterior': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
            },
            alwaysShowCalendars: true,

        });
        $('#daterangepicker').on('cancel.daterangepicker', function(ev, picker) {
            //do something, like clearing an input
            $('#daterangepicker').val('').change();

        });

        var table = $('#midatatable').DataTable();
        table.rows({ selected: true }).data();
        // Event listener to the two range filtering inputs to redraw on input
        $('#min, #max').change(function() {
            table.draw();
        });

        $('#headingTwo').click(function() {
            $('#min').val('');
            $('#max').val('');
            $('#midtbusqueda').val('');
            midatatable.search('').draw();
            table.draw();
        });

        $('#cleanfilters').click(function() {
            $('#min').val('');
            $('#max').val('');
            $('#midtbusqueda').val('');
            midatatable.search('').draw();
            table.draw()
        });

        //para hacer seleccionable las filas de mi datatable
        $('#midatatable tbody').on('click', 'tr', function() {
            if ($(this).hasClass('selected')) {
                $(this).removeClass('selected');
            } else {
                table.$('tr.selected').removeClass('selected');
                $(this).addClass('selected');
            }

        });
    });
    var table = $('#midatatable').DataTable();
    $('#midatatable tbody').on('click', 'tr', function() {
        var datos = table.row(this).data()
        console.log(datos[0]);
        $.ajax({
            url: 'justificaciones_list/' + datos[0],
            type: 'get',
            dataType: 'json',
            success: function(data) {
                console.log(table.row('.selected').data());
                console.log(data[0]);
                console.log("AJAX OK");
                $('#legajo-txt').html(String(data[0]['legajo']['legajo']));
                $('#apellido-txt').html(data[0]['legajo']['last_name']);
                $('#nombre-txt').html(data[0]['legajo']['first_name']);
                $('#tjust-txt').html(data[0]['tipo_justificacion']['motivo']);
                $('#fsol-txt').html(formato(data[0]['fecha_solicitud']));
                $('#fdesde-txt').html(formato(data[0]['fecha_inicio']));
                $('#fhasta-txt').html(formato(data[0]['fecha_fin']));
                $('#btn-aprobar').attr("href", "/app_justificacion/aprobar_just/" + data[0]['pk']);
                $('#btn-rechazar').attr("href", "/app_justificacion/rechazar_just/" + data[0]['pk']);
                $('#id_just').attr("value", data[0]['pk'])

            }
        });

        // 
        // 
        // //

    });


    $('#min').val('');
    $('#max').val('');
    $('#select-cargo').ready(function() { //no anda
        $('.selDiv option:eq(2)');
    });

    //Dos combobox, al seleccionar uno se hace una consulta a la bd y se rellena el otro.
    $('#select-cargo').change(function() {
        var cg = $(this).val();

        $.ajax({
            url: '/app_tipojustificacion/tipos_justificacion_list',
            data: {
                'cargo': cg,
            },
            dataType: 'json',
            success: function(data) {
                var html = "";
                for (var i = 0; i < data.length; i++) {

                    html += "<option value='" + data[i].pk + "'>" + data[i].motivo + "</option>";
                }
                $('#select-just').html(html);
            }
        })
    });



    //Para filtrar cada columna de un datatable.
    $(document).ready(function() {
        // Setup - add a text input to each footer cell
        $('#midatatabl thead tr').clone(true).appendTo('#midatatabl thead');
        $('#midatatabl thead tr:eq(1) th').each(function(i) {
            var title = $(this).text();
            $(this).html('<input type="text" placeholder="Buscar por ' + title + '" />');

            $('input', this).on('keyup change', function() {
                if (table.column(i).search() !== this.value) {
                    table
                        .column(i)
                        .search(this.value)
                        .draw();
                }
            });
        });





    });

    $('#just-cargo').change(function() {
        console.log("Algo");
        if (this.checked) {
            $('#select-cargo').collapse('show')
        } else {
            $('#select-cargo').collapse('hide')
        }
    });









    //Select 2 multiple, para mandar mensajes a usuarios.
    $(document).ready(function() {
        $('.to').select2();
        //console.log("oli");

        $('.select2').select2();

        console.log("la wea");
        $('#min').val('');
        $('#max').val('');
        $('#daterangepicker').val('');

    });



    (function($) {
        $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
            if (!$(this).next().hasClass('show')) {
                $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
            }
            var $subMenu = $(this).next(".dropdown-menu");
            $subMenu.toggleClass('show');

            $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
                $('.dropdown-submenu .show').removeClass("show");
            });

            return false;
        });
    })(jQuery)


    // //Rellenar Mis Cargos
    // $('#perfil').click(function() {
    //     console.log('hghghhghgh');
    //     $.ajax({
    //         url: '/cargos/mis_cargos_list',
    //         success: function(data) {
    //             var html = "";
    //             for (var i = 0; i < data.length; i++) {

    //                 html += "<li> <a href='cargos/switch_cargo/" + data[i].cargo + "'>" + data[i].desc_categ + "</li>";
    //             }
    //             $('#mis_cargos').html(html);
    //         }
    //     })
    // });


    $(document).ready(function() {
        $('#min').val('');
        $('#max').val('');
        $('#daterangepicker').val('').change();
        $('#midtbusqueda').val('');
        midatatable.search('').draw();
        table.draw();
        // console.log("COSO");
        // console.log($("progress-bar, progress-bar-success").attr("data-transitiongoal"));
        // console.log($(this).find('div[data-transitiongoal]').attr('data-transitiongoal'));

        // var progresbar_value = $(this).find('div[data-transitiongoal]').attr('data-transitiongoal')
        $('[data-toggle="tooltip"]').tooltip();

    });





});

function msj_finalizar_hs_mayor() {
    Swal.fire({
        type: 'error',
        title: 'Oops...',
        text: 'Usted ha excedido las horas a cumplir que le corresponde según su cargo',
    })
}

function msj_finalizar_hs_menor() {
    Swal.fire({
        type: 'error',
        title: 'Oops...',
        text: 'Aun no declaro todas las horas para su cargo',
    })
}