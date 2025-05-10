import os
import sys

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("\nFiles and directories in current directory:")

try:
    for item in os.listdir("."):
        if os.path.isdir(item):
            print(f"[DIR] {item}")
        else:
            print(f"[FILE] {item}")
except Exception as e:
    print(f"Error listing directory: {e}")

print("\nChecking for Django installation:")
try:
    import django
    print(f"Django version: {django.get_version()}")
except ImportError:
    print("Django is not installed")
except Exception as e:
    print(f"Error importing Django: {e}")

print("\nChecking for manage.py:")
if os.path.exists("manage.py"):
    print("manage.py exists")
    with open("manage.py", "r") as f:
        print("\nFirst few lines of manage.py:")
        for i, line in enumerate(f):
            if i < 10:  # Print first 10 lines
                print(line.strip())
            else:
                break
else:
    print("manage.py does not exist")

print("\nChecking for virtual environments:")
venv_dirs = ["venv", "env", "myenv", ".venv", "django_env", "fresh_env"]
for venv in venv_dirs:
    if os.path.exists(venv):
        print(f"Found virtual environment: {venv}")
        if os.path.exists(os.path.join(venv, "Scripts", "activate")):
            print(f"  - Activation script exists: {os.path.join(venv, 'Scripts', 'activate')}")
