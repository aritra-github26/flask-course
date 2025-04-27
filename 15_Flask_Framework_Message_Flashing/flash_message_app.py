# file: flash_message_app.py

# Demonstrates flashing messages in Flask using the session and Bootstrap alerts

from flask import Flask, flash, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'very_secret_key'  # Required to use flash messaging

@app.route('/')
def index():
    return render_template('flash_home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    if not name:
        flash('Name is required!', 'error')  # Flashing error message
    else:
        flash(f'Thank you for submitting, {name}!', 'success')  # Flashing success message
    return redirect(url_for('index'))
