import smtplib
import datetime
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# E-mail configuration
host = os.environ.get("SMTP_HOST")
port = os.environ.get("SMTP_PORT")
user = os.environ.get("MAIL_USER")
password = os.environ.get("MAIL_PASS")


def sendNotification(df):

    print('Creating server object...')
    server = smtplib.SMTP(host, port)

    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    message = createMessage(df)
    print('Creating message...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = 'antoniomellies@gmail.com'
    email_msg['Subject'] = createSubjet()

    print('Adding text...')
    email_msg.attach(MIMEText(message, 'html'))

    print('Sending message...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    print('Message sent successfully!')
    server.quit()


def createSubjet():
    subject = 'Pendencias Contabilidade -'
    date = datetime.datetime.now()
    return f'{subject} {date.day}/{date.month}/{date.year}'


def createMessage(df):
    # Prepare DF
    df = df.groupby(['Responsável'])['Responsável'].count().reset_index(name="Quantidade")
    df['Responsável'].replace('', 'SEM RESPONSAVEL', inplace=True)

    message = '<h3>Existem pendências esperando para serem resolvidas</h3>'
    message += '<br>'
    message += df.to_html(justify='center', border=2)
    message += '<br>'
    message += f'<a href="{os.environ.get("URL_SPREADSHEET")}">Link da planilha</a>'
    message += f'<p style="font-size: 0.7em;">{createSubjet()}</p>'

    file1 = open("email.html", "w")
    file1.write(message)
    file1.close()

    return message
