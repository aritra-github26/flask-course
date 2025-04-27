# file: README.txt

# Flask URL Building App

🔧 PURPOSE
----------------------------
This app demonstrates how to use Flask’s `url_for()` function to generate URLs dynamically based on the view function name and parameters.

🧪 HOW TO RUN
----------------------------
1. Setup environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the app:
   set FLASK_APP=url_building_app.py
   flask run

🌐 VISIT
----------------------------
http://127.0.0.1:5000/

🔗 OUTPUT EXAMPLE
----------------------------
Home URL: /
Login URL: /login
Profile URL (dynamic): /user/aritra

✅ BENEFITS OF `url_for()`
----------------------------
- Generates correct paths even if route paths change later
- Allows passing dynamic arguments
- Avoids hardcoding of URLs
