import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'teacher_platform.settings'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
