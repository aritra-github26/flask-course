# file: run.py

# Entry point for running the Flask application
# Advanced concepts included as comments:
# - Application factory usage for creating app instance
# - Shell context processor for flask shell convenience
# - Conditional app run for development with debug mode

from app import create_app, db
from app.models import User  # Example model if created

app = create_app()

# Optional: shell context for flask shell
@app.shell_context_processor
def make_shell_context():
    # Provides context variables for flask shell
    return {'db': db, 'User': User}

# Only runs if file is executed directly
if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)
