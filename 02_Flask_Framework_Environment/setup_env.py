# file: setup_env.py

# Script to set up a virtual environment and install basic Flask dependencies

import os
import subprocess
import sys

def create_virtualenv(env_name="venv"):
    if not os.path.exists(env_name):
        print(f"Creating virtual environment '{env_name}'...")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
    else:
        print(f"Virtual environment '{env_name}' already exists.")

def install_dependencies(env_name="venv"):
    pip_path = os.path.join(env_name, "Scripts" if os.name == "nt" else "bin", "pip")
    print("Installing Flask dependencies...")
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    create_virtualenv()
    install_dependencies()
