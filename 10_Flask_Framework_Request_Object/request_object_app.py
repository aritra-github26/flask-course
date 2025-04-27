# file: request_object_app.py

# Demonstrates usage of Flask's request object to access form data, query parameters, and headers

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    # Renders a basic form to demonstrate the request object
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Accessing form data, query parameters, and headers using request object
    name = request.form.get('name')
    age = request.form.get('age')
    query_param = request.args.get('ref')
    user_agent = request.headers.get('User-Agent')
    
    return f"""
        <h2>Form Submitted</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
        <p>Query Param 'ref': {query_param}</p>
        <p>User-Agent: {user_agent}</p>
    """
