import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# need to store username & password  in Environment variables for security purposes
username = 'pyjohndoepy@gmail.com'
password = 'pythonpython20'

def send_mail(text='Email Body', subject='Hello world!', from_email ='John Doe <pyjohndoepy@gmail.com>', to_emails =None, html=None):
    assert isinstance(to_emails ,list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    # login to the SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username , password )
    server.sendmail(from_email,to_emails, msg_str)


    server.quit()

