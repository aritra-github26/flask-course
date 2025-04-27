# file: app_structure_overview.py

# This file demonstrates a basic but scalable Flask project structure
# Advanced concepts included as comments:
# - Application Factory Pattern for creating app instances
# - Use of Flask extensions: SQLAlchemy, Migrate, LoginManager
# - Blueprint registration for modular app structure
# - Configuration management via Config class

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Initializing extensions
db = SQLAlchemy()  # Database instance
migrate = Migrate()  # DB migration handler
login = LoginManager()  # Login management
login.login_view = 'auth.login'  # Redirect to 'login' if unauthorized

def create_app(config_class=Config):
    # Factory function to create Flask app instances
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initializing extensions with the app context
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Registering blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
