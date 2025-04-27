# file: Dockerfile

# Dockerfile for deploying the Flask app using Gunicorn and Nginx

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port Gunicorn will run on
EXPOSE 5000

# Start the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask_app:app"]
