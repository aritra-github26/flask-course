# file: app/auth/routes.py

# Sample routes for authentication
# Advanced concepts included as comments:
# - Blueprint usage for modular route grouping
# - Route decorators for login and logout
# - Redirects and URL building with url_for

from flask import render_template, redirect, url_for
from app.auth import bp

@bp.route('/login')
def login():
    # Render the login page template
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    # Redirect to the main index page on logout
    return redirect(url_for('main.index'))
