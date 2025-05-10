@echo off
echo ===============================================
echo    STARTING DJANGO SERVER
echo ===============================================
echo.

cd "%~dp0"
echo Current directory: %CD%
echo.

echo Starting Django server...
echo.
echo Server will be available at: http://127.0.0.1:8000/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

echo.
echo Server stopped. Press any key to exit...
pause > nul
