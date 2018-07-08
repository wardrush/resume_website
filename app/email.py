from flask_mail import Message
from app import mail
import os



def send_email(subject, sender, text_body):
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    msg = Message(subject, sender=MAIL_USERNAME, recipients=MAIL_USERNAME)
    msg.body = text_body