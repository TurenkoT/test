import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['test@test.com']
msg = MIMEMultipart()
sender = 'sender@test.com'
subject = "Отчет"
body = "Добрый день!\nВо вложении отчет"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
# print text
# Send the message via our SMTP server
s = smtplib.SMTP('exchange.test.com')
s.sendmail(sender, address_book, text)
s.quit()