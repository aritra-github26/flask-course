# file: variable_rules_app.py

# Demonstrates Flask's variable rules and converters in routing

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Variable Rules Demo!"

@app.route('/user/<username>')
def user_profile(username):
    # Capture username as string
    return f"Profile of user: {username}"

@app.route('/post/<int:post_id>')
def post(post_id):
    # Capture post_id as integer
    return f"Post ID: {post_id}"

@app.route('/path/<path:subpath>')
def subpath(subpath):
    # Capture a full path after /path/
    return f"Subpath is: {subpath}"

@app.route('/float/<float:price>')
def show_price(price):
    # Capture a float number
    return f"The price is: {price}"

@app.route('/uuid/<uuid:item_id>')
def show_uuid(item_id):
    # Capture UUID format
    return f"Item UUID is: {item_id}"
