# file: README.txt

# Flask Routing App

🧪 HOW TO RUN
-----------------------
1. Set up your virtual environment and install Flask:
   python -m venv venv
   venv\Scripts\activate
   pip install Flask

2. Run the app:
   set FLASK_APP=routing_app.py
   flask run

🔗 ROUTES AVAILABLE
-----------------------
/                      → Home Page  
/hello                 → Simple static route  
/user/<username>       → Dynamic route with string  
/post/<int:post_id>    → Dynamic route with integer  
/admin                 → Admin page  
/login                 → Login page  
/redirect-to-admin     → Redirects to /admin  
