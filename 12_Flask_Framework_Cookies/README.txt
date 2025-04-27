# file: README.txt

# Flask Cookies Demo

🎯 PURPOSE
----------------------------
Demonstrates how to:
- Set cookies using `response.set_cookie()`
- Retrieve cookies using `request.cookies.get()`
- Delete cookies using `response.delete_cookie()`

📁 FILE STRUCTURE
----------------------------
cookies_app.py
/templates/
    cookie_home.html

🧪 HOW TO RUN
----------------------------
1. Setup virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Start the app:
   set FLASK_APP=cookies_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

📌 NOTES
----------------------------
- Cookies are stored in the browser.
- `max_age` specifies how long the cookie should live (in seconds).
- Cookies persist across requests until deleted or expired.
