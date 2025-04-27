# file: flask_mail_app.py

# Demonstrates sending emails using Flask-Mail

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'mail_demo_secret'

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'           # Use your email provider
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'   # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'          # Replace with app password or real password

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        to = request.form['to']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject=subject,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[to],
                      body=message)

        try:
            mail.send(msg)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'danger')
        return redirect(url_for('index'))

    return render_template('mail_form.html')
