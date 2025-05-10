@echo off
echo Starting Django server...

REM Try to activate the virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist "myenv\Scripts\activate.bat" (
    call myenv\Scripts\activate.bat
) else if exist "django_env\Scripts\activate.bat" (
    call django_env\Scripts\activate.bat
) else (
    echo No virtual environment found, using system Python
)

REM Install required packages
pip install django==5.2 django-admin-interface django-allauth pillow pyjwt cryptography

REM Try to run the server on port 8080
echo Running Django server on port 8080...
python manage.py runserver 8080

REM If we get here, the server has stopped
echo Server stopped. Press any key to exit.
pause
