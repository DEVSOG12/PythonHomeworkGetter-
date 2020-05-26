import smtplib

import config as config

import anays as george

import oreofe as oreofe

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(oreofe.EMAIL_ADDRESS, oreofe.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Oreofe's Assignment "
msg = 'george.results'

send_email(subject, msg)