import os
import sys
import subprocess

print("=== Simple Django Server Runner ===")

# Install required packages
print("Installing required packages...")
subprocess.run([sys.executable, "-m", "pip", "install", "django==5.2", "django-admin-interface", "django-allauth", "pillow", "pyjwt", "cryptography", "requests"])

# Check if manage.py exists
if not os.path.exists("manage.py"):
    print("Error: manage.py not found in current directory")
    sys.exit(1)

# Run migrations if needed
if not os.path.exists("db.sqlite3"):
    print("Database not found. Running migrations...")
    subprocess.run([sys.executable, "manage.py", "migrate"])

# Start the server on port 9999
print("\nStarting Django server on port 9999...")
print("Server will be available at: http://127.0.0.1:9999/")
print("Press Ctrl+C to stop the server\n")

try:
    subprocess.run([sys.executable, "manage.py", "runserver", "9999"])
except KeyboardInterrupt:
    print("\nServer stopped.")
