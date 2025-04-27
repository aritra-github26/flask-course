# file: app/__init__.py

# This module initializes the Flask application using the factory pattern
# Advanced concepts included as comments:
# - Application Factory Pattern for creating app instances
# - Initialization of Flask extensions (SQLAlchemy, Migrate, LoginManager)
# - Blueprint registration for modular app structure
# - Configuration management via Config class

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=Config):
    # Factory function to create Flask app instances
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app context
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Register blueprints inside the app context
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
