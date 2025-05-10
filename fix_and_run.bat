@echo off
echo ===== Django Server Fix and Run =====
echo.

REM Create a fresh virtual environment
echo Creating a fresh virtual environment...
python -m venv fresh_env

REM Activate the virtual environment
echo Activating virtual environment...
call fresh_env\Scripts\activate.bat

REM Install all required packages
echo Installing required packages...
pip install django==5.2 django-admin-interface django-allauth pillow pyjwt cryptography requests

REM Apply migrations
echo Applying migrations...
python manage.py migrate

REM Run the server
echo.
echo Starting Django server on port 8080...
echo.
echo If you see this message, the server is running!
echo Access the site at: http://127.0.0.1:8080/
echo.
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver 8080

REM Keep the window open if there's an error
pause
