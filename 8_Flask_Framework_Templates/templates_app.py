# file: templates_app.py

# Demonstrates rendering HTML templates using Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renders a template with variables
    return render_template('index.html', name="Aritra", skills=["Python", "Flask", "SQL"])
