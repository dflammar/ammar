import sys
import os
import subprocess

print("=== Python Environment Check ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")

# Check for Django
try:
    import django
    print(f"Django is installed. Version: {django.get_version()}")
except ImportError:
    print("Django is NOT installed")

# Check for other required packages
required_packages = [
    "django-admin-interface",
    "django-allauth",
    "pillow",
    "pyjwt",
    "cryptography",
    "requests"
]

print("\n=== Required Packages ===")
for package in required_packages:
    try:
        __import__(package.replace("-", "_"))
        print(f"✓ {package} is installed")
    except ImportError:
        print(f"✗ {package} is NOT installed")

# Check for manage.py
print("\n=== Project Structure ===")
if os.path.exists("manage.py"):
    print("✓ manage.py exists")
else:
    print("✗ manage.py does not exist")

# Check for settings.py
if os.path.exists("teacher_platform/settings.py"):
    print("✓ teacher_platform/settings.py exists")
else:
    print("✗ teacher_platform/settings.py does not exist")

# Check for virtual environments
print("\n=== Virtual Environments ===")
venv_dirs = ["venv", "env", "myenv", ".venv", "django_env", "fresh_env"]
found_venvs = []
for venv in venv_dirs:
    if os.path.exists(venv):
        found_venvs.append(venv)
        print(f"Found virtual environment: {venv}")
        if os.path.exists(os.path.join(venv, "Scripts", "activate")):
            print(f"  - Activation script exists: {os.path.join(venv, 'Scripts', 'activate')}")

if not found_venvs:
    print("No virtual environments found")

# Check for port usage
print("\n=== Port Check ===")
ports_to_check = [8000, 8080, 9000]
for port in ports_to_check:
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        if result == 0:
            print(f"Port {port} is in use (something is already running on this port)")
        else:
            print(f"Port {port} is available")
    except Exception as e:
        print(f"Error checking port {port}: {e}")

print("\n=== Recommendations ===")
if not os.path.exists("manage.py"):
    print("- The manage.py file is missing. Make sure you're in the correct directory.")
elif not os.path.exists("teacher_platform/settings.py"):
    print("- The settings.py file is missing. The project structure might be incorrect.")
else:
    print("- The project structure looks correct.")

try:
    import django
except ImportError:
    print("- Django is not installed. Run: pip install django==5.2")

missing_packages = []
for package in required_packages:
    try:
        __import__(package.replace("-", "_"))
    except ImportError:
        missing_packages.append(package)

if missing_packages:
    print(f"- Missing packages: {', '.join(missing_packages)}. Run: pip install {' '.join(missing_packages)}")
