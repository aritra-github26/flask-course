# file: app/models.py

# Example SQLAlchemy model for users
# Advanced concepts included as comments:
# - SQLAlchemy ORM model definition
# - Flask-Login UserMixin integration for user session management
# - User loader callback for Flask-Login

from app import db
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(64), index=True, unique=True)  # Username field
    email = db.Column(db.String(120), index=True, unique=True)  # Email field
    password_hash = db.Column(db.String(128))  # Hashed password

    def __repr__(self):
        return f'<User {self.username}>'

# Callback for loading user from user ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
