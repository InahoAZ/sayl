from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from login.models import CustomUser

# Create your views here.

def mandar_mail(users_to, asunto, mensaje):
    # subject = 'Thank you for registering to our site'
    # message = ' it  means a world to us '

    email_from = settings.EMAIL_HOST_USER    
    
    #Arma lista con todos los mail a avisar.
    para = []
    for user_to in users_to:
        contacto_usuario = CustomUser.objects.get(pk=user_to)
        para.append(contacto_usuario.email)

    send_mail(asunto, mensaje, email_from, para) 
    
    #return redirect('redirect to a new page')

def mandar_whatsapp(users_to, mensaje): #FUncion comun para mandar mensajes por wpp

    account_sid = 'AC07ab30ceb21fe363d6ed1027b8df8725' 
    auth_token = '8783e451a24540b7a2371d686ceefecc' 
    client = Client(account_sid, auth_token) 
    
    for user_to in users_to:
        contacto_usuario = CustomUser.objects.get(pk=user_to)
        contacto_usuario = contacto_usuario.telefono
        numero = 'whatsapp:' + contacto_usuario.prefijo + '9' + contacto_usuario.caracteristica + contacto_usuario.numero
        print(numero)
    
        message = client.messages.create(
                                    from_='whatsapp:+14155238886',  
                                    body=mensaje,      
                                    to=numero
                                    ) 
        print(message.sid)
    # return redirect('index')
    
