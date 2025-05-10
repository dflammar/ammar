"""
Django test script to check if Django is installed and configured correctly.
"""

import os
import sys
import importlib
import subprocess
import webbrowser
import time
import threading

def check_django():
    """Check if Django is installed and configured correctly"""
    print("="*50)
    print("Django Configuration Test")
    print("="*50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check if Django is installed
    try:
        import django
        print(f"Django version: {django.get_version()}")
    except ImportError:
        print("ERROR: Django is not installed")
        return False
    
    # Check if manage.py exists
    if not os.path.exists('manage.py'):
        print("ERROR: manage.py not found in current directory")
        return False
    else:
        print("manage.py found in current directory")
    
    # Check Django settings
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teacher_platform.settings')
        import teacher_platform.settings as settings
        print(f"Settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
        print(f"DEBUG: {settings.DEBUG}")
        print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"INSTALLED_APPS: {', '.join(settings.INSTALLED_APPS)}")
    except ImportError:
        print("ERROR: Could not import Django settings")
        return False
    
    # Check database configuration
    try:
        print(f"Database engine: {settings.DATABASES['default']['ENGINE']}")
        print(f"Database name: {settings.DATABASES['default']['NAME']}")
    except (AttributeError, KeyError):
        print("ERROR: Database configuration not found")
        return False
    
    # Check if database file exists (for SQLite)
    if 'sqlite3' in settings.DATABASES['default']['ENGINE']:
        db_path = settings.DATABASES['default']['NAME']
        if os.path.exists(db_path):
            print(f"Database file exists: {db_path}")
        else:
            print(f"WARNING: Database file does not exist: {db_path}")
    
    return True

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)
    url = 'http://127.0.0.1:9999'
    webbrowser.open(url)

def run_django_server():
    """Run Django development server"""
    if not check_django():
        print("\nDjango configuration check failed")
        input("Press Enter to exit...")
        return
    
    print("\nStarting Django development server...")
    
    # Open browser in a separate thread
    threading.Thread(target=open_browser).start()
    
    # Run Django server on port 9999
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver', '0.0.0.0:9999'])
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"\nError starting server: {str(e)}")
    
    print("\nServer stopped. Press Enter to exit...")
    input()

if __name__ == "__main__":
    run_django_server()
