# file: app/main/__init__.py

# Blueprint initialization for main app routes

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
