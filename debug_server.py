import os
import sys
import subprocess
import time

print("=== Django Server Debug ===")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Check if manage.py exists
if os.path.exists("manage.py"):
    print("✓ manage.py exists")
else:
    print("✗ manage.py does not exist")
    sys.exit(1)

# Check if teacher_platform directory exists
if os.path.exists("teacher_platform"):
    print("✓ teacher_platform directory exists")
else:
    print("✗ teacher_platform directory does not exist")
    sys.exit(1)

# Try to import Django
try:
    import django
    print(f"✓ Django is installed (version {django.get_version()})")
except ImportError:
    print("✗ Django is not installed")
    print("Installing Django...")
    subprocess.run([sys.executable, "-m", "pip", "install", "django==5.2"])
    try:
        import django
        print(f"✓ Django is now installed (version {django.get_version()})")
    except ImportError:
        print("✗ Failed to install Django")
        sys.exit(1)

# Try to run the server on port 7777
print("\nStarting Django server on port 7777...")
print("Server will be available at: http://127.0.0.1:7777/")

try:
    # Create a batch file to run the server
    with open("run_debug_server_7777.bat", "w") as f:
        f.write("""@echo off
echo ===============================================
echo    STARTING DJANGO SERVER (DEBUG)
echo ===============================================
echo.
echo Starting Django server on port 7777...
echo.
echo Server will be available at: http://127.0.0.1:7777/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 7777

echo.
echo Server stopped. Press any key to exit...
pause > nul
""")
    
    print("Created batch file: run_debug_server_7777.bat")
    print("Running the batch file...")
    
    # Run the batch file
    subprocess.Popen("start cmd /k run_debug_server_7777.bat", shell=True)
    
    print("Server should be starting in a new window.")
    print("Please wait a few seconds and then try accessing http://127.0.0.1:7777/ in your browser.")
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
