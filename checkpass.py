import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Hieu'
email['to'] = '19521512@gm.uit.edu.vn'
email['subject'] = 'text'

email.set_content("I am a python")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pthieu2111@gmail.com', 'hieu021101')
    smtp.send_message(email)
    print('all good boss!')