# file: flask_extensions_app.py

# Demonstrates usage of popular Flask extensions: Flask-SQLAlchemy, Flask-Migrate, Flask-WTF

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'extension_demo_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///extensions_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)

# Form using Flask-WTF
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Add User')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User "{form.username.data}" added!', 'success')
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('extensions_home.html', form=form, users=users)
