# file: cookies_app.py

# Demonstrates how to set, get, and delete cookies in Flask

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Display the stored cookie if available
    user = request.cookies.get('username')
    return render_template('cookie_home.html', username=user)

@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    # Set a cookie with the username
    username = request.form.get('username')
    resp = make_response(f"<h3>Cookie has been set for {username}.</h3><a href='/'>Go Home</a>")
    resp.set_cookie('username', username, max_age=60*60*24)  # expires in 1 day
    return resp

@app.route('/delete_cookie')
def delete_cookie():
    # Delete the cookie
    resp = make_response("<h3>Cookie deleted.</h3><a href='/'>Go Home</a>")
    resp.delete_cookie('username')
    return resp
