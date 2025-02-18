from smtplib  import SMTP_SSL
from email.mime.text import MIMEText


servidor =  'smtp.hostinger.com'
porta = 465

usuario = 'temp11@cybersocial.org.br'
senha = '@Aula321'

remetente = usuario
dest = 'payoce5186@noomlocs.com' #email temporario
corpo_email = 'testando mandar email pelo smtplib'
assunto = 'testa da aula'

msg = MIMEText ( corpo_email , 'plain')
msg ['Subject' ] = assunto
msg ['From'] = remetente


print(msg)
con = SMTP_SSL(servidor,porta)
con.login(usuario, senha)
con.sendmail(remetente, dest, msg.as_string())
