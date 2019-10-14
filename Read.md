# Cosas que todavia me faltar pulir:

- Al cargar el template de avisar inasistencia, los tipos de justificacion se cargan desde el formulario en vez desde la seleccion del cargo con js. Esto hace que la restriccion de tipo de justificacion segun el cargo solo funcione al seleccionar una vez un cargo. Al cargar la pagina si no se toca los cargos se listan todos los tipos de justificacion.

- Cuando se carga el template, los filtros de fecha inicio y fin estan con un valor por defecto, aunque ocultos, pero al ordenar se toma esa fecha por defecto y se filtra la tabla. Tengo que ver que al cargar la pagina esos inputs comiencen en blanco.