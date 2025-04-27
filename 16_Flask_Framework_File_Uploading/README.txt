# file: README.txt

# Flask File Upload Demo

🎯 PURPOSE
----------------------------
Demonstrates:
- Uploading files using Flask
- Validating file types
- Saving securely using `secure_filename()`

📁 FILE STRUCTURE
----------------------------
file_upload_app.py
/templates/
    upload.html
/uploads/
    [uploaded files will be stored here]

🧪 HOW TO RUN
----------------------------
1. Setup virtual environment and install Flask:
   python -m venv venv && venv\Scripts\activate
   pip install Flask

2. Run the app:
   set FLASK_APP=file_upload_app.py
   flask run

3. Open in browser:
   http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Secure file upload with filename sanitization
- Validation against allowed extensions
- Flash messages for success and errors

📌 NOTES
----------------------------
- Allowed extensions: txt, pdf, png, jpg, jpeg, gif
- Change `UPLOAD_FOLDER` and `ALLOWED_EXTENSIONS` as needed
- HTML form uses `enctype="multipart/form-data"` for file upload
