# file: http_methods_app.py

# Demonstrates handling various HTTP methods in Flask routes

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Submit a Message</h2>
        <form method="POST" action="/submit">
            <input type="text" name="message" placeholder="Enter your message">
            <input type="submit" value="Send">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    # Accessing form data sent via POST
    message = request.form.get('message')
    return f"<h3>Received Message: {message}</h3>"

@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_data():
    # Handle different HTTP methods
    if request.method == 'GET':
        return "GET request received"
    elif request.method == 'POST':
        return "POST request received"
    elif request.method == 'PUT':
        return "PUT request received"
    elif request.method == 'DELETE':
        return "DELETE request received"
    else:
        return "Unsupported Method", 405
