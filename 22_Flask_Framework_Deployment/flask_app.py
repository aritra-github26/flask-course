# file: flask_app.py

# Sample production-ready Flask app for deployment demo

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from deployed Flask app!")

# WSGI-compatible callable
if __name__ == "__main__":
    app.run(debug=True)
