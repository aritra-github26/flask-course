# file: url_building_app.py

# Demonstrates URL building using Flask's url_for()

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Build URLs for other endpoints
    home_url = url_for('index')
    login_url = url_for('login')
    profile_url = url_for('profile', username='aritra')
    return f"""
    Home URL: {home_url} <br>
    Login URL: {login_url} <br>
    Profile URL (dynamic): {profile_url}
    """

@app.route('/login')
def login():
    return "This is the login page."

@app.route('/user/<username>')
def profile(username):
    return f"User Profile Page of {username}"
