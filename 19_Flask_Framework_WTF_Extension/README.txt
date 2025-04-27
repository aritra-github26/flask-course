# file: README.txt

# Flask-WTF Extension Demo

🎯 PURPOSE
----------------------------
Demonstrates:
- Secure form handling using Flask-WTF
- Validations using WTForms
- Flash messaging and CSRF protection

📁 FILE STRUCTURE
----------------------------
flask_wtf_app.py
/templates/
    register_form.html

🧪 SETUP & USAGE
----------------------------
1. Install dependencies:
   pip install flask flask-wtf

2. Run the app:
   set FLASK_APP=flask_wtf_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Form rendering via Jinja2
- Server-side validation with instant feedback
- CSRF token integration by default

📌 NOTES
----------------------------
- Flask-WTF requires `app.secret_key`
- `form.hidden_tag()` includes CSRF token
- WTForms provides built-in validators
