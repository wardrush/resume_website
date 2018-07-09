from flask import render_template, request
from app.forms import ContactForm
from app import app
from app.email_me import send_notification_email


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        subject = form.subject.data
        email = form.email.data
        message = form.message.data
        send_notification_email(name=name, subject=subject, email=email, message=message)
        return render_template('index.html', form=form)
    elif request.method == 'GET':
        return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)


