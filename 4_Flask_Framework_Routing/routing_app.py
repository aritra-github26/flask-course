# file: routing_app.py

# Demonstration of various Flask routing techniques
# Advanced concepts included as comments:
# - Static and dynamic routing
# - URL variable rules and type converters
# - Redirects and URL building with url_for

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Static route for home page
    return "Welcome to the Home Page!"

@app.route("/hello")
def hello():
    # Static route for hello page
    return "Hello from Flask Routing!"

@app.route("/user/<username>")
def show_user_profile(username):
    # Dynamic routing using path variable
    return f"User Profile: {username}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Type-based routing: integer ID
    return f"Post ID: {post_id}"

@app.route("/admin")
def admin():
    # Static route for admin page
    return "Admin Page"

@app.route("/login")
def login():
    # Static route for login page
    return "Login Page"

@app.route("/redirect-to-admin")
def redirect_to_admin():
    # Redirecting to another route
    return redirect(url_for('admin'))
