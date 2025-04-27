# file: README.txt

# Flask Variable Rules App

🎯 VARIABLE RULES USED
--------------------------------------
- <string> (default): captures a string (e.g. /user/John)
- <int>: captures an integer (e.g. /post/10)
- <float>: captures a float (e.g. /float/19.99)
- <path>: captures a full path including slashes (e.g. /path/some/long/path)
- <uuid>: captures a valid UUID (e.g. /uuid/123e4567-e89b-12d3-a456-426614174000)

🧪 RUNNING THE APP
--------------------------------------
1. Create virtual environment (optional):
   python -m venv venv && venv\Scripts\activate

2. Install Flask:
   pip install Flask

3. Run:
   set FLASK_APP=variable_rules_app.py
   flask run

🔗 SAMPLE URLS TO TEST
--------------------------------------
- http://127.0.0.1:5000/user/Aritra
- http://127.0.0.1:5000/post/123
- http://127.0.0.1:5000/float/45.67
- http://127.0.0.1:5000/path/this/is/a/test
- http://127.0.0.1:5000/uuid/123e4567-e89b-12d3-a456-426614174000
