# file: request_form_object_app.py

# Demonstrates use of request.form to access submitted form data

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    # Render a simple HTML form
    return render_template('user_form.html')

@app.route('/process', methods=['POST'])
def process_form():
    # Access form data using request.form (POST data)
    username = request.form.get('username')
    email = request.form.get('email')
    feedback = request.form.get('feedback')

    return f"""
        <h2>Form Submitted Successfully</h2>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Feedback:</strong> {feedback}</p>
    """
