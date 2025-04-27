# file: README.txt

# Flask Request Object Demo

🎯 PURPOSE
----------------------------
Demonstrates how to use Flask's `request` object to:
- Retrieve form data
- Access query parameters
- Read HTTP headers

📁 FILE STRUCTURE
----------------------------
request_object_app.py
/templates/
    form.html

🧪 HOW TO RUN
----------------------------
1. Set up virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Start the server:
   set FLASK_APP=request_object_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

4. Submit the form and observe the use of `request.form`, `request.args`, and `request.headers`.

📌 NOTES
----------------------------
- `request.form` is used for POSTed form data
- `request.args` retrieves query string parameters
- `request.headers` allows access to request headers
