# file: README.txt

# Flask Templates App

🎯 PURPOSE
----------------------------
Demonstrates how to render HTML templates using Flask and Jinja2 syntax.

📁 FILE STRUCTURE
----------------------------
templates_app.py
/templates/
    index.html

🧪 HOW TO RUN
----------------------------
1. Set up your environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the app:
   set FLASK_APP=templates_app.py
   flask run

3. Visit:
   http://127.0.0.1:5000/

📌 NOTES
----------------------------
- Templates should be placed inside a `templates` folder.
- Use `{{ variable }}` for data and `{% %}` for control statements.
