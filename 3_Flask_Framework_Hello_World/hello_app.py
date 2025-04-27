# file: hello_app.py

# Minimal "Hello, World!" Flask application
# Advanced concepts included as comments:
# - Flask app creation and WSGI application
# - Route decorator for URL binding
# - Simple response returning plain text

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # Return a simple greeting message
    return "Hello, World from Flask!"
