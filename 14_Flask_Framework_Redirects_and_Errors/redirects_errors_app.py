# file: redirects_errors_app.py

# Demonstrates redirecting routes and handling errors in Flask

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/admin')
def admin():
    # Redirecting unauthorized user to error page
    return redirect(url_for('unauthorized'))

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html'), 401

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500
