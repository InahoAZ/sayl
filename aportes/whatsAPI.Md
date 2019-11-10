# Integrar WhatsApp API a tu Aplicacion
## Problema de Version Oficial de WP API
La idea principal era poder usar la API que tiene Whatsapp Buissines (https://www.whatsapp.com/business/api?lang=es)  para integrar el mismo con mi aplicacion, pero esta API esta en una fase Beta, y solo se puede usar solicitando acceso a WhatsApp y para ello se necesita ser una empresa.
## Solucion usando Twilio
Para poder mandar y recibir mensajes por medio de la API de WP, encontre otra solucion que es usar una plataforma que ofrece distintos tipos de servicios de mensajeria para empresas llamado Twilio (www.twilio.com/referral/bOcjxu) donde uno de sus servicios es de hacer de mediador entre WhatsApp y nuestra Aplicacion.

Para esto tenemos que seguir basicamente estos pasos principales.

 1. Registrarnos en la pagina con nuestros correos. (www.twilio.com/referral/bOcjxu)
 
 2. Verificar nuestra cuenta con el email de verificacion que nos manda Twilio.

 3. Luego de este paso, se nos pedira un numero telefonico con WhatsApp y que se verifique con un codigo que proporciona por SMS Twilio.

 4. Una vez registrados al entrar tendremos una mini bienvenida y encuestas acerca de en que usaremos Twilio, es importante decirles que se usara para un proyecto escolar (*Student / Hackaton Project*) y que va a ser para Mensajeria WhatsApp.
 
 5. Una vez contestado la encuesta, nos llevara directamente a lo que nos interesa por eso es importante responder adecuadamente. Nos aparecera un tutorial de como conectar nuestro numero con la Consola de Twilio. Para ello tenemos que enviar un mensaje al numero que nos indica, con el mensaje que nos indica. (Seguir los pasos :v)

	Es importante esta parte para poder crear el numero ya aprobado por wpp que nos proporciona Twilio y que usaremos como mediador.
	
	Seguir las demostraciones para mandar mensajes, recibir mensajes y contestar en base a lo recibido.
	
	Tutorial mas detallado aca:
	https://www.twilio.com/docs/sms/whatsapp/quickstart/python

	Cabe aclarar que los tutoriales estan disponibles para varios lenguajes, basta con elegir para cual queremos en el listado que aparece acá;
	https://www.twilio.com/docs/sms/whatsapp/quickstart

 
6. Para poder enviar y recibir mensajes desde nuestra aplicacion necesitamos descargar la libreria para hacer consultas Twilio para el lenguaje correspondiente y que haga de mediador entre nuestra aplicacion y WP, cabe aclarar que como se necesita aprobacion de WP para utilizar la API, Twilio nos proporciona un numero ya aprobado para realizar pruebas. 
En el caso de Python la libreria se descarga mediante pip (https://www.twilio.com/docs/libraries/python):

    ```console
    foo@bar:~$ pip install twilio
    ```

	Basicamente para mandar mensajes seguir este tutorial:
https://www.twilio.com/docs/sms/whatsapp/quickstart/python
