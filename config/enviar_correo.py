from email.mime.text import MIMEText # ==> MIME extensión multipropósito
import smtplib
from email.mime.multipart import MIMEMultipart 
from os import environ


mensaje = MIMEMultipart()
mensaje['From'] = environ.get('EMAIL')
mensaje['Subject'] = 'Solicitud de restauración de la contraseña'
password = environ.get('EMAIL_PASSWORD')
# print(password)

def enviarCorreo(destinatario, cuerpo):
    '''Función pque sirve para enviar un correo'''
    mensaje['To'] = destinatario
    texto = cuerpo
    mensaje.attach(MIMEText(texto, 'html'))
    try:
        servidorSMTP = smtplib.SMTP('smtp.gmail.com',587) # ==> Configuración de servidor SMTP.
        servidorSMTP.starttls() # ==> Protocolo de transferencia.
        servidorSMTP.login(user=mensaje.get('From'), password=password) # ==> Sesión en el servidor de correos con las credenciales. 
        servidorSMTP.sendmail(
            from_addr=mensaje.get('From'),
            to_addrs=mensaje.get('To'),
            msg=mensaje.as_string()
        )
        servidorSMTP.quit() # ==> Cerrar sesión de correo
    except Exception as e:
        print(e)
