from threading import Thread
from flask import render_template, url_for
from flask_mail import Message
import os
from app import app, mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_notification_email(name, email, subject, message):
    send_email('[Resume Site] Someone Contacted You!',
               sender=os.environ.get('MAIL_USERNAME'),
               recipients=os.environ.get('MAIL_PERSONAL'),
               html_body=render_template(url_for('static', filename='contact.html'), name=name, email=email, subject=subject,
                                         message=message)
               )

