import os
import sys
import traceback
import logging
import django
from django.core.management import execute_from_command_line

# Configure logging to show all errors
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Set Django settings to show detailed errors
os.environ['DJANGO_DEBUG'] = 'True'
os.environ['PYTHONUNBUFFERED'] = '1'

try:
    # Try to run the Django server
    print("Starting Django server with detailed error reporting...")
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8080', '--traceback'])
except Exception as e:
    # Print detailed error information
    print("\n\n" + "="*80)
    print("ERROR DETAILS:")
    print("="*80)
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    print("\nTraceback:")
    traceback.print_exc()
    
    # Check for common issues
    print("\n\n" + "="*80)
    print("TROUBLESHOOTING:")
    print("="*80)
    
    # Check Django installation
    try:
        print(f"Django version: {django.get_version()}")
    except:
        print("Django is not properly installed")
    
    # Check database
    try:
        from django.db import connection
        connection.ensure_connection()
        print("Database connection: OK")
    except Exception as db_error:
        print(f"Database connection error: {str(db_error)}")
    
    # Check for missing migrations
    try:
        from django.db.migrations.loader import MigrationLoader
        loader = MigrationLoader(connection)
        if loader.detect_conflicts():
            print("Migration conflicts detected")
        else:
            print("No migration conflicts")
    except Exception as migration_error:
        print(f"Migration check error: {str(migration_error)}")
    
    # Check template directories
    from django.conf import settings
    print(f"Template directories: {settings.TEMPLATES[0]['DIRS']}")
    
    # Check static files
    print(f"Static files directories: {settings.STATICFILES_DIRS}")
    
    # Check media files
    print(f"Media root: {settings.MEDIA_ROOT}")
    
    print("\nPlease fix the issues above and try again.")
