# file: README.txt

# Flask Static Files App

🎯 PURPOSE
----------------------------
Demonstrates how to serve static files in Flask — CSS, JavaScript, and images.

📁 FILE STRUCTURE
----------------------------
static_files_app.py
/templates/
    index.html
/static/
    /css/style.css
    /js/script.js
    /images/flask.png (add your own image here)

🧪 HOW TO RUN
----------------------------
1. Setup virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the app:
   set FLASK_APP=static_files_app.py
   flask run

3. Visit in browser:
   http://127.0.0.1:5000/

📝 NOTES
----------------------------
- Static files are stored in a folder named `static`.
- Use `url_for('static', filename='...')` to reference them in templates.
