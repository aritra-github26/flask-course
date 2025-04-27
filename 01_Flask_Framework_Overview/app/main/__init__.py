# file: app/main/__init__.py

# Fixing duplicate blueprint name error by setting a unique name

from flask import Blueprint

bp = Blueprint('main_bp', __name__)  # Use a unique name like 'main_bp'

from app.main import routes
