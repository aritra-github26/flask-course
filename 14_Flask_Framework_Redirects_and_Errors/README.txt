# file: README.txt

# Flask Redirects and Error Handling Demo

🎯 PURPOSE
----------------------------
Demonstrates:
- Redirecting users with `redirect()` and `url_for()`
- Handling errors like 404, 401, and 500 with `@app.errorhandler`

📁 FILE STRUCTURE
----------------------------
redirects_errors_app.py
/templates/
    home.html
    unauthorized.html
    404.html
    500.html

🧪 HOW TO RUN
----------------------------
1. Create virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the server:
   set FLASK_APP=redirects_errors_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

✅ TESTING FEATURES
----------------------------
- Click “Go to Admin Page” to test `redirect()`.
- Click “Trigger 404 Error” to test custom error handler.
- To test 500 error, you can manually raise an exception in a route.

📌 NOTES
----------------------------
- Use `redirect()` with `url_for()` for clean redirection logic.
- Custom error handlers improve user experience and debugging.
