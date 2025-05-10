@echo off
echo ===============================================
echo    STARTING DJANGO SERVER (SIMPLE MODE)
echo ===============================================
echo.

cd "%~dp0"
echo Current directory: %CD%
echo.

echo Starting Django server on port 7000...
echo.
echo Server will be available at: http://127.0.0.1:7000/simple/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 127.0.0.1:7000

echo.
echo Server stopped. Press any key to exit...
pause > nul
