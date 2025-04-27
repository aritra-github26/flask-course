# file: session_app.py

# Demonstrates how to use Flask session object to store user data across requests

from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for using sessions

@app.route('/')
def index():
    # Check if user is logged in by checking session
    if 'username' in session:
        return render_template('session_home.html', username=session['username'])
    return render_template('session_login.html')

@app.route('/login', methods=['POST'])
def login():
    # Store username in session
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Remove username from session
    session.pop('username', None)
    return redirect(url_for('index'))
