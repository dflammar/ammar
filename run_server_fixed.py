import os
import sys
import traceback

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teacher_platform.settings')

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    # Import Django and run the server
    import django
    django.setup()
    
    from django.core.management import execute_from_command_line
    
    print(f"Django version: {django.get_version()}")
    print(f"Settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    print(f"Current directory: {os.path.abspath(os.path.dirname(__file__))}")
    print("Starting Django server...")
    
    # Run the server
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8080', '--traceback'])
    
except Exception as e:
    print("\n\n" + "="*80)
    print("ERROR DETAILS:")
    print("="*80)
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    print("\nTraceback:")
    traceback.print_exc()
    
    print("\nPlease fix the issues above and try again.")
