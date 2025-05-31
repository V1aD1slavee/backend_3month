import smtplib
from config import smtp_sender, smtp_sender_password

def send_email(to_email, subject, message):
    sender = smtp_sender
    password = smtp_sender_password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()