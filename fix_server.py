import os
import sys
import subprocess
import time
import socket
import shutil
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 50)
    print(f" {text} ".center(50, "="))
    print("=" * 50)

def print_step(text):
    print(f"\n>> {text}")

def run_command(command):
    print(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, 
                               capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error output: {e.stderr}")
        return False

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

def create_virtual_env():
    print_step("Creating a fresh virtual environment")
    
    # Check if any virtual environment already exists
    venv_dirs = ["venv", "env", "myenv", ".venv", "django_env", "fresh_env"]
    for venv in venv_dirs:
        if os.path.exists(venv):
            print(f"Found existing virtual environment: {venv}")
            return venv
    
    # Create a new virtual environment
    venv_name = "fresh_env"
    if run_command(f"{sys.executable} -m venv {venv_name}"):
        print(f"Created new virtual environment: {venv_name}")
        return venv_name
    else:
        print("Failed to create virtual environment")
        return None

def install_dependencies(venv_path):
    print_step("Installing required dependencies")
    
    # Construct the pip path
    pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
    if not os.path.exists(pip_path):
        print(f"Error: pip not found at {pip_path}")
        return False
    
    # Install dependencies
    dependencies = [
        "django==5.2",
        "django-admin-interface",
        "django-allauth",
        "pillow",
        "pyjwt",
        "cryptography",
        "requests"
    ]
    
    for dep in dependencies:
        if not run_command(f'"{pip_path}" install {dep}'):
            print(f"Failed to install {dep}")
            return False
    
    return True

def check_django_project():
    print_step("Checking Django project structure")
    
    if not os.path.exists("manage.py"):
        print("Error: manage.py not found in current directory")
        return False
    
    if not os.path.exists("teacher_platform"):
        print("Error: teacher_platform directory not found")
        return False
    
    if not os.path.exists("teacher_platform/settings.py"):
        print("Error: settings.py not found in teacher_platform directory")
        return False
    
    print("Django project structure looks good")
    return True

def apply_migrations(venv_path):
    print_step("Applying database migrations")
    
    # Construct the python path
    python_path = os.path.join(venv_path, "Scripts", "python.exe")
    if not os.path.exists(python_path):
        print(f"Error: Python not found at {python_path}")
        return False
    
    # Run migrations
    if not run_command(f'"{python_path}" manage.py migrate'):
        print("Failed to apply migrations")
        return False
    
    return True

def start_server(venv_path, port=8000):
    print_step(f"Starting Django server on port {port}")
    
    # Check if port is already in use
    if check_port(port):
        print(f"Warning: Port {port} is already in use. Trying a different port.")
        port = 8080
        if check_port(port):
            port = 9000
            if check_port(port):
                print("Error: All common ports (8000, 8080, 9000) are in use.")
                return False
    
    # Construct the python path
    python_path = os.path.join(venv_path, "Scripts", "python.exe")
    if not os.path.exists(python_path):
        print(f"Error: Python not found at {python_path}")
        return False
    
    # Start the server
    print(f"Starting server on http://127.0.0.1:{port}/")
    print("Press Ctrl+C to stop the server")
    
    # Create a batch file to run the server
    batch_file = "run_fixed_server.bat"
    with open(batch_file, "w") as f:
        f.write(f"""@echo off
echo ===============================================
echo    STARTING DJANGO SERVER (FIXED)
echo ===============================================
echo.
echo Starting Django server on port {port}...
echo.
echo Server will be available at: http://127.0.0.1:{port}/
echo.
echo Press Ctrl+C to stop the server
echo.

call "{os.path.join(venv_path, 'Scripts', 'activate.bat')}"
"{python_path}" manage.py runserver {port}

echo.
echo Server stopped. Press any key to exit...
pause > nul
""")
    
    print(f"Created batch file: {batch_file}")
    print(f"Run this file to start the server: {batch_file}")
    
    # Try to start the server directly
    try:
        subprocess.Popen(f'start cmd /k "{batch_file}"', shell=True)
        print("Server started in a new window")
        
        # Wait a moment for the server to start
        print("Waiting for server to start...")
        time.sleep(5)
        
        # Check if the server is running
        if check_port(port):
            print(f"Server is running on http://127.0.0.1:{port}/")
            return True
        else:
            print("Server may not have started properly")
            return False
    except Exception as e:
        print(f"Error starting server: {e}")
        return False

def main():
    print_header("Django Server Fix Script")
    
    # Step 1: Create/find virtual environment
    venv_path = create_virtual_env()
    if not venv_path:
        print("Failed to set up virtual environment")
        return
    
    # Step 2: Install dependencies
    if not install_dependencies(venv_path):
        print("Failed to install dependencies")
        return
    
    # Step 3: Check Django project structure
    if not check_django_project():
        print("Django project structure is incorrect")
        return
    
    # Step 4: Apply migrations
    if not apply_migrations(venv_path):
        print("Failed to apply migrations")
        return
    
    # Step 5: Start the server
    if not start_server(venv_path):
        print("Failed to start server")
        return
    
    print_header("Server Fix Complete")
    print("The Django server should now be running.")
    print("If you're still having issues, please check the terminal window")
    print("where the server is running for any error messages.")

if __name__ == "__main__":
    main()
