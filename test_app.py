import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

# Configure Django settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY='your-secret-key',
    ROOT_URLCONF=__name__,
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    STATIC_URL='/static/',
)

# Define a simple view
def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Test App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            h1 {
                color: #4CAF50;
            }
            .success {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Django Test App</h1>
            <p class="success">✓ Django is working correctly!</p>
            <p>This is a simple test app to verify that Django is working properly.</p>
            <p>If you're seeing this page, it means the basic Django functionality is working.</p>
            <p>The issue with your main application might be related to specific dependencies or configuration.</p>
            
            <h2>Next Steps:</h2>
            <ol>
                <li>Try installing all required dependencies: <code>pip install -r requirements.txt</code></li>
                <li>Check for any errors in your Django project's settings or URLs</li>
                <li>Make sure all migrations are applied: <code>python manage.py migrate</code></li>
                <li>Check the Django debug page for more detailed error information</li>
            </ol>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

# Define URL patterns
urlpatterns = [
    path('', home, name='home'),
]

# Run the development server
if __name__ == '__main__':
    execute_from_command_line([sys.argv[0], 'runserver', '8888'])
