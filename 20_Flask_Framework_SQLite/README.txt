# file: README.txt

# Flask + SQLite (CRUD Operations)

🎯 PURPOSE
----------------------------
Demonstrates:
- Setting up SQLite with SQLAlchemy in Flask
- Performing basic CRUD operations
- Dynamic UI rendering with templates

📁 FILE STRUCTURE
----------------------------
flask_sqlite_app.py
/templates/
    index.html

🧪 SETUP & USAGE
----------------------------
1. Install dependencies:
   pip install flask flask_sqlalchemy

2. Run the app:
   set FLASK_APP=flask_sqlite_app.py
   flask run

3. Visit:
   http://127.0.0.1:5000/

📌 NOTES
----------------------------
- Database: students.db will be created automatically
- Models must be declared before db.create_all()
- `Student.query.get_or_404(id)` ensures safety on deletion
