from smtplib  import SMTP_SSL
from email.mime.text import MIMEText
from dotenv import load_dotenv

import os

load_dotenv()

servidor =  'smtp.hostinger.com'
porta = 465

usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')

remetente = usuario
dest = 'payoce5186@noomlocs.com'
corpo_email = 'testando mandar email pelo smtplib'
assunto = 'testa da aula'

msg = MIMEText ( corpo_email , 'plain')
msg ['Subject' ] = assunto
msg ['From'] = remetente


print(msg)
con = SMTP_SSL(servidor,porta)
con.login(usuario, senha)
con.sendmail(remetente, dest, msg.as_string())
