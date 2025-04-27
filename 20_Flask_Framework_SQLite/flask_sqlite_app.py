# file: flask_sqlite_app.py

# Demonstrates how to use SQLite with Flask using SQLAlchemy

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sqlite_demo_secret'

# SQLite DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    if name and email:
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
    else:
        flash('Fields cannot be empty.', 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted!', 'info')
    return redirect(url_for('index'))
