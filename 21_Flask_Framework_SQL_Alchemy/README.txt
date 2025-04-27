# file: README.txt

# Flask + SQLAlchemy (ORM Relationships)

🎯 PURPOSE
----------------------------
Demonstrates:
- ORM relationships with SQLAlchemy in Flask
- Creating One-to-Many relations (Author → Books)
- Using Foreign Keys and backrefs

📁 FILE STRUCTURE
----------------------------
flask_sqlalchemy_demo.py
/templates/
    index.html

🧪 SETUP & USAGE
----------------------------
1. Install dependencies:
   pip install flask flask_sqlalchemy

2. Run the app:
   set FLASK_APP=flask_sqlalchemy_demo.py
   flask run

3. Open:
   http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Author and Book model with ForeignKey and relationship
- Dynamically list and add books to authors
- SQLAlchemy ORM abstraction for database access

📌 NOTES
----------------------------
- Relationships use backref and lazy loading
- Each Book entry is bound to one Author via `author_id`
- DB file `books_authors.db` created automatically
