@echo off
echo ===============================================
echo    SIMPLE SERVER FIX
echo ===============================================
echo.

echo Step 1: Installing required packages...
pip install django==5.2 django-admin-interface django-allauth pillow pyjwt cryptography requests

echo.
echo Step 2: Checking for database...
if exist db.sqlite3 (
    echo Database found.
) else (
    echo Database not found. Creating...
    python manage.py migrate
)

echo.
echo Step 3: Starting server on port 9999...
echo.
echo Server will be available at: http://127.0.0.1:9999/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 9999

echo.
echo Server stopped. Press any key to exit...
pause > nul
