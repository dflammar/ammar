import os
import sys
import traceback
import subprocess
import time

def run_server():
    print("=== Django Server Debug Script ===")
    print(f"Current directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")

    # Check if manage.py exists
    if not os.path.exists('manage.py'):
        print("ERROR: manage.py not found in current directory")
        return False

    # Check Django installation
    try:
        import django
        print(f"Django version: {django.get_version()}")
    except ImportError:
        print("ERROR: Django not installed")
        return False

    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teacher_platform.settings')
    print(f"Settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

    # Check if port 8888 is in use
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 8888))
        s.close()
        print("Port 8888 is available")
    except socket.error:
        print("WARNING: Port 8888 is already in use")

    try:
        # Import Django and run the server
        django.setup()

        from django.core.management import execute_from_command_line

        print("\nStarting Django server on port 8888...")
        print("Access the server at: http://127.0.0.1:8888/")
        print("Press Ctrl+C to stop the server")
        print("="*50)

        # Run the server with verbose output and traceback
        execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8888', '--verbosity=2', '--traceback'])

        return True

    except Exception as e:
        print("\n\n" + "="*80)
        print("ERROR DETAILS:")
        print("="*80)
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nTraceback:")
        traceback.print_exc()

        return False

if __name__ == "__main__":
    success = run_server()

    if not success:
        print("\nServer failed to start. Press Enter to exit...")
        input()
