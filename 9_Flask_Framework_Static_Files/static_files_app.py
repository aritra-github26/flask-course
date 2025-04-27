# file: static_files_app.py

# Demonstrates usage of static files in Flask (CSS, JS, images)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
