# file: flask_sqlalchemy_demo.py

# Demonstrates advanced usage of SQLAlchemy ORM with Flask

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Association of Books and Authors (One-to-Many relationship)
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    authors = Author.query.all()
    return render_template('index.html', authors=authors)

@app.route('/add_author', methods=['POST'])
def add_author():
    name = request.form['author_name']
    if name:
        db.session.add(Author(name=name))
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_book/<int:author_id>', methods=['POST'])
def add_book(author_id):
    title = request.form['book_title']
    if title:
        db.session.add(Book(title=title, author_id=author_id))
        db.session.commit()
    return redirect(url_for('index'))
