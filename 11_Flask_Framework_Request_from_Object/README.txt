# file: README.txt

# Flask request.form Demo

🎯 PURPOSE
----------------------------
Demonstrates how to use `request.form` to access data submitted from an HTML form.

📁 FILE STRUCTURE
----------------------------
request_form_object_app.py
/templates/
    user_form.html

🧪 HOW TO RUN
----------------------------
1. Setup and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the server:
   set FLASK_APP=request_form_object_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

4. Fill the form and observe the output from `request.form`.

📌 NOTES
----------------------------
- `request.form` is a MultiDict storing POST form data.
- Use `.get('fieldname')` to safely retrieve submitted values.
