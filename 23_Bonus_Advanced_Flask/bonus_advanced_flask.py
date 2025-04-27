# file: bonus_advanced_flask.py

# Bonus Lecture: Covers advanced Flask features - Blueprints, CLI commands, Contexts, Custom Error Handling

from flask import Flask, Blueprint, jsonify, g

# Create Flask App
app = Flask(__name__)

# ------------------------
# 1. BLUEPRINT STRUCTURE
# ------------------------
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/hello')
def hello_api():
    return jsonify(message="Hello from API Blueprint!")

app.register_blueprint(api_bp)


# ------------------------
# 2. CLI COMMANDS
# ------------------------
@app.cli.command("custom-hello")
def custom_hello():
    print("👋 Hello from custom Flask CLI command!")


# ------------------------
# 3. APP CONTEXT & g OBJECT
# ------------------------
@app.before_request
def before_any_request():
    g.user = "admin"  # Simulate user from session or DB

@app.route("/whoami")
def whoami():
    return jsonify(user=g.user)


# ------------------------
# 4. CUSTOM ERROR HANDLING
# ------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource Not Found"), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal Server Error"), 500


# ------------------------
# Run in Development
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
