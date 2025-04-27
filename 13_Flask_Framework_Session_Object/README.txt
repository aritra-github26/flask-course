# file: README.txt

# Flask Session Object Demo

🎯 PURPOSE
----------------------------
Demonstrates usage of Flask `session` to:
- Store user-specific data across requests
- Simulate login/logout functionality

📁 FILE STRUCTURE
----------------------------
session_app.py
/templates/
    session_login.html
    session_home.html

🧪 HOW TO RUN
----------------------------
1. Setup virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the server:
   set FLASK_APP=session_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

📌 NOTES
----------------------------
- Flask's `session` uses cookies to store data on the client-side, securely signed using `secret_key`.
- You can store any serializable data in `session`.
- Always set a secure and unpredictable `app.secret_key` in production.
