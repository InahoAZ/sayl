$(".test").click(function() {

    Swal.fire({
        title: 'Estas seguro que desea eliminar?',
        text: "No se puede deshacer estos cambios",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar'
    }).then((result) => {
        if (result.value) {
            $.ajax({
                url: `/app_tipojustificacion/eliminar_tjust/51`,
                type: 'get',
                success: function(data) {
                    alert("todo liyo");
                    $(".datatable").load(" .datatable");
                }
            });
            Swal.fire(
                'Eliminado',
                'Se borro el registro seleccionado',
                'success'
            );
            alert('{{tipojust.pk}}');
            //window.location.href = "url";
            //$('#content').load(url);
        }
    })

});