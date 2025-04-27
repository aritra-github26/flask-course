# file: README.txt

# Flask HTTP Methods App

🌐 SUPPORTED HTTP METHODS
------------------------------------
- GET: Request data
- POST: Submit data
- PUT: Update data
- DELETE: Delete data

🧪 HOW TO RUN
------------------------------------
1. Setup venv & install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Start server:
   set FLASK_APP=http_methods_app.py
   flask run

📫 TEST ROUTES
------------------------------------
- GET form UI at:  
  http://127.0.0.1:5000/

- POST form to:  
  http://127.0.0.1:5000/submit

- API endpoint (test with curl/Postman):  
  http://127.0.0.1:5000/api/data  
  Methods: GET, POST, PUT, DELETE
