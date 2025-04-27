# file: app/main/routes.py

# Sample main routes
# Advanced concepts included as comments:
# - Blueprint usage for modular route grouping
# - Route decorator for URL binding
# - Template rendering with Jinja2

from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    # Render the main index page template
    return render_template('main/index.html')
