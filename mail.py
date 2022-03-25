import smtplib
from email.mime.text import MIMEText

sender = 'ibrahimalgerie2014@gmail.com'
sender_password = ''
receivers = ['gi_berkane@esi.dz', 'zeggarihaithem@gmail.com']
body_of_email = 'Apartment available.'
subject_of_email = 'Apartment available in Crous.'


def build_email():
    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = subject_of_email
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    return msg


def send_email():
    print("Sending email...")
    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.login(user=sender, password=sender_password)
    s.sendmail(sender, receivers, build_email().as_string())
    s.quit()
    print("Successful sending...")
