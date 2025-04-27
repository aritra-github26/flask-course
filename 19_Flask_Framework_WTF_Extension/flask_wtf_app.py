# file: flask_wtf_app.py

# Demonstrates Flask-WTF for form creation and validation

from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'wtf_secret_key'  # Required for CSRF protection

# Define a registration form using FlaskForm
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Normally save to database here
        flash(f'Registration successful for {form.name.data}!', 'success')
        return redirect(url_for('register'))
    return render_template('register_form.html', form=form)
