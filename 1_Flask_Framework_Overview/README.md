# file: README.txt

# Overview of the Flask App (Flask Framework Overview Project)

This app demonstrates a modular, production-ready Flask project using:
- Blueprint architecture (auth, main)
- SQLAlchemy ORM for models
- Flask-Migrate for database migrations
- Flask-Login for session management

======================================
📁 PROJECT STRUCTURE
======================================
flask-course/
│
├── app/
│   ├── __init__.py         # App factory function and extension initialization
│   ├── models.py           # SQLAlchemy models
│   ├── auth/               # Authentication blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/               # Main blueprint (home routes)
│   │   ├── __init__.py
│   │   └── routes.py
│   └── templates/
│       ├── auth/
│       │   └── login.html  # Sample login template
│       └── main/
│           └── index.html  # Homepage template
├── config.py               # App configuration
├── run.py                  # Main run script
└── README.txt              # Project instructions

======================================
🚀 HOW TO RUN (Developer Mode)
======================================
1. Install dependencies:
   pip install flask flask_sqlalchemy flask_migrate flask_login

2. Set environment variables:
   (Linux/macOS)
   export FLASK_APP=run.py
   export FLASK_ENV=development

   (Windows CMD)
   set FLASK_APP=run.py
   set FLASK_ENV=development

3. Run the app:
   flask run

4. Visit in browser:
   http://127.0.0.1:5000/

======================================
🧪 HOW TO INTERACT AS END USER
======================================
- Go to `/` for the homepage.
- Go to `/auth/login` for the login page.
- Currently, login is only a static form with no real authentication.
- Users can be added via database using shell or migration.

======================================
🔧 OPTIONAL: INIT DATABASE
======================================
flask db init        # Initialize migration repo (run once)
flask db migrate -m "Initial migration"
flask db upgrade     # Apply migrations to the database

======================================
✅ NEXT STEPS
======================================
- Add registration logic
- Integrate real login with password hashing
- Add user dashboards and protected routes
- Connect to PostgreSQL or other RDBMS

