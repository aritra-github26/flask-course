# file: README.txt

# Flask-Mail Email Sending Demo

🎯 PURPOSE
----------------------------
Demonstrates:
- Sending emails using Flask-Mail
- Creating form for email input

📁 FILE STRUCTURE
----------------------------
flask_mail_app.py
/templates/
    mail_form.html

🧪 SETUP & USAGE
----------------------------
1. Install dependencies:
   pip install flask flask-mail

2. Update email settings in `flask_mail_app.py`:
   - MAIL_USERNAME: your Gmail
   - MAIL_PASSWORD: app password or real password (enable 2FA and use app password)

3. Run the app:
   set FLASK_APP=flask_mail_app.py
   flask run

4. Open in browser:
   http://127.0.0.1:5000/

✅ FEATURES
----------------------------
- Send email with subject, body
- Error handling and flash messages

📌 NOTES
----------------------------
- Use App Passwords for Gmail if 2FA is enabled
- Enable "Less secure app access" or use SMTP settings from other providers if needed
