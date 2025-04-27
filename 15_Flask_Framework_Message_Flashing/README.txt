# file: README.txt

# Flask Flash Messaging Demo

🎯 PURPOSE
----------------------------
This example demonstrates how to:
- Use `flash()` to store temporary messages in the session
- Display those messages in the next request
- Style messages using Bootstrap alert classes

📁 FILE STRUCTURE
----------------------------
flash_message_app.py
/templates/
    flash_home.html

🧪 HOW TO RUN
----------------------------
1. Create virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the server:
   set FLASK_APP=flash_message_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Flash error and success messages
- Bootstrap alert styling
- Alerts are dismissible and only shown once

📌 NOTES
----------------------------
- `flash(message, category)` uses session under the hood.
- Use categories (`success`, `error`, `info`, etc.) for custom styling.
- Bootstrap makes flash messages user-friendly and visually clear.
