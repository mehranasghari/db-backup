import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import time

def send_mail(address, subject, message, delay):
    load_dotenv()
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT'))

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = address
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        time.sleep(delay)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to address: {address}")
    except Exception as e:
        print(f"Failed to send email: {e}")