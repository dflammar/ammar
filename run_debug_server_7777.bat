@echo off
echo ===============================================
echo    STARTING DJANGO SERVER (DEBUG)
echo ===============================================
echo.
echo Starting Django server on port 7777...
echo.
echo Server will be available at: http://127.0.0.1:7777/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 7777

echo.
echo Server stopped. Press any key to exit...
pause > nul
