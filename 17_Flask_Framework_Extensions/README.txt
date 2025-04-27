# file: README.txt

# Flask Extensions Demo

🎯 PURPOSE
----------------------------
Demonstrates:
- Using Flask-SQLAlchemy for ORM
- Managing DB migrations with Flask-Migrate
- Handling forms securely with Flask-WTF

📁 FILE STRUCTURE
----------------------------
flask_extensions_app.py
/templates/
    extensions_home.html

🧪 SETUP & USAGE
----------------------------
1. Install dependencies:
   pip install flask flask-sqlalchemy flask-migrate flask-wtf

2. Initialize DB and migrations:
   set FLASK_APP=flask_extensions_app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade

3. Run the app:
   flask run
   Visit: http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Add user via WTForms and store in SQLite DB
- Flash messages for feedback
- Bootstrap styling

📌 NOTES
----------------------------
- The `db.init_app()` and `Migrate(app, db)` link SQLAlchemy with Flask-Migrate
- Run `flask db migrate` whenever the model changes
